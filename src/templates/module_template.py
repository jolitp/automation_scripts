#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

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

def main():
    """
    the main function for the script
    """
# region def main(...)


# endregion def main(...)


# region if __name__ == '__main__':
if __name__ == '__main__':
    print("module_template.py.__main__")
    print()
    function(" a string ",debug_function=True)
# endregion if __name__ == '__main__':
