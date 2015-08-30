import os


def getSeqFromSmaliDir(packs_list, opcodes_list):
    seq = list()
    for pack_path in packs_list:
        for file in os.listdir(pack_path):
            file_path = os.path.join(pack_path,file)
            if os.path.isfile(file_path):
                getOPCodes(file_path, opcodes_list, seq)
    return seq

def getDALVIKOPCodes(dalvik_file_path):
    opcodes_list = list()
    file = open(dalvik_file_path, "r")
    for line in file.readlines():
        opcodes_list.append(line.strip())

    file.close()
    return opcodes_list


def getOPCodes(file_path, opcodes_list, seq):
    #print file_path
    file = open(file_path, "r")
    for line in file.readlines():

        if not len(line) or line.isspace():
            continue
        #print line
        s = getOPCodeFromLine(line)
        if s in opcodes_list:
           # print s
            seq.append(s)
            #print len(seq)
    file.close()
    return

def getOPCodeFromLine(s):
    s = s.strip()
    if s.find(" ") != -1:
        end_index = s.index(" ")
        s = s[0:end_index]
    return s

