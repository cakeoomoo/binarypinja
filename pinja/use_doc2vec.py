#!/usr/bin/python3

import pinja.bin2asm
from pinja.color import *
import glob
import re
from capstone import *
from elftools.elf.elffile import ELFFile
import os
from os import listdir
import pandas as pd
import numpy as np
import matplotlib as mp
from gensim import models
from os.path import isfile, join
from os.path import expanduser
path_HOME = expanduser("~")

sourcefiles_directory = path_HOME + "tool/pylib/doc2vec_testcode/"


def parse(_list):
    # strip lines and except { and }
    _list = [s.strip() for s in _list]
    _list = [i for i in _list if (i != '{') and (i != '}') and (i != '')]
    result_l = _list
    return result_l


def get_filelines(path_c, filename):
    debug = 1
    with open(path_c + '/' + filename, 'r') as f:
        if 0:
            # f.seek(1, 2)    # 1 colum, 2 row
            line = f.readlines()
            print("Read Line: %s" % (line))
        lines = f.readlines()
        lines = parse(lines)
    print_yelow(lines)
    return lines


def get_c_filelist(path_c):
    print_red('get_c_filelist()')
    files_c = [f for f in listdir(path_c) if isfile(join(path_c, f))]
    files_c = sorted(files_c, key=str.lower)
    if 0:
        for x in files_c:
            print_green(x)
            if 0:
                cmd = "echo test"
                os.system(cmd)
            lines = get_filelines(path_c, x)
    return files_c


def learnnning(sentences):

    if 1:
        model = models.Doc2Vec(
            sentences,
            dm=1,
            vector_size=300,
            window=5,
            alpha=.025,
            min_alpha=.025,
            min_count=0,
            sample=1e-6)
        print_red('\nlearnning start')
        epoch_num = 8
        for epoch in range(epoch_num):
            print('Epoch: {}'.format(epoch + 1))
            model.train(
                sentences,
                epochs=model.iter,
                total_examples=model.corpus_count)
            model.alpha -= (0.025 - 0.0001) / (epoch_num - 1)
            model.min_alpha = model.alpha
    if 0:
        model = models.Doc2Vec(
            sentences,
            dm=1,
            vector_size=300,
            window=15,
            alpha=.025,
            min_alpha=.025,
            min_count=1,
            sample=1e-6)
        print_red('\nlearnning start')
        epoch_num = 6
        for epoch in range(epoch_num):
            print('Epoch: {}'.format(epoch + 1))
            model.train(
                sentences,
                epochs=model.iter,
                total_examples=model.corpus_count)
            model.alpha -= (0.025 - 0.0001) / (epoch_num - 1)
            model.min_alpha = model.alpha
    if 0:
        model = models.Doc2Vec(
            documents=sentences,
            dm=1,
            vector_size=300,
            window=15,
            alpha=0.025,
            min_alpha=0.025,
            min_count=1)

    model.save("asm.doc2vec")


def search_loaded_model():
    model_loaded = models.Doc2Vec.load('asm.doc2vec')

    labelx = ''
    for x in range(12):
        labelx = x
        print_green(
            '{}-------------------------------------------------' .format(labelx))
        print(model_loaded.docvecs.most_similar([labelx]))

    if 0:
        print_green(
            'similarity-------------------------------------------------')
        print(model_loaded.docvecs.similarity("1", "7"))


'''
make csv fie by using pandas
'''


def save_file(filename, output_dir, listA):
    print_blue(listA)
    print_yelow(filename)

    df = pd.DataFrame(listA)
    df.to_csv(output_dir + "/OUT_" + filename + ".csv", sep=";")


'''
get elf header information
'''


def get_elf_info(filepath_name):
    print_green(filepath_name)
    with open(filepath_name, 'rb') as f:
        elf = ELFFile(f)
    print_green(elf)
    print_blue(vars(elf))
    print_green("{0}".format(elf.header))
    print_red('--')

    # set data of pandas
    df = pd.DataFrame(
        columns=[
            "malware",
            "VirtualAddress",
            "ResourceSize",
            "DebugSize",
            "IATSize"])

    # get file path
    PATH = path_HOME + u'/tool/pylib/doc2vec_testcode/bin_data/*'
    files = glob.glob(PATH)
    print_yelow(PATH)
    print_yelow(files)

    print_red('--')

    # extruct elf information from path's files for feature engieering
    for file in files:
        with open(file, 'rb') as f:
            data = ELFFile(f)
            if 0:
                print_green(data)
                print_blue(data._file_stringtable_section)
                print_purple(vars(data._file_stringtable_section))
                print_blue(data.structs)
            print_purple(vars(data.structs))
            print_blue(data.structs.Elf_addr)

            print_green(data.address_offsets(data, 0))

            #VA = data.VirtualAddress
            #RS = data.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size
            #DS = data.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
            #IATSize = data.OPTIONAL_HEADER.DATA_DIRECTORY[1].Size
            #newdf = pd.DataFrame([[0, VA, RS, DS, IATSize]], columns=["malware", "VirtualAddress", "ResourceSize", "DebugSize", "IATSize"])

            #df = df.append(newdf, ignore_index=True)


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


def wrapper_get_elf_info(dirpath):
    for file in find_all_files(dirpath):
        if os.path.isdir(file):
            continue
        print_green(file)
        get_elf_info(file)


'''
run doc2vec
argumetns:
    path_asm
        filepath
    learnnning_mode
        True: run
        False: not run
    compare_mode
        True: run
        False: not run
    splitmode
        arguments of byte2asm() function's mode --> 'int' or 'ope'
'''


def ctrl_file_lines(
        path_asm,
        learnnning_mode,
        compare_mode,
        save_mode,
        split_mode):
    eachlines = []
    str_temp = ''
    texts = []

    filelist = get_c_filelist(path_asm)
    for x in filelist:
        eachlines.append(bin2asm.byte2asm(path_asm + '/' + x, split_mode))

    # make list of doc2vec
    num = 0
    for i in filelist:
        print_green(i)
        str_temp = i
        texts.append(
            models.doc2vec.TaggedDocument(
                words=eachlines[num],
                tags=[str_temp]))
        num += 1

    # save csv files for each files
    if save_mode:
        num = 0
        for filename in filelist:
            save_file(filename, 'outputCSV', eachlines[num])
            num += 1

    if learnnning_mode:
        learnnning(texts)

    if compare_mode:
        search_loaded_model()


'''
The fuction emit binarycode which has optimization, cross architecture,
other compiler from c source code in this directorey.
'''


def make_compilestring(_fn, locate):
    obcuscated_clang_path = '/home/n/TOOL/build_ollvm/bin'
    obcuscated_clang = obcuscated_clang_path + '/clang'
    exec_folder = 'exec/'

    str1 = 'gcc' + ' -O3 ' + locate + _fn + '.c' + \
        ' -o ' + locate + exec_folder + 'gccO3_' + _fn
    str2 = 'gcc' + ' -O0 ' + locate + _fn + '.c' + \
        ' -o ' + locate + exec_folder + 'gccO0_' + _fn
    str3 = 'clang' + ' -O3 ' + locate + _fn + '.c' + \
        ' -o ' + locate + exec_folder + 'clangO3_' + _fn
    str4 = 'clang' + ' -O0 ' + locate + _fn + '.c' + \
        ' -o ' + locate + exec_folder + 'clangO0_' + _fn
    str5 = obcuscated_clang + ' -mllvm -fla ' + locate + _fn + '.c' + ' -o ' + \
        locate + exec_folder + 'clangfla_' + _fn  # control flow flattening
    str6 = obcuscated_clang + ' -mllvm -sub ' + locate + _fn + '.c' + ' -o ' + \
        locate + exec_folder + 'clangsub_' + _fn  # instruction substitution
    str7 = obcuscated_clang + ' -mllvm -bcf ' + locate + _fn + '.c' + \
        ' -o ' + locate + exec_folder + 'clangscf_' + _fn  # bogus control flow
    str8 = 'arm-linux-gnueabi-gcc' + ' -O3 ' + locate + _fn + \
        '.c' + ' -o ' + locate + exec_folder + 'armO3_' + _fn
    str9 = 'arm-linux-gnueabi-gcc' + ' -O0 ' + locate + _fn + \
        '.c' + ' -o ' + locate + exec_folder + 'armO0_' + _fn

    compile_strlist = [str1, str2, str3, str4, str5, str6, str7, str8, str9]

    return compile_strlist


def autocompile():
    print_green('autocompile()')

    filelocation = '/tool/pylib/doc2vec_testcode/testdata'

    # get c-source file list
    sourcefiles_dir = path_HOME + filelocation
    filelist = get_c_filelist(sourcefiles_dir)
    print_yelow(filelist)

    # extruct extension
    filelist_name = []
    for x in filelist:
        name, ext = os.path.splitext(x)
        filelist_name.append(name)
    print_yelow(filelist_name)

    # do compile for testdata/001test.c
    list_tmp = make_compilestring('001test', sourcefiles_dir + '/')
    for x in list_tmp:
        os.system(x)

    if 0:
        # make strings of compile command
        for x in filelist_name:
            list_tmp = make_compilestring(x, sourcefiles_dir + '/')
        print_green(list_tmp)
        # do compile of system command
        for x in list_tmp:
            os.system(x)


if __name__ == '__main__':

    get_elf_info(path_HOME + '/tool/pylib/doc2vec_testcode/bin_data/ls')

    if 0:
        # run doc2vec
        ctrl_file_lines(
            path_HOME +
            "/tool/pylib/doc2vec_testcode/bin_data",
            True,
            True,
            True,
            'ope')
    elif 0:
        # make bianry in testdata
        autocompile()
        list = ctrl_file_lines(
            path_HOME +
            "/tool/pylib/doc2vec_testcode/bin_data",
            False,
            False,
            True,
            'int')
    else:
        pass
