import os
import random
import shutil


def rename_to_number(first, second):
    os.rename(first, second)


def randomize_directory(path):
    try:
        shutil.copytree('./res/textures', './textures')
    except:
        print('copying')

    newpath = './textures' + path

    x = 0
    files = []
    for i in os.listdir(newpath):
        if not i.__contains__('mcmeta'):
            files.append(i)

    for rename in files:
        rename_to_number(newpath + '/' + rename, newpath + '/' + str(x))
        x += 1

    files_tmp = files.copy()

    x = 0
    for rand in files:
        r = random.randint(0, len(files_tmp) - 1)
        os.rename(newpath + '/' + str(x), newpath + '/' + files_tmp[r])
        files_tmp.pop(r)

        x += 1


randomize_directory(
    '/assets/minecraft/textures/block'
)

randomize_directory(
    '/assets/minecraft/textures/item'
)