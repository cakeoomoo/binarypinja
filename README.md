BINARY PINJA
==============================

[![status](https://img.shields.io/badge/test-v0.0.1-ff7964.svg?style=for-the-badge)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)


This project is to make dataset for sevearal machine learnning program and model of the natural processng language.


## FEATURE:

- Output CSVfiles
    - `[dirname].csv`             :  Extract entrypoint for all files
    - `[dirname].bin.csv`         :  Extract binarycode for all files
    - `[dirname].allbin.csv`      :  Extract text section for all files
    - `[dirname].bin.asm.csv`     :  Convert disassembly files for all files
    - `[dirname].bin.asm.repl.csv`:  Replace to arbitrary code from code of disassembly files for all files

- Output similary comparison with disassembly code by using doc2vec 
    - Print list on CLI


### HOW TO INSTALL:

```
pip3 install .      (non check)
```

### HOW TO INSTALL(developper):

```
pip3 install -r requirements.txt 
pip3 install -e . 
```

### Usage:

```
pinja [INPUT_DIRPATH]
pinja --help
```

### Example:

```
pinja -m AEP256 test
```

### DEMO:

pendding...


![pinjaTree](https://github.com/cakeoomoo/binarypinja/blob/master/image.jpg "pinja tree")



Project Organization
------------

    ├── data
    │   ├── infileELF
    │   ├── infileELF_1file
    │   └── infilePE
    ├── image.jpg
    ├── LICENSE
    ├── pinja
    │   ├── bin2asm
    │   │   └── bin2asm.py  <--------------------working!!!
    │   ├── color
    │   │   ├── color.py
    │   ├── getfileinfo
    │   │   └── getfileinfo.py  <--------------------working!!!
    │   ├── getbin
    │   │   └── getbin.py <--------------------todo!!!
    │   ├── __init__.py
    │   ├── main.py
    │   └── reference
    │       ├── AEP256_01.py
    │       └── use_doc2vec.py
    ├── README.md
    ├── requirements.txt
    └── setup.py

--------

### Reference(for ALL committer):

#### library manual* 
[https://pypi.org/project/click/](https://pypi.org/project/click/)

[https://www.capstone-engine.org/lang_python.html](https://www.capstone-engine.org/lang_python.html)

[https://docs.python.org/3/library/glob.html](https://docs.python.org/3/library/glob.html)

[https://github.com/eliben/pyelftools](https://github.com/eliben/pyelftools)

[https://pypi.org/project/pefile/](https://pypi.org/project/pefile/)


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
