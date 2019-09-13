#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
from capstone import *
import glob
#from pinja.color import *
from color import *


def byte2asm(filepath, mode):
    debug = 0
    list_i = []
    with open(filepath, 'rb') as f:
        print_green(filepath)
        elf = ELFFile(f)
        code = elf.get_section_by_name('.text')
        ops = code.data()
        addr = code['sh_addr']
        md = Cs(CS_ARCH_X86, CS_MODE_64)

        countbyte = 0

        if mode == "ope":
            for i in md.disasm(ops, addr):
                current_inst = ops[countbyte:countbyte + i.size:]
                # print information
                if debug:
                    print_yelow('{} {}'.format(i.mnemonic, i.op_str))
                countbyte += i.size
                list_i.append(i.mnemonic)

                if debug:
                    # split all
                    parser_op = filter(
                        lambda w: len(w) > 0, re.split(
                            r'\s|"|,|\.', i.op_str))
                    list_i.extend(parser_op)
                else:
                    # non split
                    list_i.append(i.op_str)
        elif mode == "int":
            for i in md.disasm(ops, addr):
                current_inst = ops[countbyte:countbyte + i.size:]
                countbyte += i.size
                str_temp = i.mnemonic + ' ' + i.op_str
                list_i.append(str_temp)
        else:
            print_red("Error mode is wrong!! in byte2asm()...")

    return [x for x in list_i if (x != '{') and (x != '}') and (x != '')]


'''Extruct the assembley-language from .text section of arbitry binary files
   mode:
        "int" : opecode + operand,
        "ope" : opecode, operand
'''
def get256byte2asm(filepath, mode):
    debug = 0
    getByteNum = 256
    list_i = []

    with open(filepath, 'rb') as f:
        # get text segtion all data
        elf = ELFFile(f)
        code = elf.get_section_by_name('.text')
        ops = code.data()

        # get the start address of the text-section
        starttAddr_textSection = code['sh_addr']

        entrypointAdress = 0x3870

        startAddr = entrypointAdress - starttAddr_textSection

        endAddr = startAddr + getByteNum
        ops = ops[startAddr:endAddr]

        # entry point of touch(binary)
        addr_offset = starttAddr_textSection + 1000


        md = Cs(CS_ARCH_X86, CS_MODE_64)

        countbyte = 0
        if mode == "ope":
            for i in md.disasm(ops, startAddr):
                current_inst = ops[countbyte:countbyte + i.size:]
                # print information
                if debug:
                    print_yelow('{} {}'.format(i.mnemonic, i.op_str))
                countbyte += i.size
                list_i.append(i.mnemonic)

                if debug:
                    # split all
                    parser_op = filter(
                        lambda w: len(w) > 0, re.split(
                            r'\s|"|,|\.', i.op_str))
                    list_i.extend(parser_op)
                else:
                    # non split
                    list_i.append(i.op_str)
        elif mode == "int":
            for i in md.disasm(ops, startAddr):
                current_inst = ops[countbyte:countbyte + i.size:]
                countbyte += i.size
                str_temp = i.mnemonic + ' ' + i.op_str
                list_i.append(str_temp)
        else:
            print_red("Error mode is wrong!! in byte2asm()...")

    return [x for x in list_i if (x != '{') and (x != '}') and (x != '')]


def elf2asm(input_dir):
    mode = 'int'
    files = glob.glob(input_dir)
    print_green(files)
    for file in files:
        result001 = byte2asm(file, mode)

    print_blue("----------------------------")

    for file in files:
        result002 = get256byte2asm(file, mode)
    print_yelow(result002)


if __name__ == '__main__':
    elf2asm('infileELF_1file/*')
