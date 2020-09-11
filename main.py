import os
import random


def rename_to_number(first, second):
    os.rename(first, second)


def randomize_directory(path):
    x = 0
    files = []
    for i in os.listdir(path):
        if not i.__contains__('mcmeta'):
            files.append(i)

    for rename in files:
        rename_to_number(path + '/' + rename, path + '/' + str(x))
        x += 1

    files_tmp = files.copy()

    x = 0
    for rand in files:
        r = random.randint(0, len(files_tmp) - 1)
        os.rename(path + '/' + str(x), path + '/' + files_tmp[r])
        files_tmp.pop(r)

        x += 1


randomize_directory(
    './textures/assets/minecraft/textures/block'
)

randomize_directory(
    './textures/assets/minecraft/textures/item'
)