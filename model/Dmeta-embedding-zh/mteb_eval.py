import logging
import functools
from mteb import MTEB
from sentence_transformers import SentenceTransformer
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

# task_list
task_list = ['Classification', 'Clustering', 'Reranking', 'Retrieval', 'STS', 'PairClassification']
# languages
task_langs=["zh", "zh-CN"]

model_name = "DMetaSoul/Dmeta-embedding"
model = SentenceTransformer(model_name)
# normalize_embeddings should be true for this model
model.encode = functools.partial(model.encode, normalize_embeddings=True)
evaluation = MTEB(task_types=task_list, task_langs=task_langs)
evaluation.run(model, output_folder=f"results/zh/{model_name.split('/')[-1]}")