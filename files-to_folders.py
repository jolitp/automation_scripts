#! /usr/bin/env python3

import os


cwd = os.getcwd()

all_files = os.listdir(cwd)

only_files = []
for element in all_files:
    if os.path.isfile(element):
        only_files.append(element)

for file in only_files:
    name = os.path.splitext(file)[0]
    folder_path = cwd + "/" + name
    print("fodler path:")
    print(folder_path)

    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    source_path = cwd + "/" + file
    destination_path = folder_path + "/" + file
    print()
    print("source")
    print(source_path)

    print()
    print("destintation")
    print(destination_path)
    os.rename(source_path, destination_path)
