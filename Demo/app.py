from openai import AzureOpenAI
from aip import AipSpeech
import gradio as gr
from sentence_transformers import SentenceTransformer
import os
import re
from sklearn.metrics.pairwise import euclidean_distances
from pydub import AudioSegment
from io import BytesIO
from flask import Flask
import pika
import json

# OPENAI-API配置
AZURE_OPENAI_API_KEY = '4213f3298d82495a8fdaf5e838402493'
AZURE_OPENAI_ENDPOINT = 'https://yidu-resource-4.openai.azure.com/'
os.environ['AZURE_OPENAI_API_KEY'] = AZURE_OPENAI_API_KEY
os.environ['AZURE_OPENAI_ENDPOINT'] = AZURE_OPENAI_ENDPOINT
os.environ['OPENAI_API_VERSION'] = '2024-05-01-preview'

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# flask http 应用
app = Flask(__name__)

# RabbitMQ连接配置
RABBITMQ_HOST = '120.76.47.158'
RABBITMQ_VHOST = 'my_vhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'admin'
RABBITMQ_PASS = '123456'
RABBITMQ_QUEUE = 'bi_queue'

# 连接到RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT,
                              credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS),
                              virtual_host=RABBITMQ_VHOST)
)
channel = connection.channel()


def get_completion(prompt, model="gpt-4o"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def encode_questions(embedding_model, questions):
    return embedding_model.encode(questions, normalize_embeddings=True)

def load_model(model_path):
    return SentenceTransformer(model_path)

embedding_model_path = '/app/model/Dmeta-embedding-zh'
embedding_model = load_model(embedding_model_path)

all_data_path = '/app/dataset/all_data_process_unique.json'
all_data = load_json(all_data_path)

questions = [item['question'] for item in all_data]
queries = [item['query'] for item in all_data]
mask_queries = [item['mask_query'] for item in all_data]

question_embeddings = encode_questions(embedding_model, questions)

# 加载百度asr模型
BAIDU_APP_ID = 'BAIDU_APP_ID'
BAIDU_API_KEY = 'BAIDU_API_KEY'
BAIDU_SECRET_KEY = 'BAIDU_SECRET_KEY'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)

def compute_distances(question_embedding, question_embeddings):
    return euclidean_distances(question_embedding, question_embeddings).squeeze()

def extract_sql(query):
    query = query.replace("### SQL:", "").replace("###", "").replace("#", "")
    sql_patterns = [r"```SQL(.*?)```", r"```SQL(.*?)", r"```sql(.*?)```", r"```sql(.*?)"]
    for pattern in sql_patterns:
        matches = re.findall(pattern, query.replace('\n', ' '))
        if matches:
            return matches[0].strip()
    return query.replace('\n', '').replace("`", "").strip()

def generate_prompt(examples, create_table_sql_prompt, question, database_records_prompt):
    return f"""
### 以下是基于类似问题提供的一些问题和相应的SQL查询的示例对：
{examples}
### 仅通过SQLite SQL查询回答问题，不需要解释。您必须在确保正确性的同时最小化SQL执行时间。
### 给定以下数据库架构:
#
{create_table_sql_prompt}
#
### 以下是相关数据库中引用的一些数据信息:
#
{database_records_prompt}
#
### 问题:{question}
### SQL:
"""

def jaccard_similarity(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def compute_combined_scores(distances, mask_similarities, threshold):
    return [(i, distances[i], mask_similarities[i]) for i in range(len(distances)) if mask_similarities[i] >= threshold]

def filter_prompt_lines(prompt, found_tables):
    filtered_prompt = []
    for line in prompt.split('\n'):
        if line.startswith("# ") and len(line) > 3:
            if any(table in line for table in found_tables):
                filtered_prompt.append(line)
        else:
            filtered_prompt.append(line)
    return "\n".join(filtered_prompt)

def add_comment_to_sql(sql):
    return "\n".join(["# " + line for line in sql.strip().split("\n")])

def process_sql(sql):
    sql = sql.replace('`', '')
    sql = re.sub(r"ENGINE=.*? COLLATE=.*?(?=\n|$)", '', sql)
    sql = re.sub(r'\)(\s*CREATE TABLE|\s*$)', r');\1', sql)
    return sql.strip()

def extract_table_info(sql):
    table_regex = re.compile(r'CREATE TABLE\s+(\w+(?:\.\w+)?)\s*\((.*?)\);', re.DOTALL | re.IGNORECASE)
    column_regex = re.compile(r'(\w+)\s+[^\s,]+.*?(?:,|$)', re.IGNORECASE)
    tables = table_regex.findall(sql)
    table_info = []

    for table in tables:
        table_name = table[0]
        columns = column_regex.findall(table[1])
        filtered_columns = [col for col in columns if 'PRIMARY' not in col.upper() and 'UNIQUE' not in col.upper() and 'KEY' not in col.upper()]
        table_info.append(f"{table_name} ({', '.join(filtered_columns)})")

    return table_info

def format_sql_statements(sql):
    # 去除前后的空格和换行符
    sql = sql.strip()

    # 使用正则表达式匹配每个完整的SQL语句
    statements = re.split(r';\s*', sql)

    formatted_statements = []
    for statement in statements:
        if statement.strip():
            # 将所有换行符替换为空格
            single_line_statement = " ".join(statement.split())
            formatted_statements.append(single_line_statement + ";")

    return "\n".join(formatted_statements)

def main(your_question, create_table_sql, database_records):
    if not create_table_sql.strip():
        return "ERROR: 创建表的SQL语句不能为空。", ""

    your_question_embedding = encode_questions(embedding_model, [your_question])
    distances = compute_distances(your_question_embedding, question_embeddings)
    k = 5
    top_k_indices = distances.argsort()[:k]
    examples = "\n".join([f"### {questions[idx]}\n{queries[idx]}\n" for idx in top_k_indices]).strip()

    process_sql1 = process_sql(create_table_sql)
    formatted_sql = format_sql_statements(process_sql1)
    table_info = extract_table_info(formatted_sql)

    create_table_sql_prompt = add_comment_to_sql(formatted_sql)

    formatted_database_records = format_sql_statements(database_records)
    database_records_prompt = add_comment_to_sql(formatted_database_records)

    prompt = generate_prompt(examples, create_table_sql_prompt, your_question, database_records_prompt)
    response = get_completion(prompt)
    response_extract = extract_sql(response)

    table_names = []
    column_set = []

    for info in table_info:
        table_name, columns = info.split(' (')
        table_names.append(table_name.strip())
        columns = columns.strip(')').split(', ')
        column_set.extend(columns)

    table_names = list(set(table_names))
    column_set = list(set(column_set))
    found_tables = [table for table in table_names if table in response_extract and table.startswith('t_')]

    response_mask = response_extract
    for table in table_names:
        response_mask = re.sub(r'\b' + table + r'\b', '<mask>', response_mask)

    for column in column_set:
        response_mask = re.sub(r'\b' + column + r'\b', '<unk>', response_mask)

    mask_similarities = [jaccard_similarity(response_mask, mask_query) for mask_query in mask_queries]
    threshold = 0.4
    combined_scores = compute_combined_scores(distances, mask_similarities, threshold)
    combined_scores = sorted(combined_scores, key=lambda x: x[1])
    top_pairs = [x for x in combined_scores if x[2] >= threshold]

    top_k_indices = [x[0] for x in top_pairs[:k]]
    examples_new = "\n".join([f"### {questions[idx]}\n{queries[idx]}\n" for idx in top_k_indices]).strip()

    prompt_new = generate_prompt(examples_new, create_table_sql_prompt, your_question, database_records_prompt)
    prompt_final = filter_prompt_lines(prompt_new, found_tables)
    response_final = get_completion(prompt_final)
    response_final = extract_sql(response_final)
    return response_final, prompt_final

def recognize_speech(audio):
    sr, y = audio
    # 创建AudioSegment对象
    audio_segment = AudioSegment(
        data=y.tobytes(),
        sample_width=y.dtype.itemsize,
        frame_rate=sr,
        channels=1
    )

    # 确保音频为单声道并将采样率转换为16kHz
    if audio_segment.channels > 1:
        audio_segment = audio_segment.set_channels(1)
    if audio_segment.frame_rate != 16000:
        audio_segment = audio_segment.set_frame_rate(16000)

    # 将音频数据转换为WAV格式的字节流
    wav_io = BytesIO()
    audio_segment.export(wav_io, format="wav")
    audio_data = wav_io.getvalue()

    # 调用百度语音识别API进行语音识别
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1536})

    if ret and ret['err_no'] == 0:
        result = ''.join(ret['result'])
        return result
    else:
        return "识别失败: " + ret['err_msg']

def process_input(input_choice, input_data, create_table_sql, database_records):
    if not create_table_sql.strip():
        return "ERROR：创建表的SQL语句不能为空。", '----', '----'

    if input_choice == '语音输入':
        recognized_text = recognize_speech(input_data)
        your_question = recognized_text
    elif input_choice == '文字输入':
        recognized_text = '----'
        your_question = input_data
    else:
        return "ERROR：请选择输入方式", '----', '----'

    final_sql, final_prompt = main(your_question, create_table_sql, database_records)
    return final_sql, recognized_text, final_prompt

# Gradio demo
def demo_fn(input_choice, audio_input, text_input, create_table_sql, database_records):
    input_data = audio_input if input_choice == "语音输入" else text_input
    final_sql, transcribed_text, final_prompt = process_input(input_choice, input_data, create_table_sql, database_records)
    return final_prompt, transcribed_text, final_sql


# 定义一个回调函数来处理队列中的消息
def callback(ch, method, properties, body):
    # 将消息体从字节串解码为 UTF-8 字符串
    message_str = body.decode('utf-8')
    message_dict = json.loads(message_str)
    query_id = message_dict['id']
    prompt = message_dict['prompt']
    create_table_sql = message_dict['createTableSqlList']
    database_records = message_dict['defaultRows']
    response_final, prompt_final = main(prompt, create_table_sql, database_records)
    print(create_table_sql)
    print(database_records)
    print('-----分隔符')
    print(response_final)
    print(prompt_final)
    print(query_id)
    # 向java后台发送消息
    result = {}
    result['id'] = query_id
    result['generateSql'] = response_final
    print('-----分隔符')
    print(response_final)
    print(query_id)
    result = json.dumps(result)
    print(result)
    channel.basic_publish(exchange='bi_exchange',  routing_key='update_sql',  body=result)

demo = gr.Interface(
    fn=demo_fn,
    inputs=[
        gr.Radio(choices=["语音输入", "文字输入"], label="选择输入方式"),
        gr.Audio(sources=["microphone"]),
        gr.Textbox(label="请输入您的问题"),
        gr.Textbox(label="输入创建表的SQL语句", lines=10, placeholder="必填项，每个表请以';'进行分隔，在每个字段后面加入COMMENT信息会让结果更加精确\n示例：CREATE TABLE t_device_online_status (id INT PRIMARY KEY AUTO_INCREMENT COMMENT '序号',mac_id CHAR(16) NOT NULL COMMENT '设备id',login TINYINT(1) NOT NULL COMMENT '设备上下线状态，设备上线：1，设备下线：0',created TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间');"),
        gr.Textbox(label="输入数据表的具体数据信息", lines=10, placeholder="可选项，每个表的信息请以';'进行分隔，添加这部分可使结果更加精确\n示例：t_device_online_status (id [1, 2, 3], mac_id [0012*************4057, 0012*************3747, 0012*************5913],login [1, 1, 1],created [2024-07-01 00:00:00.0, 2024-07-01 00:00:00.0, 2024-07-01 00:00:00.0],modified [2024-07-01 03:24:30.0, 2024-07-01 23:55:40.0, 2024-07-01 23:20:40.0]);")
    ],
    outputs=[
        gr.Textbox(label="Final-Prompt"),
        gr.Textbox(label="语音识别结果"),
        gr.Textbox(label="生成的SQL查询")
    ],
    title="Speech2Text2SQL",
    description="通过语音或文字输入问题，生成相应的SQL查询。",
)

# 开始消费队列中的消息
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)


if __name__ == "__main__":
    # demo.launch()
    # prompt to sql
    # input_choice = '文字输入'
    # input_data = '查询设备记录'
    # create_table_sql = "CREATE TABLE t_device_online_status (id INT PRIMARY KEY AUTO_INCREMENT COMMENT '序号',mac_id CHAR(16) NOT NULL COMMENT '设备id',login TINYINT(1) NOT NULL COMMENT '设备上下线状态，设备上线：1，设备下线：0',created TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间');"
    # database_records = "t_device_online_status (id [1, 2, 3], mac_id [0012*************4057, 0012*************3747, 0012*************5913],login [1, 1, 1],created [2024-07-01 00:00:00.0, 2024-07-01 00:00:00.0, 2024-07-01 00:00:00.0],modified [2024-07-01 03:24:30.0, 2024-07-01 23:55:40.0, 2024-07-01 23:20:40.0]);"
    # final_sql, transcribed_text, final_prompt = process_input(input_choice, input_data, create_table_sql,database_records)
    # print(final_sql)

    # 在后台线程中开始消费RabbitMQ消息
    import threading
    threading.Thread(target=lambda: channel.start_consuming()).start()
    # 运行Flask应用
    app.run(debug=True, host='localhost', port=5001)
