################################
# 使い方
# >pyhton2 AEP256_01.py sample_folder
#
# Ubuntuで動作することを確認しています（Windowsは未確認）
# ライブラリ「pefile」をインストールしてください
# 引数はフォルダです、引数をファイル（exe）にすると動作しません（エラー処理もしていません）
# 処理するフォルダ内に、複数のフォルダが入っていても処理されます
# が、フォルダ階層が保持されません（処理したファイルの直前の階層のフォルダ名に分類されます）
#

################################
# pefileをインポート
import sys
import pefile
import os
import platform


#############################
# 総なめで処理する関数
def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


def get_AEP256(input_fpath, output_fpath):
    #####################################
    # 引数の処理（引数は、処理するフォルダ）
    path = ""
    exportpath = ""

    path = input_fpath
    exportpath = output_fpath

    if 0:
        if len(sys.argv) != 2:
            print("[!]Error\n")
            exit()
        else:
            path = sys.argv[1]
            exportpath = "export_" + sys.argv[1]

    if not os.path.exists(exportpath):
        os.mkdir(exportpath)
        print("[*]CREATE-DIR:" + exportpath)

    files = []

    splitter = ""

    count = 0
    dcount = 0
    ecount = 0
    ncount = 0
    acount = 0

    if platform.system() == "Windows":
        splitter = "\\"
    else:
        splitter = "/"

    if os.path.exists(exportpath) == False:
        os.mkdir(exportpath)

    #########################################
    # 引数で指定したフォルダ以下を処理
    for file in find_all_files(path):
        filename = file.split(splitter)

        ########################################
        # ファイル以外は処理しない（フォルダとか）
        if os.path.isdir(file):
            continue

        ########################################
        # 拡張子がDLLは処理しない（カウントする）
        if file[-4:] == ".dll":
            count += 1
            dcount += 1
            continue

        ########################################
        # 拡張子がEXEのみEPの位置を計算する
        if file[-4:] == ".exe":

            try:

                ###########################
                # PEヘッダ処理ここから
                pe = pefile.PE(file)
                flag = 0
                flaga = 0
                AEP = pe.OPTIONAL_HEADER.AddressOfEntryPoint

                ###########################
                # セクションごとにいろいろ求める
                for section in pe.sections:
                    secN = section.Name
                    secVA = section.VirtualAddress
                    secVS = section.Misc_VirtualSize
                    secSRD = section.SizeOfRawData
                    secPRD = section.PointerToRawData

                    #######################################
                    # 以下のifは特定のパッカー用（ここはなくてよい）
                    if AEP == 340:
                        flaga = 2
                        RAEP = AEP
                        break

                    elif AEP == 4120:
                        flaga = 3
                        RAEP = AEP - secVA
                        break

                    elif AEP == 4144:
                        flaga = 4
                        RAEP = 48
                        break

                    ###########################################################
                    # 一般のプログラム用（ここがメイン）
                    # PEヘッダ内のAEPを含むセクションに対してRawファイルでの位置を計算
                    if secVA <= AEP <= (secVA + secSRD):
                        RAEP = AEP - secVA + secPRD
                        flag = 1
                        break

                #################################
                # 検証用（PEヘッダの始まり位置確認）
                if flag == 1:
                    for i in range(0, 4096, 1):

                        offset = i
                        dlen = 2
                        findd = b'PE'
                        f = open(file, 'rb')
                        f.seek(offset)
                        data = f.read(dlen)
                        f.close()

                        if data == findd:
                            flaga = 5
                            break

                        if i == 4096:
                            flaga = 6
                            break

                    if i >= secPRD:
                        flaga = 7
                        RAEP = AEP - secVA

                ###############################
                # EPから抜き出すバイト数
                length = 256

                f = open(file, 'rb')
                f.seek(RAEP)
                data = f.read(length)
                f.close()

                ##################################
                # EPがファイルの末尾に近いため(length)バイト抜き出せない場合、\x00で残りを埋める
                if len(data) < length:
                    add = length - len(data)
                    data = data + (b'\x00' * add)
                    flag = 3

                #################################
                # 出力（抜き出したバイナリをファイル保存）に関する処理
                mkfolder = filename[-2]
                savefolder = exportpath + splitter + filename[-2]
                savepath = savefolder + splitter + filename[-1]

                if not os.path.exists(savefolder):
                    os.mkdir(savefolder)
                wf = open(savepath + ".bin", 'wb')
                wf.write(data)
                wf.close()
                count += 1
                ecount += 1

                ################################
                # ログに関する処理（python2用）
                print(count, ecount, dcount, ncount, acount),
                print(","),
                print(mkfolder + "," + filename[-1]),
                print(","),
                print(
                    flag,
                    flaga,
                    secN,
                    secVA,
                    AEP,
                    secVA +
                    secSRD,
                    secSRD,
                    RAEP,
                    len(data))

            except BaseException:
                count += 1
                ncount += 1
                continue

        else:
            count += 1
            acount += 1


if __name__ == '__main__':
    input_fpath = 'infile'
    output_fpath = 'outfile'
    get_AEP256(input_fpath, output_fpath)
