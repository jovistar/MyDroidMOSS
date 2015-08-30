import os
import shutil
import subprocess

class ApkSmali():
    def __init__(self, srcFile, workingDir):
        self.srcFile = srcFile
        self.workingDir = workingDir
        self.smaliDir = workingDir + '/smali'
        self.toolsDir = 'tools'

    def convert(self):
        dexFile = self.workingDir + '/' + self.srcFile
        dstDir = self.smaliDir

        if not os.path.isfile(dexFile):
            return 1

        if os.path.isdir(dstDir):
            os.system('rm -rf %s' % dstDir)

        #os.system('java -jar %s/baksmali.jar -o %s %s' % (self.toolsDir, dstDir, dexFile))
        sub = subprocess.Popen('java -jar %s/baksmali.jar -o %s %s' % (self.toolsDir, dstDir, dexFile), shell = True)
        sub.wait()

        if not os.path.isdir(dstDir):
            return 2

        return 0
