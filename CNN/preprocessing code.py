#Author: Disha Punjabi , Akhila Battula
# Deep Learning for Hindi Mood Classification
# March 30th 2016
import cPickle
import json
import ast
import codecs
import pickle
import numpy
import numpy as np 
from collections import defaultdict

vocabulary = defaultdict(float)
imp_data = []
lyricvector=[]

def read_write(stopwords,words):
   
    fp=open('songdump2.txt','r')
    temp=fp.read()
    word_map=ast.literal_eval(temp)
    features={}
    foldnumber=10
    for k,label in word_map.items():
        print label
        #print k - at each song level
        lyricwords= k.decode('utf-8').split(' ')
        #strip
        lyricwords = [w.strip('\n, )(.-24') for w in lyricwords]
        #remove stop words
        lyricwords=[j for j in lyricwords if not j in stopwords]
        for w in lyricwords: #at word level
            vocabulary[w]+=1
            if w in words:
                index=words.index(w)
                lyricvector.append(embeddings[index],)
        features[label]=lyricvector     # ADD song vectors and song labels 
        if 'sad' in label:
            datastruct  = {"y":0, 
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'tareef' in label:
            datastruct  = {"y":1,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'romantic' in label:
            datastruct  = {"y":2,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'devotional' in label:
            datastruct  = {"y":3,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'happy' in label:
            datastruct  = {"y":4,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'funny' in label:
            datastruct  = {"y":5,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'party' in label:
            datastruct  = {"y":6,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'satire' in label:
            datastruct  = {"y":7,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'naughty' in label:
            datastruct  = {"y":8,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'playful' in label:
            datastruct  = {"y":9,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'masti' in label:
            datastruct  = {"y":10,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'patriotic' in label:
            datastruct  = {"y":11,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'item' in label:
            datastruct  = {"y":12,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        
        if 'rock' in label:
            datastruct  = {"y":13,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
            
        if 'pop' in label:
            datastruct  = {"y":14,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'friendship' in label:
            datastruct  = {"y":15,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'motivational' in label:
            datastruct  = {"y":16,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'remix' in label:
            datastruct  = {"y":17,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'love' in label:
            datastruct  = {"y":18,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'dance' in label:
            datastruct  = {"y":19,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        if 'remix' in label:
            datastruct  = {"y":20,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,foldnumber)}
        imp_data.append(datastruct)

words, embeddings = pickle.load(open('polyglot-hi.pkl', 'rb'))
#word= words[10]
#print word
#print type(embeddings[10])
def vectors_drive(lyricvector, k=64):
    """
    Get word matrix. W[index] is the vector for word indexed by index
    """
    vocab_size = len(lyricvector)
    wordindexmap = dict()
    W = np.zeros(shape=(vocab_size+1, k), dtype='float32')            
    W[0] = np.zeros(k, dtype='float32')
    i = 1
    for word in lyricvector:
        W[i] = lyricvector[word]
        wordindexmap[word] = i
        i += 1
    return W, wordindexmap



stopwordfile = codecs.open("stop.txt", encoding='utf-8')
stopwords = [x.strip() for x in stopwordfile.readlines()]
#print str(stopwords)
read_write(stopwords)
#print (features)
#print vocab
#print imp_data
word2vec = {}
for w in vocabulary:
    if w in words:
        boundary=words.index(w)
        word2vec[w]=embeddings[boundary]
W, wordmap = vectors_drive(word2vec)
cPickle.dump([imp_data, W, wordmap, vocabulary], open("datafile.p", "wb"))



        


# ## 

# In[ ]:
