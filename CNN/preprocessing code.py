
# coding: utf-8

# In[1]:

import cPickle
import numpy
import json
import ast
import codecs
import pickle
import numpy
import numpy as np 
from collections import defaultdict
words, embeddings = pickle.load(open('polyglot-hi.pkl', 'rb'))


# In[2]:

word= words[10]
print word
print type(embeddings[10])


# In[3]:

vocab = defaultdict(float)
revs = []


# In[6]:

stopwordfile = codecs.open("stop.txt", encoding='utf-8')
stopwords = [x.strip() for x in stopwordfile.readlines()]

#print str(stopwords)

s=open('songdump2.txt','r')
c=s.read()
diction=ast.literal_eval(c)
features={}
cv=5
for k,label in diction.items():
    print label
    #print k - at each song level
    song_vec=[]
    song_words= k.decode('utf-8').split(' ')
    #strip
    song_words = [w.strip('\n, )(.-24') for w in song_words]
    #remove stop words
    song_words=[x for x in song_words if not x in stopwords]
    
    for w in song_words: #at word level
        vocab[w]+=1
        if w in words:
            idx=words.index(w)
            song_vec.append(embeddings[idx],)
        #else:
            #print w
            #print 'not in the dictionary:' + w + ' end'
        #print song_vec
    features[label]=song_vec     # ADD song vectors and song labels 
    if 'sad' in label:
        datum  = {"y":1, 
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,cv)}
    else:
        datum  = {"y":0,
                      "text":k,                             
                      "num_words": len(k.decode('utf-8').split(' ')),
                      "split": np.random.randint(0,cv)}
        
    revs.append(datum)
    
#print (features)
#print vocab
#print revs

w2v = {}
for w in vocab:
    if w in words:
        idx=words.index(w)
        w2v[w]=embeddings[idx]
        
def add_unknown_words(word_vecs, vocab, min_df=1, k=64):
    """
    For words that occur in at least min_df documents, create a separate word vector.    
    0.25 is chosen so the unknown vectors have (approximately) same variance as pre-trained ones
    """
    for word in vocab:
        if word not in word_vecs and vocab[word] >= min_df:
            word_vecs[word] = np.random.uniform(-0.25,0.25,k)   

def get_W(word_vecs, k=64):
    """
    Get word matrix. W[i] is the vector for word indexed by i
    """
    vocab_size = len(word_vecs)
    word_idx_map = dict()
    W = np.zeros(shape=(vocab_size+1, k), dtype='float32')            
    W[0] = np.zeros(k, dtype='float32')
    i = 1
    for word in word_vecs:
        W[i] = word_vecs[word]
        word_idx_map[word] = i
        i += 1
    return W, word_idx_map

add_unknown_words(w2v,vocab)
W, word_idx_map = get_W(w2v)
rand_vecs = {}
add_unknown_words(rand_vecs, vocab)
W2, _ = get_W(rand_vecs)
cPickle.dump([revs, W, W2, word_idx_map, vocab], open("mr.p", "wb"))
print W2
        


# ## 

# In[ ]:



