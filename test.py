import LibsOP
import Utils

#libs = list()
#packs = list()
#opcodes_list = list()

libs = LibsOP.readLibs("D:/libs.txt")
packs = LibsOP.filterLibs("D:/root/7723.cn_3Dzq.apk/smali", libs)
opcodes_list = Utils.getDALVIKOPCodes("D:/dalvik_opcodes.txt")
seq = Utils.getSeqFromSmaliDir(packs, opcodes_list)

#print len(seq)

#record = open("D:/lxy.txt","w+")
#for s in seq:
#    record.write(s)
#    record.write("\n")
#record.close()
