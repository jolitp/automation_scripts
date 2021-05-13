#! /usr/bin/python3
import pathlib
# from pathlib import Path
import os
# import shutil
# import sys
# import re
import importlib.util
import inspect
import tokenize
from varname import nameof
# from glob import glob
# from colorama import Fore
# from colorama import Style


"""
https://stackoverflow.com/questions/39172306/can-a-line-of-python-code-know-its-indentation-nesting-level
"""
def get_indentation_level():
    """ get indentation level of the place where it is called in the script
        Parameters:
            None
        Returns:
            indentation_level (int): the indentation level
    """
    caller_frame = inspect.currentframe().f_back
    filename, caller_lineno, _, _, _ = inspect.getframeinfo(caller_frame)
    with open(filename) as f_n:
        indentation_level = 0
        for token_record in tokenize.generate_tokens(f_n.readline):
            token_type, _, (token_lineno, _), _, _ = token_record
            if token_lineno > caller_lineno:
                break
            elif token_type == tokenize.INDENT:
                indentation_level += 1
            elif token_type == tokenize.DEDENT:
                indentation_level -= 1
        return indentation_level


spec = importlib.util.spec_from_file_location("logic_log",
    "/home/jolitp/Dropbox/PROJECTS/python-scripts/helpers/org_log/org_log.py")
org_log = importlib.util.module_from_spec(spec)

spec.loader.exec_module(org_log)
org_logger = org_log.OrgLogger(cwd = os.getcwd(), script_name = os.path.basename(__file__))

DEBUG = False
DEBUG = True                                                                   # comment to toggle

folders_to_delete = [
    "videos",
    "converted"
]

current_path = pathlib.Path(__file__).parent.absolute()

# region org logger add variable
org_logger.add_variable(current_path,
                        nameof(current_path),
                        get_indentation_level())
# endregion

HAS_FILES_COMPRESSED = False
# region org logger add variable
org_logger.add_variable(HAS_FILES_COMPRESSED,
                        nameof(HAS_FILES_COMPRESSED),
                        get_indentation_level())
# endregion

dir_and_files = os.walk(".", topdown=False)

# region org logger add for (begin)
org_logger.add_for_statement(dir_and_files,
                            nameof(dir_and_files),
                            get_indentation_level(),
                            begin_or_end='begin')
# endregion
for root, dirs, files in os.walk(".", topdown=False):

    # region org logger add line
    org_logger.add_line(get_indentation_level() * "*" + " start of loop")
    # endregion

    # region org logger add variable
    org_logger.add_blank_line()
    org_logger.add_variable(root,
                        nameof(root),
                        get_indentation_level())
    # endregion

    # region org logger add variable
    org_logger.add_variable(dirs,
                        nameof(dirs),
                        get_indentation_level())
    # endregion

    # region org logger add variable
    org_logger.add_variable(files,
                        nameof(files),
                        get_indentation_level())
    # endregion

    # region org logger add for (begin)
    org_logger.add_for_statement(files,
                                nameof(files),
                                get_indentation_level(),
                                begin_or_end='begin')
    # endregion

    for file in files:

        # region org logger add variable
        org_logger.add_variable(file,
                                nameof(file),
                                get_indentation_level())
        # endregion

        compressed_files_found : bool = 'files.7z' in file or 'files.zip' in file

        # region org logger add if (begin)
        org_logger.add_if_statement(compressed_files_found,
                            nameof(compressed_files_found),
                            get_indentation_level(),
                            begin_or_end='begin')
        # endregion

        if compressed_files_found:
            HAS_FILES_COMPRESSED = True

            # region org logger add variable
            org_logger.add_variable(HAS_FILES_COMPRESSED,
                                    nameof(HAS_FILES_COMPRESSED),
                                    get_indentation_level())
            # endregion

        # region org logger add if (end)
        org_logger.add_if_statement(compressed_files_found,
                            nameof(compressed_files_found),
                            get_indentation_level(),
                            begin_or_end='end')
        # endregion

        video_file_found : bool = '.mp4' in file or '.mkv' in file

        # region org logger add if (begin)
        org_logger.add_if_statement(video_file_found,
                            nameof(video_file_found),
                            get_indentation_level(),
                            begin_or_end='begin')
        # endregion

        if video_file_found:

            video_path = os.path.join(root, file)

            # region org logger add variable
            org_logger.add_variable(video_path,
                                    nameof(video_path),
                                    get_indentation_level())
            # endregion

            # region org logger add line
            org_logger.add_line(get_indentation_level() * "*" + " [#A] removes file: video_path")
            # endregion

            # try:
            #     os.remove(video_path)
            # except OSError as exception:
            #     print("Error: %s : %s" % (video_path, exception.strerror))

        # region org logger add if (end)
        org_logger.add_if_statement(video_file_found,
                            nameof(video_file_found),
                            get_indentation_level(),
                            begin_or_end='end')
        # endregion

    # region org logger add for (end)
    org_logger.add_for_statement(files,
                                nameof(files),
                                get_indentation_level(),
                                begin_or_end='end')
    # endregion

    # region org logger add for (begin)
    org_logger.add_for_statement(dirs,
                                nameof(dirs),
                                get_indentation_level(),
                                begin_or_end='begin')
    # endregion

    for dir in dirs:

        # region org logger add variable
        org_logger.add_variable(dir,
                                nameof(dir),
                                get_indentation_level())
        # endregion

        can_remove_files_folder : bool = HAS_FILES_COMPRESSED and "files" in dir

        # region org logger add if (begin)
        org_logger.add_if_statement(can_remove_files_folder,
                            nameof(can_remove_files_folder),
                            get_indentation_level(),
                            begin_or_end='begin')
        # endregion

# TODO is the name of the directory in the the name of the videos in the root folder?
        if can_remove_files_folder:
            command : str = "rm -rf " + os.path.join(root, dir)

            # region org logger add variable
            org_logger.add_variable(command,
                                    nameof(command),
                                    get_indentation_level())
            # endregion

            # print(command)

        # region org logger add if (end)
        org_logger.add_if_statement(can_remove_files_folder,
                            nameof(can_remove_files_folder),
                            get_indentation_level(),
                            begin_or_end='end')
        # endregion

        # region org logger add for (begin)
        org_logger.add_for_statement(folders_to_delete,
                                    nameof(folders_to_delete),
                                    get_indentation_level(),
                                    begin_or_end='begin')
        # endregion

        for folder in folders_to_delete:
            # region org logger add variable
            org_logger.add_variable(folder,
                                    nameof(folder),
                                    get_indentation_level())
            # endregion

            is_folder_in_dir : bool = folder in dir
            # region org logger add if (end)
            org_logger.add_if_statement(is_folder_in_dir,
                                nameof(is_folder_in_dir),
                                get_indentation_level(),
                                begin_or_end='end')
            # endregion

            if is_folder_in_dir:

                full_path = os.path.join(root, dir)
                # os.system(r"rm -rf {} ")

                ...
            # region org logger add if (end)
            org_logger.add_if_statement(is_folder_in_dir,
                                nameof(is_folder_in_dir),
                                get_indentation_level(),
                                begin_or_end='end')
            # endregion

            ...

        # region org logger add for (begin)
        org_logger.add_for_statement(folders_to_delete,
                                    nameof(folders_to_delete),
                                    get_indentation_level(),
                                    begin_or_end='end')
        # endregion

        ...
    # region org logger add for (end)
    org_logger.add_for_statement(dirs,
                                nameof(dirs),
                                get_indentation_level(),
                                begin_or_end='end')
    # endregion

    ...
# region org logger add for (end)
org_logger.add_for_statement(dir_and_files,
                            nameof(dir_and_files),
                            get_indentation_level(),
                            begin_or_end='end')
# endregion



# region org logger print table of dictionary
org_logger.table_of_a_dictionary(sections,
                            nameof(sections),
                            get_indentation_level())
# endregion



