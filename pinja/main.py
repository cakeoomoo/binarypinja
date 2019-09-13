#!/usr/bin/python3

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import glob

# local import 
from pinja.reference.AEP256_01 import *
from pinja.reference.use_doc2vec import *
from pinja.color.color import *
from pinja.getfileinfo.getfileinfo import *
from pinja.getbin.getbin import *




def getallfiles(input_dirpath):
    files = glob.glob(input_dirpath + '/*' )
    return files


@click.command()
@click.option('-m', '--mode', 'mode', default='bin',
        help='AEP256: get AEP(256byte)\ndoc2vec: run the doc2vec\nbin: binCode\nasm: asmCode\ndefault: bin')
@click.option('-f', '--fmt', 'format', default='pe',
                help='pe: PEformat\nelf: ELFformat\ndefault:pe')
@click.option('-o', '--out', 'output_dirpath', default='out',
                help='output directory path\ndefault:out')
@click.option('-b', '--byte', 'byte', default='256',
              help='byte: get number of byte\ndefault: 256')
@click.argument('input_dirpath', type=click.Path())
def main(input_dirpath, output_dirpath, format, mode, byte):
    """ Runs data processing scripts to turn assembler data from the binary into 
        cleaned data ready to be analyzed.
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    print_green('----start program----')
    
    '''
        special routine to refer
    '''
    if mode == 'AEP256':
        get_AEP256(input_dirpath, output_dirpath)
        return 
    if mode == 'doc2vec':
        get_elf_info('data/infileELF_1file/touch')
        return 

    '''
        basic routine
    '''
    # get files list
    files = getallfiles(input_dirpath)

    # get files entry point
    entry_pointlist = []
    if format == 'pe':
        for file in files:
            if os.path.isdir(file):
                continue
            entry_pointlist.append([file, get_pe_entrypoint(file)])
    elif format == 'elf':
        for file in files:
            if os.path.isdir(file):
                continue
            entry_pointlist.append([file, get_elf_entrypoint(file)])
    else:
        print_red('argument(mode) is wrong!')

    print_green(entry_pointlist)

    # get files all symbol
        #TODO

    # get binary code and make binaryfiles
        #TODO

    # get dissaasemble code and make the dataset(CSV)
        #TODO


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    main()
