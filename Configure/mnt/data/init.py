import os, sys, glob, zipfile

def unzip(zip_file_path, extract_to_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)

# def unzip(zip_file_path, extract_to_path):
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to_path, pwd=b'123456')

# def print_directory(path):
#     folder_structure = {}
#     for root, dirs, files in os.walk(path):
#         relative_path = os.path.relpath(root, path)
#         folder_structure[relative_path] = files
#     print(folder_structure)

data_path = '/mnt/data/'
# data_path = './'

unzip(data_path + 'orgparse.zip', data_path + 'orgparse/')
# unzip(data_path + 'orgparsezip', data_path + 'orgparse/')
# print_directory(data_path)

