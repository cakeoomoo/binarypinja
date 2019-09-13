BINARY PINJA
==============================

[![status](https://img.shields.io/badge/test-v0.0.1-ff7964.svg?style=for-the-badge)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)


This project is to make dataset for sevearal machine learnning program and model of the natural processng language.


## FEATURE:

- output CSVfiles
    - [dirname].csv :  extract entrypoint for all files
    - [dirname].bin.csv :  extract binarycode for all files
    - [dirname].allbin.csv :  extract text section for all files
    - [dirname].bin.asm.csv :  convert disassembly files for all files
    - [dirname].bin.asm.repl.csv :  replace to arbitrary code from code of disassembly files for all files

- output similary comparison with disassembly code by using doc2vec 
    - print list on CLI


### HOW TO INSTALL:

```
pip3 install .      (non check)
```

### HOW TO INSTALL(developper):

```
pip3 install -r requirements.txt 
pip3 install -e . 
```

### HOW TO USE:

```
pinja [input-directory]
pinja --help
```

### Example:

```
pinja -m AEP256 test
```

### DEMO:

pendding...


![pinjaTree](http://github.com/cakeoomoo/binarypinja/image.jpg "pinja tree")



Project Organization
------------

    ├── data  <--------------------dataset
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
    │   │   └── getfileinfo.py <--------------------todo!!!
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

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
