import os
import zipfile
import random

print('What is the path to your Minecraft folder?')
MINECRAFT_PATH = input()

MINECRAFT_VERSIONS_PATH = os.path.join(MINECRAFT_PATH, 'versions')
MINECRAFT_RESOURCE_PACKS_PATH = os.path.join(MINECRAFT_PATH, 'resourcepacks')

MC_MUDDLE_NAME = 'MCMuddle'
MC_MUDDLE_PATH = os.path.join(MINECRAFT_RESOURCE_PACKS_PATH, MC_MUDDLE_NAME)

minecraft_versions = []


def version_path_to_display_name(path):
    return path[path.rfind('/') + 1:]


def get_minecraft_versions():
    global minecraft_versions

    versions = [x[0] for x in os.walk(MINECRAFT_VERSIONS_PATH)]
    minecraft_versions = list(
        filter(lambda path: os.path.isfile(os.path.join(path, f'{version_path_to_display_name(path)}.jar')),
               versions[1:]))


def select_minecraft_version():
    print('Which version would you like to extract the textures from?')

    for i, v in enumerate(minecraft_versions):
        display = f'{i + 1}: {version_path_to_display_name(v)}'
        print(display)

    selected_version = int(input())
    return selected_version - 1


def get_textures(version_folder_path):
    jar_path = os.path.join(version_folder_path, f'{version_path_to_display_name(version_folder_path)}.jar')

    archive = zipfile.ZipFile(jar_path)

    for file in archive.namelist():
        if file.startswith('assets/minecraft/textures'):
            archive.extract(file, os.path.join(MC_MUDDLE_PATH))

    archive.close()

    mcmeta = open(os.path.join(MC_MUDDLE_PATH, 'pack.mcmeta'), 'w')
    mcmeta.write('{"pack":{"pack_format":1,"description":"Get ready for a cursed adventure"}}')
    mcmeta.close()


def randomize_textures(textures_path):
    x = 0
    files = []
    for i in os.listdir(textures_path):
        if not i.__contains__('mcmeta'):
            files.append(i)

    for rename in files:
        os.rename(os.path.join(textures_path, rename), os.path.join(textures_path, str(x)))
        x += 1

    files_tmp = files.copy()

    x = 0
    for _ in files:
        r = random.randint(0, len(files_tmp) - 1)
        os.rename(os.path.join(textures_path, str(x)), os.path.join(textures_path, files_tmp[r]))
        files_tmp.pop(r)

        x += 1


get_minecraft_versions()
selection = select_minecraft_version()
get_textures(minecraft_versions[selection])

# Randomizes the blocks
randomize_textures(os.path.join(MC_MUDDLE_PATH, 'assets/minecraft/textures/block'))
# Randomizes the items
randomize_textures(os.path.join(MC_MUDDLE_PATH, 'assets/minecraft/textures/item'))

print('Done! You can now open Minecraft in the selected version and select the resource pack in the options menu. '
      'Minecraft will tell you that the resource pack may be incompatible, but it will work perfectly fine.')
