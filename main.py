# This is a sample Python script.
import glob
import os.path
import shutil


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


import glob


def get_stl_3mf_files_deep(folder_path):
    search_pattern = os.path.join(folder_path, '**', '*.stl')
    stl_files = glob.glob(search_pattern, recursive=True)

    search_pattern = os.path.join(folder_path, '**', '*.3mf')
    mf_files = glob.glob(search_pattern, recursive=True)

    stl_3mf_files = stl_files + mf_files
    return stl_3mf_files


def get_stl_3mf_files_shallow(folder_path):
    search_pattern = os.path.join(folder_path, '*.stl')
    stl_files = glob.glob(search_pattern, recursive=True)

    print(f"{len(stl_files)} stl files found.")

    search_pattern = os.path.join(folder_path, '*.3mf')
    mf_files = glob.glob(search_pattern, recursive=True)
    print(f"{len(mf_files)} 3mf files found.")

    stl_3mf_files = stl_files + mf_files
    return stl_3mf_files


def get_folders_list(folder_path):
    folders_list = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return folders_list


def folder_containst_models(folder):
    models = get_stl_3mf_files_deep(folder)
    if len(models) > 0:
        return True
    else:
        return False


def move_file(source_file, destination_folder):
    try:
        shutil.move(source_file, destination_folder)
        print(f"File '{source_file}' moved to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


def move_folder(source_folder, destination_folder):
    try:
        shutil.move(source_folder, destination_folder)
        print(f"Folder '{source_folder}' moved to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


# Press the green button in the gutter to run the script.
def move_shallow_files(root, dst):
    stl_3mf_files_list_shallow = get_stl_3mf_files_shallow(root)
    print(f"{len(stl_3mf_files_list_shallow)} models found in shallow search.")

    for file in stl_3mf_files_list_shallow:
        move_file(file, dst)
        print(f"moved {file}")

if __name__ == '__main__':
    root = '/Users/vishnusivadasan/Downloads'
    dst = os.path.join(root, "ModelDirectory")
    os.makedirs(dst, exist_ok=True)
    move_shallow_files(root, dst)

    folders_list = get_folders_list(root)
    folders_list = [i for i in folders_list if os.path.abspath(dst) != os.path.abspath(i)]
    folders_list = [i for i in folders_list if folder_containst_models(i)]

    for folder in folders_list:
        move_folder(folder, dst)
        print(f"{folder} moved.")
