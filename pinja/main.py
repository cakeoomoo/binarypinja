#!/usr/bin/python3

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import glob
import magic

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

    # get entry point
    entry_pointlist = []
    for file in files:
        if fmt == 'pe':
            entry_pointlist.append([file, get_pe_raw_entrypoint(file)])
        elif fmt == 'elf':
            entry_pointlist.append([file, get_elf_entrypoint(file)])
        else:
            print('Error! argv!!!')
    print_green(entry_pointlist)
    print_yelow('-------------------------------------------------------------')

    # get all symbol
    symbol_list = []
    for file in files:
        if fmt == 'pe':
            symbol_list.append([file, get_pe_ALLsymbol_address(file)])
        elif fmt == 'elf':
            symbol_list.append([file, get_elf_ALLsymbol_address(file)])
            #get_elf_ALLsymbol_address_otherinformation(file)
        else:
            print('Error! argv!!!')
    print_green(symbol_list)
    print_yelow('-------------------------------------------------------------')

    # get binary code and disassemble code
    asmcodelist = []
    asmcodelist.append([get_elf_binarycode(symbol_list)])
    print_green(binarycodelist)

    print_yelow('-------------------------------------------------------------')

    # make the dataset(CSV) from assemble code, binarycode and etc...
    df = pd.DataFrame(asmcodelist)
    df.to_csv("disassemble.csv")

    print_yelow('-------------------------------------------------------------')
    print_green('Finish!')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    main()
