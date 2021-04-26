#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""
import os.path


def get_absolute_path_before_moving_to_directory(root_directory : str,
                                        destination_directory : str,
                                        file_or_folder_to_move : str,
                                        debug_function : bool = False):
    """
        get the absolute path of a file or directory after it WOULD be moved to a directory
        in the root directory. Doesn't actually move the file or directory.

    Args:
        root_directory (str): the directory containing the file or folder to move,
            should be an absolute path

        destination_directory (str): the destination directory to move,
            should be a relative path

        file_or_folder_to_move (str): the file or folder to move,
            should be a relative path

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.

    Returns:
        str: the path to the file or folder in the destination directory
    """
# region def get_absolute_path_before_moving_to_directory(...)
# region debug_function
    if debug_function:
        print("[def] get_absolute_path_before_moving_to_directory(")
        print("      root_directory : {0} = {1}"\
            .format(type(root_directory), str(root_directory)))
        print("      file_or_folder_to_move : {0} = {1}"\
            .format(type(file_or_folder_to_move), str(file_or_folder_to_move)))
        print("      destination_directory : {0} = {1}"\
            .format(type(destination_directory), str(destination_directory)))
        print("                                                 )")
        print("{")
# endregion
    # region if not os.path.isabs(root_directory):
    if not os.path.isabs(root_directory):
# region debug_function
        if debug_function:
            print("> [if] not os.path.isabs(root_directory): {0}"
                    .format(os.path.isabs(root_directory)))
            print("> > [raise] ValueError")
# endregion
        raise ValueError("root_directory is not absolute path")
    # endregion if not os.path.isabs(root_directory):
    # region if os.path.isabs(file_or_folder_to_move):
    if os.path.isabs(file_or_folder_to_move):
# region debug_function
        if debug_function:
            print("> [if] not os.path.isabs(file_or_folder_to_move): {0}"
                    .format(os.path.isabs(file_or_folder_to_move)))
            print("> > [raise] ValueError")
# endregion
        raise ValueError("file_or_folder_to_move is absolute path")
    # endregion if os.path.isabs(file_or_folder_to_move):
    # region if os.path.isabs(destination_directory):
    if os.path.isabs(destination_directory):
        message : str = "destination_directory is absolute path"
# region debug_function
        if debug_function:
            print("> [if] not os.path.isabs(destination_directory): {0}"
                    .format(os.path.isabs(destination_directory)))
            print("> > [raise] ValueError")
            print("> >  message: {0}".format(message))
# endregion
        raise ValueError(message)
    # endregion if os.path.isabs(destination_directory):
    path : str = "{0}/{1}/{2}".format(root_directory, destination_directory, file_or_folder_to_move)
    dot_dot_slash_index : int = path.find("../")
    dot_dot_slash_found : bool = dot_dot_slash_index != -1
# region debug_function
    if debug_function:
        print("> path : {0} = {1}"\
            .format(type(path), str(path)))
        print("> dot_dot_slash_index : {0} = {1}"\
            .format(type(dot_dot_slash_index), str(dot_dot_slash_index)))
        print("> dot_dot_slash_found : {0} = {1}"\
            .format(type(dot_dot_slash_found), str(dot_dot_slash_found)))
        print("> [if] dot_dot_slash_index != -1: {0}".format(dot_dot_slash_found))
# endregion
    # region if dot_dot_slash_found:
    if dot_dot_slash_found:
        message : str = "found ../ in result path, that is not supported"
        raise ValueError(message)
    # endregion if dot_dot_slash_found:
    double_slashes : int = path.find("//")
    # region while double_slashes != -1:
    while double_slashes != -1:
# region debug_function
        if debug_function:
            print()
            print("> [while] double_slashes != -1: {0}".format(double_slashes != -1))
            print()
            print("> double_slashes : int = path.find(\"//\")")
            print("> double_slashes - 1 : {0} = {1} path[double_slashes] {2} = {3}" \
                .format(type(double_slashes),
                        str(double_slashes - 1),
                        type(path[double_slashes -1]),
                        path[double_slashes - 1],
                        ))
            print("> double_slashes : {0} = {1} path[double_slashes] {2} = {3}" \
                .format(type(double_slashes),
                        str(double_slashes),
                        type(path[double_slashes]),
                        path[double_slashes],
                        ))
            print("> double_slashes + 1 : {0} = {1} path[double_slashes] {2} = {3}" \
                .format(type(double_slashes),
                        str(double_slashes + 1),
                        type(path[double_slashes + 1]),
                        path[double_slashes + 1],
                        ))
            print("> double_slashes + 2 : {0} = {1} path[double_slashes] {2} = {3}" \
                .format(type(double_slashes),
                        str(double_slashes + 2),
                        type(path[double_slashes + 2]),
                        path[double_slashes + 2],
                        ))
            print()
            print("> > path (before) : {0} = {1}" \
                .format(type(path), str(path)))
# endregion
        path = path[:double_slashes] + path[double_slashes+1:]
# region debug_function
        if debug_function:
            print("> > path (after) : {0} = {1}" \
                .format(type(path), str(path)))
# endregion
        double_slashes : int = path.find("//")
    # endregion while double_slashes != -1:
    last_character : str = path[len(path) - 1]
# region debug_function
    if debug_function:
        print("> last_character : {0} = {1}" \
            .format(type(last_character), str(last_character)))
# endregion
    # region if "/" in last_character:
    if "/" in last_character:
        path = path[:-1]
    # endregion if "/" in last_character:
# region debug_function
        if debug_function:
            print("> [if] \"/\" in last_character: {0}".format("/" in last_character))
            print("> > path : {0} = {1}" \
                .format(type(path), str(path)))
# endregion
# region debug_function
    if debug_function:
        print("}")
# endregion
    return path
# endregion def get_absolute_path_before_moving_to_directory(...)


if __name__ == '__main__':
    print("get_absolute_path_before_moving_to_directory.py.__main__")
