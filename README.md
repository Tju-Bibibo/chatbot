# 基于tf-idf的搜索型对话系统

## 数据来源
这里我获取的是GIthub上开源的数据集`https://github.com/hailiang-wang/egret-wenda-corpus.git`，这版语料，是从白鹭时代官方论坛问答板块**10,000+** 问题中，选择被标注了“最佳答案”的纪录汇总而成。目前，语料库包含了2907个问答。

## 目录说明  

    stopwordList
    	文件夹是停用词的数据
    dataclear.py
    	用来预处理数据的文件
    jiebaSegment.py 
    	封装好的结巴分词，支持多种切分模式
    sentence.py
      封装好的读取句子的类
    sentenceSimilarity.py
    	tf-idf模型
    tmodel.py
    	直接利用模型的问答
    tmode2.py  
    	加入倒排索引后的问答
    	语料库存储在hdfs上

## 结果展示：  
<img src="https://i.loli.net/2021/05/12/rSy27Z5YkFuXdD9.png" alt="image-20210511225109663" style="zoom:50%;" />