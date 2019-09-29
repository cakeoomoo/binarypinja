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
        # print debug
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
        # print debug
        if 0:
            print_green("{0}".format(pe.OPTIONAL_HEADER))
            print_green("{0}".format(section))
            print_blue("{0}".format(entrypoint_raw))

    return entrypoint_raw


def get_elf_entrypoint(filepath):
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        # print debug
        if 0:
            print_green("{0}".format(elf.header))
            print_blue("{0}".format(elf.header.e_entry))
        entrypoint = elf.header.e_entry
    return entrypoint


def get_pe_ALLsymbol_address(filepath):
    debug1 = 0
    debug2 = 0
    debug3 = 0
    allsymbol = []
    with open(filepath, 'rb') as f:
        pe = pefile.PE(f.name)

        if debug1:
            print_green("{0}".format(pe.OPTIONAL_HEADER))
            print_blue("{0}".format(pe.OPTIONAL_HEADER.AddressOfEntryPoint))

            # print section name and some address
            for section in pe.sections:
                print_yelow("{}, {}, {}, {}".format(section.Name, hex(section.VirtualAddress), hex(section.Misc_VirtualSize), hex(section.SizeOfRawData) ))

            # If the PE file was loaded using the fast_load=True argument, we will need to parse the data directories:
            #pe.parse_data_directories()
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print_blue("{}".format(entry.dll))
                for imp in entry.imports:
                    print_purple("{}, {}".format(hex(imp.address), imp.name))

        if debug2:
            for exp in pe.DIRECTORY_ENTRY_EXPORT:
                print_green("{}, {}, {}".format(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal))
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print_yelow(entry.dll)
                for imp in entry.imports:
                      print_blue("{}, {}".format(hex(imp.address), imp.name))
            for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                print_green("{}, {}".format(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)
            print_blue("{}".format(pe.dump_info()))

        if debug3:
            for section in pe.sections:
                print_green("{}, {}, {}, {}, {}".format(
                    section.Name,
                    hex(section.VirtualAddress),
                    hex(section.Misc_VirtualSize),
                    section.SizeOfRawData,
                    section.get_entropy()))
                if section.Name == '.text':
                    print_red("{}, {}".format((section.PointerToRawData),hex(section.Misc_VirtualSize)))

        allsymbol.append([0, 0, 0])
    return allsymbol


def get_elf_ALLsymbol_address(filepath):
    debug = 0
    allsymbol = []
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')

        # store the symbol information into .text section(.sym is not ) of the file
        if debug:
            print_green(".text-address({0}): {1}, ".format(f.name, elf.get_section_by_name('.text')['sh_addr']))
        if symtab is not None:
            for element in symtab.iter_symbols():
                if debug:
                    print_red("ALL: {0}, ".format(dir(element.entry)))
                    print_purple_noLF("name: {0}, ".format(element.name))
                    print_blue_noLF("st_name: {0}".format(element.entry['st_name']))
                    print_green_noLF("address: {0}, ".format(hex(element.entry['st_value'])))
                    print_red("size {0},".format(hex(element.entry['st_size'])))
                if element.entry['st_size'] != 0:
                    allsymbol.append([element.name, element.entry['st_value'], element.entry['st_size']])
        else:
            print_blue("WARNING(no symbol) :  {0}".format(f.name))
            allsymbol.append([0, 0, 0])

        # dynsym
        dynsym = 0
        if dynsym:
            dynsym = elf.get_section_by_name('.dynsym')
            if dynsym is not None:
                for element in dynsym.iter_symbols():
                    # print debug
                    if debug:
                        print_red("ALL: {0}, ".format(dir(element.entry)))
                        print_purple_noLF("name: {0}, ".format(element.name))
                        print_blue_noLF("st_name: {0}".format(element.entry['st_name']))
                        print_green_noLF("address: {0}, ".format(hex(element.entry['st_value'])))
                        print_red("size {0},".format(hex(element.entry['st_size'])))
                    if element.entry['st_size'] != 0:
                        allsymbol.append([element.name, element.entry['st_value'], element.entry['st_size']])
            else:
                print_red("{0}: No symbol-info".format(f.name))
                allsymbol.append([0, 0, 0])

    return allsymbol


# Just Reference code, so this function do not use in main() of pinja 
def get_elf_ALLsymbol_address_otherinformation(filepath):
    debug = 0
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        for section in elf.iter_sections():
            symbol = [hex(section['sh_addr']), section.name]
            if debug:
                print_yelow("{0}".format(symbol))
                print_purple("{0}".format(f'{section.name}'))
                print(dir(section))

            if isinstance(section, StringTableSection):
                if debug:
                    print_red("{0}".format(f'{section.name}:'))
                symbol_table = elf.get_section(section['sh_link'])
            if isinstance(section, SymbolTableSection):
                if debug:
                    print_red("{0}".format(f'{section.name}:'))
                symbol_table = elf.get_section(section['sh_link'])
            if debug:
                print_red(dir(elf.get_section(section['sh_link']).name))
        print_green(elf.get_section_by_name('.text')['sh_addr'])
        print_green(elf.get_section_by_name('.text')['sh_name'])
