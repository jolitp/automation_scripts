#! /usr/bin/python3
import os
import shutil
import warnings

import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/is_file_video/"
script_name : str = "is_file_video.py"
full_script_path : str = python_scripts_folder_path + subfolder + script_name
# print("Loading module from path : {}".format(full_script_path))
module_name : str = "is_file_video_script"
# print("module name : {}".format(module_name))
spec = importlib.util.spec_from_file_location(module_name, full_script_path)
is_file_video_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_file_video_script)

# print("as {}".format(is_file_video_script))
# print()

def prettify_path(path: str):
    """pretty print a path

    Args:
        path (str): the path
    """
    dirs = path.split("/")
    separator = "/"
    tab = "-"
    number_of_tabs = 0

    final_string : str = ""
    for directory in dirs:
        final_string \
          += "|" + tab * number_of_tabs \
          + separator \
          + directory + "\n"
        number_of_tabs += 1
        ...
    return final_string
    ...

current_dir_path = os.getcwd()
# # region debug
# print()
# print("current_dir_path : {}".format(current_dir_path))
# print()
# # endregion debug
current_dir = os.path.basename(current_dir_path)
# # region debug
# print()
# print("current_dir : {}".format(current_dir))
# print()
# # endregion debug
all_files_full_path = []
# # region debug
# print("FOR START")
# print("for root, directories, filenames in os.walk(current_dir_path):")
# print()
# # endregion debug
for root, directories, filenames in os.walk(current_dir_path):
# # region debug
#     print("> ITERATION START")
#     print("> root: {}".format(root))
#     print("> directories: {}".format(directories))
#     print("> filenames : {}".format(filenames ))
#     print()
# # endregion debug
# # region debug
#     print("> FOR START")
#     print("> for filename in filenames:")
#     print()
# # endregion debug
    for filename in filenames:
        all_files_full_path.append(os.path.join(root,filename))

# # region debug
# print()
# print("all_files_full_path : {}".format(all_files_full_path ))
# print()
# for debug_index, debug_item in enumerate(all_files_full_path):
#     print("all_files_full_path[{0}] : {1}"\
#       .format(debug_index, debug_item))
#     print()
# print()
# # endregion debug

all_videos = []
for file_path in all_files_full_path:
    if is_file_video_script.is_video(file_path):
    # if is_video(file_path):
        all_videos.append(file_path)

all_files = {}

for file_path in all_videos:
    all_files[file_path] = {
        'file_name' : os.path.basename(file_path),
        'folders' : (current_dir + os.path.dirname(file_path))
                    .replace(current_dir_path,'')
                    .replace('/', '...'),
        'folder_path': os.path.dirname(file_path) + "/"
    }

all_videos_with_new_name = []
for path in all_files:
    folder_path = all_files[path]['folder_path']
    folder_path = current_dir_path
    nested_folders = all_files[path]['folders'] + '...'
    file_name = all_files[path]['file_name']
    new_name = \
      folder_path + "/" + \
      nested_folders + \
      file_name
    print()
    print("folder_path : ")
    print(prettify_path(folder_path))
    print()
    print("nested folders : ")
    print(prettify_path(nested_folders))
    print()
    print("file name: ")
    print(prettify_path(file_name))
    print()
    print("new name: ")
    print(prettify_path(new_name))
    print()
    os.rename(path, new_name)
    all_videos_with_new_name.append(new_name)

# BUG when the files are at root the first letter vanishes
# # region debug
# print()
# print("all_videos_with_new_name")
# print()
# print(all_videos_with_new_name)
# print()
# for video in all_videos_with_new_name:
#     print(prettify_path(video))
#     print()
# # endregion debug

# TODO make the name shrink if the video get more than 100 characters

for video in all_videos_with_new_name:
    if len(video) > 100:
        warnings.warn("video: \n{0} \nhas more than 100 characters" \
          .format(video))
# what i want to do

# given a root folder (can be the folder the script is in (will need to copy the script each time))
# get every video with a video extension "*.mp4"
# and change the name to the root directory + other directory + filename.ext
