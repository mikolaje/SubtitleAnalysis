### 文本分析过程简介

- extract_transcript.py  脚本用来处理下载的原始字幕文件 .ass 文件
- 过滤出的subtitle 放在 filtered_subtitles, 每行用 "\b0\b1\b2---" 用分割 中文字幕和英文字幕
- 文本处理方面，用了NLTK以及spacy 这两个Python的NLP 模块
- 作图用了Matplotlib 和 Seaborn
