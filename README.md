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


    |  0                        |  1                           |  2             |  3             |  4                                |  5                                |  6
----|---------------------------|------------------------------|----------------|----------------|-----------------------------------|-----------------------------------|---------------------------------
0   |  infileELF/syslog_sample  |  __libc_csu_init             |  push r15      |  push r14      |  mov r15d, edi                    |  push r13                         |  push r12
1   |  infileELF/syslog_sample  |  _start                      |  xor ebp, ebp  |  mov r9, rdx   |  pop rsi                          |  mov rdx, rsp                     |  and rsp, 0xfffffffffffffff0
2   |  infileELF/syslog_sample  |  main                        |  push rbp      |  mov rbp, rsp  |  mov edx, 8                       |  mov esi, 3                       |  mov edi, 0x400678
3   |  infileELF/ptrace         |  my_command                  |  push rbp      |  mov rbp, rsp  |  sub rsp, 0xf0                    |  mov dword ptr [rbp - 0xe4], edi  |  mov rax, qword ptr fs:[0x28]
4   |  infileELF/ptrace         |  p_attach                    |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x20                    |  mov dword ptr [rbp - 0x14], edi  |  mov rax, qword ptr fs:[0x28]
5   |  infileELF/ptrace         |  convertNum_endian           |  push rbp      |  mov rbp, rsp  |  mov qword ptr [rbp - 0x18], rdi  |  mov qword ptr [rbp - 8], 0       |  mov rax, qword ptr [rbp - 0x18]
6   |  infileELF/ptrace         |  testcode_convertNum_endian  |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x10                    |  movabs rax, 0x1122334455667788   |  mov qword ptr [rbp - 8], rax
7   |  infileELF/ptrace         |  p_break                     |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x20                    |  mov dword ptr [rbp - 0x14], edi  |  mov qword ptr [rbp - 0x20], rsi
8   |  infileELF/ptrace         |  p_delete                    |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x100                   |  mov dword ptr [rbp - 0xe4], edi  |  mov qword ptr [rbp - 0xf0], rsi
9   |  infileELF/ptrace         |  p_continue                  |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x30                    |  mov dword ptr [rbp - 0x24], edi  |  mov rax, qword ptr fs:[0x28]
10  |  infileELF/ptrace         |  p_stepi                     |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x20                    |  mov dword ptr [rbp - 0x14], edi  |  mov rax, qword ptr fs:[0x28]
11  |  infileELF/ptrace         |  p_quit                      |  push rbp      |  mov rbp, rsp  |  sub rsp, 0x10                    |  mov dword ptr [rbp - 4], edi     |  mov eax, dword ptr [rbp - 4]
12  |  infileELF/ptrace         |  __stat                      |  mov rdx, rsi  |  mov rsi, rdi  |  mov edi, 1                       |  jmp 0x3ffef0                     |


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

##### Example Command:

```
pinja --help
pinja data/infilePE
pinja -f elf data/infileELF  -b 180 -o OUTPUTNAME 
```

##### DEMO:

![usage](https://github.com/cakeoomoo/binarypinja/blob/master/mics/usage_gif01.gif)


### Project Organization

------------
    

```bash
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
```

--------

### Reference

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
