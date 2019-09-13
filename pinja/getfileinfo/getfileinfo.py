#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
#from pefile import PE
import pefile

from pinja.color.color import *


'''
    TODO
'''
def get_pe_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        pe = pefile.PE(f.name)
        if 0:
            print_green("{0}".format(pe.OPTIONAL_HEADER))
            print_blue("{0}".format(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
        entrypoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    return entrypoint


def get_elf_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        if 0:
            print_green("{0}".format(elf.header))
            print_blue("{0}".format(elf.header.e_entry))
        entrypoint = elf.header.e_entry
    return entrypoint


def get_elf_ALLsymbol_address(filepath):
    pass


def get_pe_ALLsymbol_address(filepath):
    pass






