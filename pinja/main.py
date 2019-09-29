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
    f = magic.Magic(mime=True, uncompress=True)
    if (f.from_file(filepath) != 'application/x-dosexec') and (f.from_file(filepath) != 'application/x-executable') and (f.from_file(filepath) != 'application/x-sharedlib'):
        if 0:
            print_red("{0} is not exec-file".format(filepath))
        return False
    return True


def get_outputnameOfCSV_fromDirectory(directorypath):
    return directorypath.replace('/', '_')


def make_CSVfile_from_datalist_withPandasFmt(filename, datalist):
    df = pd.DataFrame(datalist)
    df.to_csv(filename)
    print_green('----------------------------------------------')
    print_green('OUTPUT: {}!'.format(filename))
    print_green('----------------------------------------------')


@click.command()
@click.option(
    '-m',
    '--mode',
    'mode',
    default='bin',
    help='AEP256: get AEP(256byte)\ndoc2vec: run the doc2vec\nbin: binCode\nasm: asmCode\ndefault: bin')
@click.option('-f', '--fmt', 'fmt', default='pe',
              help='pe: PEformat\nelf: ELFformat\ndefault:pe')
@click.option('-o', '--out', 'output_dirpath', default='out',
              help='output directory path\ndefault:out')
@click.option('-b', '--byte', 'byte', default='256',
              help='byte: get number of byte\ndefault: 256')
@click.argument('input_dirpath', type=click.Path())
def main(input_dirpath, output_dirpath, fmt, mode, byte):
    """ Runs data processing scripts to turn assembler data from the binary into
        cleaned data ready to be analyzed.
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    debug = 0

    ''' special routine into reference folder
    '''
    if mode == 'AEP256':
        get_AEP256(input_dirpath, output_dirpath)
        return
    if mode == 'doc2vec':
        get_elf_info('data/infileELF_1file/touch')
        return

    ''' basic routine
    '''
    # get files
    files = getallfiles(input_dirpath)
    files = list(filter(checkfiletype, files))
    files = list(filter(os.path.isfile, files))
    print_yelow('-------------------------------------------------------------')

    # get outputfilename without file-extension
    outputfilename = get_outputnameOfCSV_fromDirectory(output_dirpath)

    # Extract entry-point for all files
    entry_pointlist = []
    for file in files:
        if fmt == 'pe':
            entry_pointlist.append([file, get_pe_raw_entrypoint(file)])
        elif fmt == 'elf':
            entry_pointlist.append([file, get_elf_entrypoint(file)])
        else:
            print('Error! argv!!!')
    print_green(entry_pointlist)
    # make the dataset(CSV) from entrypoint
    tempfilename =  outputfilename + "_EP.csv"
    make_CSVfile_from_datalist_withPandasFmt(tempfilename, entry_pointlist)
    print_yelow('-------------------------------------------------------------')




    # Extract disassembly code from text-section of all files
    # TODO




    # get all symbol
    symbol_list = []
    for file in files:
        if fmt == 'pe':
            symbol_list.append([file, get_pe_ALLsymbol_address(file)])
        elif fmt == 'elf':
            symbol_list.append([file, get_elf_ALLsymbol_address(file)])
            if debug:
                print_green(symbol_list)
        else:
            print('Error! argv!!!')
    print_yelow('-------------------------------------------------------------')

    # Extract disassembly code from all-function of all files
    if fmt == 'pe':
        # TODO
        pass
    elif fmt == 'elf':
        asmcodelist = []
        asmcodelist = get_elf_binarycode(symbol_list)
        if debug:
            pprint.pprint(asmcodelist)
        # make the dataset(CSV) from assemble code, binarycode and etc...
        tempfilename =  outputfilename + "_FUNC_asm.csv"
        make_CSVfile_from_datalist_withPandasFmt(tempfilename, asmcodelist)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    main()
