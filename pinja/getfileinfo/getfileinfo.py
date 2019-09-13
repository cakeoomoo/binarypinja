#!/usr/bin/python3

from elftools.elf.elffile import ELFFile

from pinja.color.color import *


'''
    TODO
'''
def get_elf_entrypoint(filepath):
    with open(filepath_name, 'rb') as f:
        elf = ELFFile(f)

    print_green("{0}".format(elf.header))


    entrypoint = 0x40000000
    return entrypoint

def get_pe_entrypoint(filepath):
    pass


def get_elf_ALLsymbol_address(filepath):
    pass


def get_pe_ALLsymbol_address(filepath):
    pass






