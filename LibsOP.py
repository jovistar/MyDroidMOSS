import os

def readLibs(file_path):
    file = open(file_path, "r")
    rst_list = list()
    for line in file.readlines():
        rst_list.append(line.rstrip())
    file.close()

    return rst_list
    
def filterLibs(root_path, libs):
    pack_list = list()
    packs = list()
    for dir in os.walk(root_path):
        if len(dir[2]) != 0:
            str = dir[0]
            str = str.replace("\\", "/")
            beg_index = str.index("/smali/")
            #str = str[beg_index+7:]
            #print "packages",str
            flag = True
            for s in libs:
                if str.startswith(s, beg_index +7):
                    flag = False
                    break
            if flag:
                pack_list.append(str)

    return pack_list        
