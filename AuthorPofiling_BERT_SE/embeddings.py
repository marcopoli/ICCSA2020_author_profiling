from numpy import asarray
from numpy import array
from numpy import asarray
from numpy import zeros
import numpy as np
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding

sentences = []
sa = np.zeros((150,1024))
sentences.append(sa)
sentences = np.array(sentences)
#print(sentences)

# load the whole embedding into memory
embeddings_index = dict()
f = open('/Volumes/MacPassport/embedding_2.txt')

prevId = 0
s = []
index = 0
numInsert = 0
for line in f:
    #print(line)
    values = line.split()
    word = values[0]
    idUser = word.split('_')[0]

    if index == 0:
        prevId = idUser

    if idUser != prevId and len(s)!= 0 and index != 0:
        numInsert = numInsert +1
        resto = np.zeros(((150 - len(s)),1024))
        s = np.array(s)
        s = np.concatenate((s, resto), 0)

        ls = []
        ls.append(s)
        #print(ls)
        ls = np.array(ls)
        ls = np.concatenate((sentences,ls),0)

        sentences = ls
        print(sentences.shape)
        s = []
        prevId = idUser

        if numInsert == 1:
            sentences = np.delete(sentences,0,axis=0)
            print(sentences)

    coefs = np.array(values[1:], dtype='float32')
    s.append(coefs)

    #embeddings_index[word] = coefs
    #print(embeddings_index)
    index = index+1
f.close()
print('Loaded %s word vectors.' % sentences.shape)
joblib.dump(sentences,'/Volumes/MacPassport/UMAP_AP_weighs.gz')
