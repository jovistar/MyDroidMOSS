import zipfile
import os

class ApkBin():
    def __init__(self, apkFile, workingDir):
        self.apkFile = apkFile
        self.workingDir = workingDir
        self.zipFile = zipfile.ZipFile(self.apkFile)

    def unpack(self, unpackFile):
        '''
        Unpack
        '''
        if not os.path.isfile(self.apkFile):
            return 1
        if not os.path.isdir(self.workingDir):
            os.makedirs(self.workingDir)
        if os.path.isfile('%s/%s' % (self.workingDir, unpackFile)):
            os.remove('%s/%s' % (self.workingDir, unpackFile))

        try:
            data = self.zipFile.read(unpackFile)
            dstFile = open('%s/%s' % (self.workingDir, unpackFile), 'w')
            dstFile.write(data)
            dstFile.close()
            return 0
        except KeyError:
            return 2
