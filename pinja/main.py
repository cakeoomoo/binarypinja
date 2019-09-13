#!/usr/bin/python3

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import pinja.use_doc2vec
import pinja.AEP256_01
from pinja.color import *



@click.command()
@click.option('-f', '--fmt', 'format', default='pe',
              help='pe: PEformat elf: ELFformat   default:pe')
@click.option('-o', '--out', 'output_dirpath', default='out',
              help='output directory path default=out')
@click.option('-m', '--mode', 'mode', default='bin',
              help='bin: binaryCode, asm: assemblerCode   default: bin')
@click.option('-b', '--byte', 'byte', default='256',
              help='byte: get number of byte   default: 256')
@click.argument('input_dirpath', type=click.Path())
def main(input_dirpath, output_dirpath, format, mode, byte):
    """ Runs data processing scripts to turn assembler data from the binary into 
        cleaned data ready to be analyzed.
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    if format == 'pe' and mode == 'bin':
        pinja.AEP256_01.get_AEP256(input_dirpath, output_dirpath)
    elif format == 'pe' and mode == 'asm':
        pass
    elif format == 'elf' and mode == 'bin':
        pass
    elif format == 'elf' and mode == 'asm':
        pass
        #use_doc2vec.wrapper_get_elf_info(input_dirpath)
    else:
        print_red("error: argumetns is wrong!")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    main()
