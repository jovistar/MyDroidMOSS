import os

def readLibs(file_path):
    file = open(file_path, "r")
    rst_list = list()
    for line in file.readlines():
        rst_list.append(line.rstrip())
    file.close()

    return rst_list

def filterLibs(root_path, libs):
    if root_path[-1:] != '/':
        root_path = root_path + '/'

    pack_list = list()
    packs = list()

    for root, dirs, files in os.walk(root_path):
        if len(files) == 0:
            continue

        flag = True

        for s in libs:
            subDir = root[len(root_path):]
            if subDir.startswith(s):
                flag = False
                break

        if flag == True:
            pack_list.append(root)

    return pack_list
