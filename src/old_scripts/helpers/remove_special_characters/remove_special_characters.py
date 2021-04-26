#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""


def remove_special_characters(string : str, debug_function : bool = False):
    """ removes special characters from a given string, so it does not break in the command line

    exceptions: some special characters are not removed

    . = not removed because it can mess up file types

    Args:
        path (str): the original string

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.

    Returns:
        str: the string without the special characters
    """
# region def remove_special_characters(string):

# region debug_function
    if debug_function:
        print("[def] filter_videos(")
        print("> string : {0} = {1}".format(type(string), str(string)))
        print("              )")
        print("{")
# endregion
    new : str = str(string).replace('\'', "")
    new = new.replace('\"', "")
    new = new.replace('\'', "")
    new = new.replace('\\', "")
    new = new.replace('|', "")
    new = new.replace('(', '')
    new = new.replace(')', '')
    new = new.replace('~', '')
    new = new.replace('`', '')
    new = new.replace('#', '')
    new = new.replace('@', '')
    new = new.replace('!', '')
    new = new.replace('$', '')
    new = new.replace('%', '')
    new = new.replace('^', '')
    new = new.replace('&', '')
    new = new.replace('*', '')
    new = new.replace('[', '')
    new = new.replace(']', '')
    new = new.replace('{', '')
    new = new.replace('}', '')
    new = new.replace(';', '')
    new = new.replace(':', '')
    new = new.replace('<', '')
    new = new.replace('>', '')
    new = new.replace('?', '')
# region debug_function
    if debug_function:
        print("> new : {0} = {1}".format(type(new), str(new)))
        print("}")
# endregion
    return new
# endregion def remove_special_characters(string):



if __name__ == '__main__':
    print("remove_special_characters.py.__main__")
