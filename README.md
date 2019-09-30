BINARY PINJA
==============================

[![status](https://img.shields.io/badge/test-v0.0.1-ff7964.svg?style=for-the-badge)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)

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
pinja data/testfile_pe
pinja --help
pinja -f pe data/infilePE -b 180
pinja -f elf data/infilePE -o DATASET001 
pinja -f elf data/infileELF
pinja -f elf data/infileELF -o DATASET002 
```

### DEMO:



![pinjaTree](https://github.com/cakeoomoo/binarypinja/blob/master/image.jpg "pinja tree" {width=200px height=200px})


Project Organization
------------
    
  binarypinja
    ├── data
    │   ├── infileELF
    │   ├── infilePE
    │   ├── _misc
    │   ├── outfileELF
    │   └── outfilePE
    ├── image.jpg
    ├── LICENSE
    ├── pinja
    │   ├── bin2asm
    │   │   └── bin2asm.py
    │   ├── color
    │   │   └── color.py
    │   ├── csvImprovement
    │   │   └── csv_improvement.py
    │   ├── getbin
    │   │   └── getbin.py
    │   ├── getfileinfo
    │   │   └── getfileinfo.py
    │   ├── __init__.py
    │   ├── main.py
    │   └── reference
    │       ├── AEP256_01.py
    │       └── use_doc2vec.py
    ├── README.md
    ├── requirements.txt
    └── setup.py 

--------

### Reference:

[click----https://pypi.org/project/click/](https://pypi.org/project/click/)

[capstone----https://www.capstone-engine.org/lang_python.html](https://www.capstone-engine.org/lang_python.html)

[glob----https://docs.python.org/3/library/glob.html](https://docs.python.org/3/library/glob.html)

[pefile----https://pypi.org/project/pefile/](https://pypi.org/project/pefile/)

[pefile-Howtouse----https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction)

[PEheader----https://blog.kowalczyk.info/articles/pefileformat.html](https://blog.kowalczyk.info/articles/pefileformat.html)

[elftools----https://github.com/eliben/pyelftools](https://github.com/eliben/pyelftools)

[elftools-user's-guide----https://github.com/eliben/pyelftools/wiki/User%27s-guide](https://github.com/eliben/pyelftools/wiki/User%27s-guide)

[elftools-example----https://www.programcreek.com/python/example/105189/elftools.elf.elffile.ELFFile](https://www.programcreek.com/python/example/105189/elftools.elf.elffile.ELFFile)

[ELF----https://unix.stackexchange.com/questions/418354/understanding-what-a-linux-binary-is-doing](https://unix.stackexchange.com/questions/418354/understanding-what-a-linux-binary-is-doing)

[ELF----https://gist.github.com/DhavalKapil/2243db1b732b211d0c16fd5d9140ab0b](https://gist.github.com/DhavalKapil/2243db1b732b211d0c16fd5d9140ab0b)

[Refer reversing tool blog----https://dev.to/icyphox/python-for-reverse-engineering-1-elf-binaries-1fo4](https://dev.to/icyphox/python-for-reverse-engineering-1-elf-binaries-1fo4)

[https://www.programcreek.com/python/example/50993/pefile.DIRECTORY_ENTRY](https://www.programcreek.com/python/example/50993/pefile.DIRECTORY_ENTRY)

[https://stackoverflow.com/questions/19325402/getting-iat-and-eat-from-pe](https://stackoverflow.com/questions/19325402/getting-iat-and-eat-from-pe)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
