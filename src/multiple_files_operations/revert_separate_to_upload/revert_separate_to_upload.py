#! /usr/bin/python3
"""
    separate the videos of a folder to be uploaded to youtube
"""
import os
import sys
import importlib.util # needed for importing scripts using the scripts path
# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/is_file_video/"
spec = importlib.util.spec_from_file_location("is_file_video",
    python_scripts_folder_path + subfolder + "is_file_video.py")
is_file_video_script = importlib.util.module_from_spec(spec)

spec.loader.exec_module(is_file_video_script)

def move_video(source : str, destination: str):
    """move one video

    Args:
        source (str): the source path
        destination (str): the destination path
    """
    os.rename(source,destination)


def get_all_folders_inside(directory_path: str, debug_function: bool = True):
    """
        get all folders inside a directory
    """
# region def get_all_folders_inside(...)
    # debug_function : bool = True  # comment to toggle
# region debug_function
    if debug_function:
        print()
        print("> [def] get_all_folders_inside(")
        print("                              )")
        print("{")
        print()
# endregion
    current_working_directory = os.getcwd()
    # cSpell: disable
    os.chdir(os.path.join(current_working_directory, directory_path))
    # cSpell: enable
    all_items : list = os.listdir(directory_path)
    for item in all_items:
        item = directory_path + "/" + item
# region debug_function
    if debug_function:
        print("> all_items = [")
        for debug_item in all_items:
            print("    {},".format(debug_item))
        print("> ]")
# endregion
    only_folders : list = []
    for index, item in enumerate(all_items):
# region debug_function
        if debug_function:
            print()
            print("> all_items[{}] = {}".format(index, item))
            print("> os.path.isdir(item) = {}".format(os.path.isdir(item)))
            print()
# endregion
        if os.path.isdir(item):
            only_folders.append(item)
# region debug_function
    if debug_function:
        print("> only_folders = [")
        for debug_item in only_folders:
            print("    {},".format(debug_item))
        print("> ]")
# endregion
# region debug_function
    if debug_function:
        print("}")
        print("# end of get_all_folders_inside()")
        print()
# endregion
    # cSpell: disable
    os.chdir(current_working_directory)
    # cSpell: enable
    return only_folders
    ...
# endregion def get_all_folders_inside(...)



def get_all_videos_inside(directory_path: str, debug_function: bool = True):
    """
        get all videos inside a directory
    """
# region def get_all_videos_inside(...)
    # debug_function : bool = True  # comment to toggle
# region debug_function
    if debug_function:
        print()
        print("> [def] get_all_folders_inside(")
        print("                              )")
        print("{")
        print()
# endregion
    # all_items : list = is_file_video_script.is_video()
    all_items : list = os.listdir(directory_path)
# region debug_function
    if debug_function:
        print("> all_items = [")
        for debug_item in all_items:
            print("    {},".format(debug_item))
        print("> ]")
# endregion
    only_videos : list = []
    for item in all_items:
        if is_file_video_script.is_video(item):
            only_videos.append(item)
# region debug_function
    if debug_function:
        print("> only_videos = [")
        for debug_item in only_videos:
            print("    {},".format(debug_item))
        print("> ]")
# endregion
# region debug_function
    if debug_function:
        print("}")
        print("# end of get_all_folders_inside()")
        print()
# endregion
    return only_videos
    ...
# endregion def get_all_folders_inside(...)



def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)
    # debug_function : bool = True  # comment to toggle
# region debug_function
    if debug_function:
        print()
        print("> [def] main(")
        print("            )")
        print("{")
        print()
# endregion
    current_directory : str = os.getcwd()
# region debug_function
    if debug_function:
        print()
        print("> current_directory = {}".format(current_directory))
        print()
# endregion
    only_folders = get_all_folders_inside(current_directory, \
                                            # debug_function=debug_function
                                            )
    only_upload_folders = []
    for folder in only_folders:
        if "[upload_" in folder:
            only_upload_folders.append(folder)
    uploaded_folder_name = "[_0_uploaded_0_]"
    uploaded_folder_path = current_directory + "/" + uploaded_folder_name
    only_folders_inside_uploaded_folder = \
        get_all_folders_inside(uploaded_folder_path, \
                                # debug_function=debug_function
                                )
    only_upload_folders_inside_uploaded_folder = []
    for folder in only_folders_inside_uploaded_folder:
        if "[upload_" in folder:
            only_upload_folders_inside_uploaded_folder.append(folder)
    videos_inside_folders = {}
    for folder in only_folders:
        videos_inside_folder : list = get_all_videos_inside(folder, \
                                                            # debug_function=debug_function
                                                            )
        videos_inside_folders[folder] = videos_inside_folder
    for folder in only_folders_inside_uploaded_folder:
        folder_path : str = uploaded_folder_name + "/" + folder
        videos_inside_folder : list = get_all_videos_inside(folder_path,\
                                                            # debug_function=debug_function
                                                            )
        videos_inside_folders[folder_path] = videos_inside_folder
# region debug_function
    if debug_function:
        print()
        print("> videos_inside_folders = [")
        for key, value in videos_inside_folders.items():
            print("    {} : {},"\
                .format(key, value))
        print("> ]")
        print()
# endregion

    list_of_paths_to_move : list = []
    for directory, list_of_videos in videos_inside_folders.items():
        for video in list_of_videos:
            path_to_video : str = current_directory + "/" + directory + "/" + video
# region debug_function
            if debug_function:
                print()
                print("> > path_to_video = {}".format(path_to_video))
                print()
# endregion
            list_of_paths_to_move.append(path_to_video)
# region debug_function
    if debug_function:
        print("> list_of_paths_to_move = [")
        for debug_item in list_of_paths_to_move:
            print("    {},".format(debug_item))
        print("> ]")
# endregion
    for video in list_of_paths_to_move:
        video_name : str = video.split("/")[-1]
        source = video
        destination = current_directory + "/" + video_name
# region debug_function
        if debug_function:
            print()
            print("> > video_name = {}".format(video_name))
            print("> > source = {}".format(source))
            print("> > destination = {}".format(destination))
            print()
# endregion
        move_video(source, destination)
        ...

# region debug_function
    if debug_function:
        print()
        print("}")
        print("# end of main()")
        print()
# endregion
    ...
# endregion def main(...)


# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    print("module_template.py.__main__")
    print()

    main(
        debug_function = debug_script
        )
    print("# end of module_template.py")
    ...
# endregion if __name__ == "__main__":
