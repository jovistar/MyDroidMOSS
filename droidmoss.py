import sys
import getopt
import os

import LibsOP
import Utils
import Sim
from fp_generator import Fp_Generator

from apkbin import ApkBin
from apksmali import ApkSmali

def load_apk_files(importDir):
    apkFiles = []

    dirWalk = os.walk(importDir)

    for root, dirs, files in dirWalk:
        for oneFile in files:
            if oneFile[-4:] == '.apk':
                apkFiles.append(root + '/' + oneFile)

    return apkFiles

def print_apk_files(apkFiles):
    for apkFile in apkFiles:
        print apkFile

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'd:w:r:o:')

    importDir = ''
    windowSize = 2
    resetPointValue = 173
    outputFile = ''

    for opt, arg in opts:
        if opt in ('-d'):
            importDir = arg
        if opt in ('-w'):
            windowSize = int(arg)
        if opt in ('-r'):
            resetPointValue = int(arg)
        if opt in ('-o'):
            outputFile = arg

    adLibs = LibsOP.readLibs('./adlibs.dat')
    opCodes = Utils.getDALVIKOPCodes('./opcodes.dat')
    fpGenerator = Fp_Generator(windowSize, resetPointValue)

    apkFiles = load_apk_files(importDir)
    print_apk_files(apkFiles)

    apkResults = {}

    for apkFile in apkFiles:
        apkBin = ApkBin(apkFile, './tmp')
        if apkBin.unpack('classes.dex') != 0:
            print apkFile + ' is not valid apk file!'
            continue

        apkSmali = ApkSmali('classes.dex', './tmp')
        if apkSmali.convert() != 0:
            print apkFile + ' has no valid classes.dex!'
            continue

        apkPacks = LibsOP.filterLibs('./tmp/smali/', adLibs)

        apkSeqs = Utils.getSeqFromSmaliDir(apkPacks, opCodes)

        seq = ''
        for apkSeq in apkSeqs:
            seq = seq + apkSeq

        print seq

        apkFp = fpGenerator.do_generate(seq)
        apkResults[apkFile] = apkFp

        print apkFile + ':\n'
        print apkFp

    doOut = False
    if outputFile != '':
        doOut = True
        fileHandle = open(outputFile, 'w')

    resultCache = []
    for srcFile in apkResults:
        for dstFile in apkResults:
            if srcFile == dstFile:
                continue

            if [srcFile, dstFile] in resultCache:
                continue

            resultCache.append([dstFile, srcFile])
            simScore = Sim.SimScore(apkResults[srcFile], apkResults[dstFile])

            print srcFile + '    ' + dstFile + '    ' + '%d' % simScore
            if doOut == True:
                fileHandle.write(srcFile + '    ' + dstFile + '    ' + '%d' % simScore)

    if doOut == True:
        fileHandle.close()
