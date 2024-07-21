"""
作者：legionb
日期：2024年07月21日
"""
# import nltk
# nltk.download('wordnet')
#第一次用需要下载，后面直接注释掉就行
from nltk.corpus import wordnet as wn
poses={'n':'noun','v':'verb','s':'adj(s)','a':'adj','r':'adv'}
for synset in wn.synsets("good"):
    print("{}:{}".format(poses[synset.pos()],
                         ", ".join([l.name() for l in synset.lemmas()])))