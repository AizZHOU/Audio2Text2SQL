# **Audio2Text2SQL**
![框架图](框架_01.png)
## 项目简介

该项目旨在通过使用大语言模型（LLM）来实现从音频或文本输入生成SQL语句的功能。通过将用户的自然语言查询转化为结构化的SQL语句，可以大大简化数据查询的过程，尤其适用于不熟悉SQL语法的用户。

**功能特点**:
1. **多输入支持**: 支持音频和文本两种输入方式。
2. **高精度解析**: 使用先进的大语言模型进行自然语言处理，保证解析结果的准确性。
3. **多数据库支持**: 生成的SQL语句兼容多种数据库系统，如MySQL、PostgreSQL、SQLite等。

## 安装环境
```
pip install sentence_transformers -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install SpeechRecognition -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install baidu-aip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install pyaudio
另外的缺啥安啥
```
## 用法
- 到Hugging Face上下载embedding模型以及ASR模型后替换路径即可开始本项目
- Embedding模型[DMetaSoul/Dmeta-embedding-zh](https://hf-mirror.com/DMetaSoul/Dmeta-embedding-zh/tree/main)
- ASR模型[Systran/faster-whisper-small](https://hf-mirror.com/Systran/faster-whisper-small/tree/main)

**或者**

```
git lfs install
git clone https://hf-mirror.com/Systran/faster-whisper-small
git clone https://hf-mirror.com/DMetaSoul/Dmeta-embedding-zh
```

## 一些细节
- [all_data_process_unique.json](/dataset/all_data_process_unique.json)文件是从[CSpider](https://taolusi.github.io/CSpider-explorer/)中提取整理得来
- [Text2SQL](Text2SQL.ipynb)文件展示了从文本生成SQL查询语句的过程
- 其余文件均为可选的[文本/语音]生成SQL查询过程。其中，后缀为'auto'的文件是自动调用麦克风进行ASR转录并生成SQL查询；后缀为'manual'的文件则需手动点击进行转录，再次点击停止转录后进行ASR转录并生成SQL查询。


---
通过本项目，我们希望能够降低数据查询的门槛，让更多人能够轻松地从数据中获取所需的信息。期待您的参与与贡献！
