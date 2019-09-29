#!/usr/bin/python3

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import glob
import magic
import pprint

# local import
from pinja.reference.AEP256_01 import *
from pinja.reference.use_doc2vec import *
from pinja.color.color import *
from pinja.getfileinfo.getfileinfo import *
from pinja.getbin.getbin import *


def getallfiles(input_dirpath):
    files = glob.glob(input_dirpath + '/*')
    return files


def checkfiletype(filepath):
    # check filetype
    debug = 0
    f = magic.Magic(mime=True, uncompress=True)
    if (f.from_file(filepath) != 'application/x-dosexec') and (f.from_file(filepath) != 'application/x-executable') and (f.from_file(filepath) != 'application/x-sharedlib'):
        if debug:
            print_red("{0} is not exec-file".format(filepath))
        return False
    return True


def get_outputnameOfCSV_fromDirectory(directorypath):
    return directorypath.replace('/', '_')


def make_CSVfile_from_datalist_withPandasFmt(filename, datalist):
    df = pd.DataFrame(datalist)
    df.to_csv(filename)
    print_green('OUTPUT >>>>>>>>  {} '.format(filename))


def check32or64_elf(filepath):
    debug = 0
    with open(filepath, 'rb') as f:
        elf = ELFFile(f)
        checkbit = elf.header.e_ident.EI_CLASS
    if debug:
        print_red("{}: bit is {}".format(filepath, checkbit))
    if checkbit == 'ELFCLASS32':
        return 32
    elif checkbit == 'ELFCLASS64':
        return 64


@click.command()
#@click.option('-m', '--mode', 'mode', default='bin', help='other: \ndefault: bin')
@click.option('-f', '--fmt', 'fmt', default='pe',
              help='pe: PEformat\nelf: ELFformat\ndefault:pe')
@click.option('-o', '--out', 'output_dirpath', default='out',
              help='output directory path\ndefault:out')
@click.option('-b', '--byte', 'byte', default='256',
              help='byte: get number of byte\ndefault: 256')
@click.argument('input_dirpath', type=click.Path())
def main(input_dirpath, output_dirpath, fmt, byte):
    """ Runs data processing scripts to turn assembler data from the binary into
        cleaned data ready to be analyzed.
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    print_green('----------------pinja START!----------------')
    debug = 0

    # get files
    files = getallfiles(input_dirpath)
    files = list(filter(checkfiletype, files))
    files = list(filter(os.path.isfile, files))

    for file in files:
        check32or64_elf(file)


    # get outputfilename without file-extension
    outputfilename = get_outputnameOfCSV_fromDirectory(output_dirpath)

    ''' ------------------------------------------------------------------------
        Extract entry-point for all files
        [dirpathname]_EP.csv
        ------------------------------------------------------------------------
    '''
    entrypoint_list = []
    for file in files:
        if fmt == 'pe':
            entrypoint_list.append([file, get_pe_raw_entrypoint(file)])
        elif fmt == 'elf':
            entrypoint_list.append([file, get_elf_entrypoint(file)])
        else:
            print('Error: argv')
            return 0
    if debug:
        print_green(entrypoint_list)
    # make the dataset(CSV)
    tempfilename =  outputfilename + "_EP.csv"
    make_CSVfile_from_datalist_withPandasFmt(tempfilename, entrypoint_list)

    ''' ------------------------------------------------------------------------
        Extract disassembly code from entry-point of all files at arbitrary bytes
        [dirpathname]_EP_asm.csv
        ------------------------------------------------------------------------
    '''
    anyBytefromEp_list = []
    for file in files:
        if fmt == 'pe':
            anyBytefromEp_templist = [file]
            anyBytefromEp_templist.extend(get_pe_binarycode(file, byte))
            anyBytefromEp_list.append(anyBytefromEp_templist)
        elif fmt == 'elf':
            anyBytefromEp_templist = [file]
            anyBytefromEp_templist.extend(get_elf_binarycode(file, byte))
            anyBytefromEp_list.append(anyBytefromEp_templist)
        else:
            return 0
    if debug:
        pprint.pprint(anyBytefromEp_list)
    # make the dataset(CSV)
    tempfilename =  outputfilename + "_EP_asm.csv"
    make_CSVfile_from_datalist_withPandasFmt(tempfilename, anyBytefromEp_list)

    ''' ------------------------------------------------------------------------
        Extract disassembly code from text-section of all files
        [dirpathname]_TEXTSec_asm.csv
        ------------------------------------------------------------------------
    '''
    textsegment_list = []
    for file in files:
        if fmt == 'pe':
            textsegment_templist = [file]
            textsegment_templist.extend(get_pe_textsection2asm(file))
            textsegment_list.append(textsegment_templist)
            if 0:
                pprint.pprint(textsegment_list)
        elif fmt == 'elf':
            textsegment_templist = [file]
            textsegment_templist.extend(get_elf_textsection2asm(file, 'int'))
            textsegment_list.append(textsegment_templist)
            if debug:
                pprint.pprint(textsegment_list)
        else:
            print_red('ERROR: your arguments is worng')
    # make the dataset(CSV) from assemble code, binarycode and etc...
    tempfilename =  outputfilename + "_TEXTSec_asm.csv"
    make_CSVfile_from_datalist_withPandasFmt(tempfilename, textsegment_list)

    ''' ------------------------------------------------------------------------
        Extract disassembly code from all-function of all files
        [dirpathname]_FUNC_asm.csv
        ------------------------------------------------------------------------
    '''
    symbol_list = []
    # get all symbol
    for file in files:
        if fmt == 'pe':
            symbol_list.append([file, get_pe_ALLsymbol_address(file)])
            if debug:
                print_green(symbol_list)
        elif fmt == 'elf':
            symbol_list.append([file, get_elf_ALLsymbol_address(file)])
            if debug:
                print_green(symbol_list)
        else:
            return 0
    if fmt == 'pe':
        asmcodelist = []
        asmcodelist = get_pe_function_binarycode(symbol_list)
    elif fmt == 'elf':
        asmcodelist = []
        asmcodelist = get_elf_function_binarycode(symbol_list)
        if debug:
            pprint.pprint(asmcodelist)
        # make the dataset(CSV) from assemble code, binarycode and etc...
        tempfilename =  outputfilename + "_FUNC_asm.csv"
        make_CSVfile_from_datalist_withPandasFmt(tempfilename, asmcodelist)

    ''' ------------------------------------------------------------------------
        Transform disassembly code from csvfile by arbitrary rules
        [dirpathname]_FUNC_asm_repl.csv
        ------------------------------------------------------------------------
    '''
    # TODO

    print_green('----------------pinja FINISH!----------------')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    main()
