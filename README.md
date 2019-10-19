BINARY PINJA
==============================

![GitHub release (latest by date)](https://img.shields.io/github/v/release/cakeoomoo/binarypinja)

![GitHub top language](https://img.shields.io/github/languages/top/cakeoomoo/binarypinja)
![GitHub repo size](https://img.shields.io/github/repo-size/cakeoomoo/binarypinja)
[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fcakeoomoo%2Fbinarypinja)


This tool has the ability to create datasets for several ML(machine learning) programs in a NLP(natural language processing).
The main feature is converted to disassembly-code from executable files in PE and ELF of x86_64, and make these CSV-files for easy handling in ML.
The advantage is more simpler usage, and to use on free and open-source without Paid tools like IDA-Python.


## FEATURES:

- Input
    - DirectoryPath :  `PEformat(.exe) files` or  `ELFformat exefiles`

- Output
    - `[dirname]_EP.csv`               :  Extract entry-point for all files
    - `[dirname]_EP_asm.csv`           :  Extract disassembly code from entry-point of all files at arbitrary bytes
    - `[dirname]_TEXTSec_asm.csv`      :  Extract disassembly code from text-section of all files
    - `[dirname]_TEXTSec_asm_TRANS.csv`:  Transform disassembly code from csvfile by arbitrary rules
    - `[dirname]_FUNC_asm.csv`         :  Extract disassembly code from all-function of all files(ELFbinary)
    - `[dirname]_FUNC_asm_TRANS.csv`   :  Transform disassembly code from csvfile by arbitrary rules(ELFbinary)

###### out_FUNC_asm.csv

![csv sample](https://github.com/cakeoomoo/binarypinja/blob/master/mics/csv_sample.png)


## HOW TO INSTALL:

```
pip3 install -r requirements.txt 
pip3 install .
```

## HOW TO INSTALL for Developper:

```
pip3 install -r requirements.txt 
pip3 install -e . 
```

## Usage:

```
pinja [INPUT_DIRPATH]
```

##### Example Command:

```
pinja --help
pinja data/infilePE
pinja -f elf data/infileELF  -b 180 -o OUTPUTNAME 
```

##### DEMO:

![usage](https://github.com/cakeoomoo/binarypinja/blob/master/mics/usage_gif01.gif)




## Use Case: Binarycode Similarity with pinja-dataset

###### Purpose: Get the binarycode similarity score by using pinja-dataset

###### Type: Machine Laernning of the Narural Language processing.

###### Overview: Output each similarity score as a numerical value from 0 to 1 for each binary code.

```
pip3 install pandas
pip3 install gensim
cd UseCase/
python3 use.py out_TEXTSec_asm.csv
```

###### DEMO: about 1 minuts

![usecase](https://github.com/cakeoomoo/binarypinja/blob/master/mics/UseCase.gif)


###### Source code

```python
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
```


--------

## Reference

[click](https://pypi.org/project/click/)

[capstone](https://www.capstone-engine.org/lang_python.html)

[glob](https://docs.python.org/3/library/glob.html)

[pefile](https://pypi.org/project/pefile/)

[pefile UsageExamples.md](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction)

[pefile.DIRECTORY_ENTRY](https://www.programcreek.com/python/example/50993/pefile.DIRECTORY_ENTRY)

[PEheader pefileformat.html](https://blog.kowalczyk.info/articles/pefileformat.html)

[elftools](https://github.com/eliben/pyelftools)

[elftools user's guide](https://github.com/eliben/pyelftools/wiki/User%27s-guide)

[elftools example](https://www.programcreek.com/python/example/105189/elftools.elf.elffile.ELFFile)

[ELF about elf](https://gist.github.com/DhavalKapil/2243db1b732b211d0c16fd5d9140ab0b)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
