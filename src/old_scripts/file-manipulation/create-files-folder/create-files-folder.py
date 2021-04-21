import os


def get_all_folders_in_dir(basepath):
  directories_array = []
  with os.scandir(basepath) as entries:
    for entry in entries:
      if entry.is_dir():
        directories_array.append(entry.name)
  return directories_array


cwd = os.getcwd()
all_dirs = get_all_folders_in_dir(cwd)
files_dir = cwd + '/files'

if not os.path.isdir(files_dir):
  os.mkdir(files_dir) 

for directory in all_dirs:
  new_folder = files_dir + '/' + str(directory)
  os.mkdir(new_folder)
  # print(new_folder)