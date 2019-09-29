#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import *
from capstone import *
from pinja.color.color import *
import pprint
import numpy as np
import pandas as pd

def get_pe_binarycode(file):
    pass
    # TODO

def get_elf_binarycode(symbollist):
    # initialize variable and list
    inst_allFunc = []
    inst_allFile = []
    debug = 0
    shreshold_size = 4

    # split two lists from symbollist
    filename_list, sym_addr_list = map(list, zip(*symbollist))

    # get disassemble code of all function of .text section on elf binary files.
    for (filename, list_syminfo) in zip(filename_list,sym_addr_list):
        with open(filename, 'rb') as f:
            if debug:
                print_red(filename)
            elf = ELFFile(f)
            code = elf.get_section_by_name('.text')
            ops = code.data()
            starttAddr_textSection = code['sh_addr']
            l_temp = []
            for name, addr, size in list_syminfo:
                l_file_func_inst = []
                # skip no symbol
                if name is 0:
                    continue
                # skip short size of the code
                if size <= shreshold_size:
                    continue
                staAddr = addr - starttAddr_textSection
                endAddr = addr - starttAddr_textSection + size
                ops_temp = ops[staAddr:endAddr]
                if debug:
                    print("name:{},  addr:{},  size:{}".format(name, addr, size))
                    print("start: {}, end:{}".format(hex(staAddr), hex(endAddr)))
                list_i = []
                md = Cs(CS_ARCH_X86, CS_MODE_64)
                countb = 0
                for i in md.disasm(ops_temp, starttAddr_textSection):
                    current_inst = ops_temp[countb:countb + i.size:]
                    countb += i.size
                    str_temp = i.mnemonic + ' ' + i.op_str
                    list_i.append(str_temp)
                l_file_func_inst = [filename,name]
                l_file_func_inst.extend(list_i)
                l_temp.append(l_file_func_inst)
            inst_allFunc.extend(l_temp)
    return inst_allFunc

