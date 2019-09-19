BINARY PINJA
==============================

[![status](https://img.shields.io/badge/test-v0.0.1-ff7964.svg?style=for-the-badge)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)

This tool has the ability to create datasets for several ML(machine learning) programs in a NLP(natural language processing).
The main feature is converted to binary-code and disassembly-code from executable files, and make these CSV-files for the ML.
The advantage is more simpler usage, and to use on free and open-source without Paid tools like IDA-Python.


## FEATURE:

- Input
    - `PEformat(.exe) files`
    - `ELFformat execfiles`

- Output
    - `[dirname].csv`             :  Extract entry-point for all files
    - `[dirname].bin.csv`         :  Extract binary-code for all files
    - `[dirname].txtbin.csv`      :  Extract text section for all files
    - `[dirname].bin.asm.csv`     :  Convert to each disassembly files from all files
    - `[dirname].bin.asm.repl.csv`:  Transform disassembly code using arbitrary rules for easy handling in ML

- Output(command-option is --mode doc2vec)
    - Print on console :  the similarity comparison value at disassembly codes by using doc2vec


### HOW TO INSTALL:

```
pip3 install -r requirements.txt 
pip3 install .
```

### HOW TO INSTALL for Developper:

```
pip3 install -r requirements.txt 
pip3 install -e . 
```

### Usage:

```
pinja [INPUT_DIRPATH]
```

### Example Command:

```
pinja -m AEP256 test
pinja data/infilePE -f pe
pinja data/infileELF -f elf
```

### DEMO:

pendding...


![pinjaTree](https://github.com/cakeoomoo/binarypinja/blob/master/image.jpg "pinja tree")



Project Organization
------------
    
    binarypinja
    │ 
    │ 
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

### Reference(for ALL contributor):

[click----https://pypi.org/project/click/](https://pypi.org/project/click/)

[capstone----https://www.capstone-engine.org/lang_python.html](https://www.capstone-engine.org/lang_python.html)

[glob----https://docs.python.org/3/library/glob.html](https://docs.python.org/3/library/glob.html)

[elftools----https://github.com/eliben/pyelftools](https://github.com/eliben/pyelftools)

[elftools-user's-guide----https://github.com/eliben/pyelftools/wiki/User%27s-guide](https://github.com/eliben/pyelftools/wiki/User%27s-guide)



[pefile----https://pypi.org/project/pefile/](https://pypi.org/project/pefile/)

[refer blog----https://dev.to/icyphox/python-for-reverse-engineering-1-elf-binaries-1fo4](https://dev.to/icyphox/python-for-reverse-engineering-1-elf-binaries-1fo4)



[ELF----https://unix.stackexchange.com/questions/418354/understanding-what-a-linux-binary-is-doing](https://unix.stackexchange.com/questions/418354/understanding-what-a-linux-binary-is-doing)

[ELF----https://gist.github.com/DhavalKapil/2243db1b732b211d0c16fd5d9140ab0b](https://gist.github.com/DhavalKapil/2243db1b732b211d0c16fd5d9140ab0b)




--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
