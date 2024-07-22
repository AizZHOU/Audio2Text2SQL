# Audio2Text2SQL
### 项目简介

**项目名称**: 基于LLM的音频/文本SQL语句生成器

**项目描述**:
该项目旨在通过使用大语言模型（LLM）来实现从音频或文本输入生成SQL语句的功能。通过将用户的自然语言查询转化为结构化的SQL语句，可以大大简化数据查询的过程，尤其适用于不熟悉SQL语法的用户。

**功能特点**:
1. **多输入支持**: 支持音频和文本两种输入方式。
2. **高精度解析**: 使用先进的大语言模型进行自然语言处理，保证解析结果的准确性。
3. **多数据库支持**: 生成的SQL语句兼容多种数据库系统，如MySQL、PostgreSQL、SQLite等。

**安装环境**
```
pip install sentence_transformers -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install SpeechRecognition -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install baidu-aip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install pyaudio
另外的缺啥安啥
```

---
通过本项目，我们希望能够降低数据查询的门槛，让更多人能够轻松地从数据中获取所需的信息。期待您的参与与贡献！
