#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection
from elftools.elf.sections import StringTableSection
from elftools.elf.sections import SymbolTableSection
from elftools.elf.sections import *

import pefile

from pinja.color.color import *


def get_pe_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        pe = pefile.PE(f.name)
        if 0:
            print_green("{0}".format(pe.OPTIONAL_HEADER))
            print_blue("{0}".format(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
        entrypoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    return entrypoint


def get_pe_raw_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        pe = pefile.PE(f.name)
        entrypoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint

        try:
            section = next(
                s for s in pe.sections
                if 0 <= entrypoint - s.VirtualAddress <= s.SizeOfRawData)
        except StopIteration:
            raise Exception('No section contains entrypoint.')
        entrypoint_raw = (entrypoint
                          - section.VirtualAddress
                          + section.PointerToRawData)
        if 0:
            print_green("{0}".format(pe.OPTIONAL_HEADER))
            print_green("{0}".format(section))
            print_blue("{0}".format(entrypoint_raw))

    return entrypoint_raw


def get_elf_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        if 0:
            print_green("{0}".format(elf.header))
            print_blue("{0}".format(elf.header.e_entry))
        entrypoint = elf.header.e_entry
    return entrypoint


def get_pe_ALLsymbol_address(filepath):
    pass



def get_elf_ALLsymbol_address(filepath):
    print_yelow('--------------------------------')
    allsymbol = []
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)

        symtab = elf.get_section_by_name('.symtab')

        for element in symtab.iter_symbols():
            if 0:
                print_red("ALL: {0}, ".format(dir(element.entry)))
            print_purple_noLF("nama is {0}, ".format(element.name))
            #print_blue_noLF("st_name is {0}".format(element.entry['st_name']))
            print_green_noLF("address is {0}, ".format(element.entry['st_value']))
            print_red("size is {0},".format(element.entry['st_size']))




        #-----------------------------------------------------------------
        # test
        #-----------------------------------------------------------------
        print_green(elf.get_section_by_name('.text')['sh_addr'])
        print_green(elf.get_section_by_name('.text')['sh_name'])
        if 0:
            for section in elf.iter_sections():
                symbol = [hex(section['sh_addr']), section.name]
                if 0:
                    print_yelow("{0}".format(symbol))
                    print_purple("{0}".format(f'{section.name}'))
                    print(dir(section))
                if 0:
                    if isinstance(section, StringTableSection):
                        print_red("{0}".format(f'{section.name}:'))
                        symbol_table = elf.get_section(section['sh_link'])

                    if isinstance(section, SymbolTableSection):
                        print_red("{0}".format(f'{section.name}:'))
                        symbol_table = elf.get_section(section['sh_link'])
                print_red(dir(elf.get_section(section['sh_link']).name))
                test = elf.get_section_by_name('.text')['sh_addr']
                print(elf.get_section_by_name('.text')['sh_addr'])
            print_green(elf.get_section_by_name('.text')['sh_addr'])
            print_green(elf.get_section_by_name('.text')['sh_name'])


    return allsymbol

