#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/get_video_length/"
spec = importlib.util.spec_from_file_location("get_video_length",
    python_scripts_folder_path + subfolder + "get_video_length.py")
get_video_length_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_video_length_script)

def function(parameter : str,
    debug_function : bool = False):
    """
        docstring for function

    Args:
        root_directory (str):

    Returns:
        str:
    """
# region def function(...)

# region debug_function
    if debug_function:
        print("[def] function(")
        print("      parameter : str = {1}"\
            .format(str(parameter)))
        print("              )")
        print("{")
# endregion



# region debug_function
    if debug_function:
        print("}")
# endregion


    return
# endregion def function(...)

def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)


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
    ...
# endregion if __name__ == "__main__":
