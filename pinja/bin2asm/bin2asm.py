#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
from capstone import *
import glob
import pefile
from pinja.color.color import *


def get_pe_textsection2asm(filepath):
    debug = 0
    list_i = []

    with open(filepath, 'rb') as f:
        pe = pefile.PE(f.name)

        if debug:
            print_blue("relative .text addr:{}, size:{}".format(hex(pe.sections[0].VirtualAddress), hex(pe.sections[0].SizeOfRawData)))

        textsection_addr = pe.sections[0].VirtualAddress
        textsection_size = pe.sections[0].SizeOfRawData

        code_section = pe.get_section_by_rva(textsection_addr)

        code_dump = code_section.get_data(textsection_addr, textsection_size)
        code_addr = pe.OPTIONAL_HEADER.ImageBase + code_section.VirtualAddress

        if debug:
            print_green(code_dump)

        md = Cs(CS_ARCH_X86, CS_MODE_64)
        countbyte = 0
        for i in md.disasm(code_dump, code_addr):
            current_inst = code_dump[countbyte:countbyte + i.size:]
            countbyte += i.size
            str_temp = i.mnemonic + ' ' + i.op_str
            list_i.append(str_temp)
    return list_i


def get_elf_textsection2asm(filepath, mode):
    debug = 0
    list_i = []
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        code = elf.get_section_by_name('.text')
        ops = code.data()
        addr = code['sh_addr']

        # check bit
        checkbit = elf.header.e_ident.EI_CLASS
        if checkbit == 'ELFCLASS32':
            md = Cs(CS_ARCH_X86, CS_MODE_32)
        elif checkbit == 'ELFCLASS64':
            md = Cs(CS_ARCH_X86, CS_MODE_64)
        else:
            print_red('ERROR: bit is wrong!')
            md = Cs(CS_ARCH_X86, CS_MODE_32)

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
            return [x for x in list_i if (x != '{') and (x != '}') and (x != '')]
        elif mode == "int":
            for i in md.disasm(ops, addr):
                current_inst = ops[countbyte:countbyte + i.size:]
                countbyte += i.size
                str_temp = i.mnemonic + ' ' + i.op_str
                list_i.append(str_temp)
        else:
            print_red("Error: mode is wrong!!")
    return list_i


'''----------------------------------------------------------------------------
   just reference as below
   ----------------------------------------------------------------------------
   Extruct the assembley-language from .text section of arbitry binary files
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

        # check bit
        checkbit = elf.header.e_ident.EI_CLASS
        if checkbit == 'ELFCLASS32':
            md = Cs(CS_ARCH_X86, CS_MODE_32)
        elif checkbit == 'ELFCLASS64':
            md = Cs(CS_ARCH_X86, CS_MODE_64)
        else:
            print_red('ERROR: bit is wrong!')
            md = Cs(CS_ARCH_X86, CS_MODE_32)

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
