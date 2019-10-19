#!/usr/bin/python3
# Usage: python3 use.py [CSVfile]

import pandas as pd
from gensim import models
import pprint
import sys

args = sys.argv
filename = args[1]

print('>>>> Read CSV PINJA dataset')
df = pd.read_csv(filename, header=0, index_col=0, dtype='str')
df = df.fillna('EMPTY')
asm_all = []
for row in df.values.tolist():
    asm_all.append([s for s in row if s != 'EMPTY'])

print('>>>> Make the ML model')
asmtext = []
for x in asm_all:
    asmtext.append(models.doc2vec.TaggedDocument(words=x, tags=[x[0]]))
model = models.Doc2Vec(asmtext, dm=1, vector_size=300, window=5, alpha=.025, min_alpha=.025, min_count=0, sample=1e-6)

print('>>>> Learning and Save model')
epoch_num = 8
for epoch in range(epoch_num):
    print('Epoch: {}'.format(epoch + 1))
    model.train(asmtext, epochs=model.iter, total_examples=model.corpus_count)
    model.alpha -= (0.025 - 0.0001) / (epoch_num - 1)
    model.min_alpha = model.alpha
model.save(filename + ".doc2vec")

print('>>>> Load model and Print Binary Code Similarity')
model = models.Doc2Vec.load(filename + '.doc2vec')
sim_list = []
for x in asm_all:
    sim_list.append([x[0], model.docvecs.most_similar([x[0]])])
pprint.pprint(sim_list)
