#! /usr/bin/python3
"""
get all the videos in the directory and create files that contain the total length of them
"""
# import subprocess
# import pathlib
import shutil
import datetime
import os # used for getting the current working directory (cwd)
import importlib.util # needed for importing scripts using the scripts path

# from colorama import Fore
# from colorama import Style

DEBUG = False
DEBUG = True

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

script_path : str = python_scripts_folder_path +  "helpers/helpers/helpers.py"
spec = importlib.util.spec_from_file_location("module.name", script_path)
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)


# TODO pad zeroes before getting any data
# TODO make [acc_length] file
# TODO make [length] file
# TODO remove un needded files
# TODO put the video name and video length in the files in "csv" format with | as separator
# this way I may be able to adjust the columns in emacs
# don't use the .csv extension though
# TODO put functions in helper module

# cSpell: disable
def get_length(filename):
    """get hte length of the video using ffprobe command line utility

    Args:
        filename (str): name of the file

    Returns:
        float: the time of the video
    """
    # print(filename)
    # result = subprocess.run(["ffprobe ", "-v ", "error ", "-show_entries ",
    #                         "format=duration ", "-of ",
    #                         "default=noprint_wrappers=1:nokey=1 ", filename],

    command: str = "ffprobe \
                    -v error \
                    -show_entries \
                    format=duration \
                    -of default=noprint_wrappers=1:nokey=1 \
                        {0}" \
        .format(filename)
    stream = os.popen(command)
        # stdout=subprocess.PIPE,
        # stderr=subprocess.STDOUT)
    # final_result = str(result.stdout)
    result = stream.read()
    # if 'Header missing' in final_result:
    #     result.strout = b'0.0\n'
    #     final_result = '0.0\n'
    return float(result)

# # pretty print an array
# def pretty_print_array(array,message,color=Fore.GREEN):
#     """print an array with colors

#     Args:
#         array (list): list
#         message (str): message
#         color (Fore.color, optional): color. Defaults to Fore.GREEN.
#     """
#     if DEBUG :
#         print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
#     for local_index, name in enumerate(array):
#         start = f'{color}'
#         reset = f' : {Style.RESET_ALL}'
#         if DEBUG :
#             print(start + str(local_index) + reset + str(name))


# def pretty_print_value(value,message,color=Fore.BLUE):
#     """print an array with colors

#     Args:
#         value (any): value
#         message (str): message
#         color (Fore.color, optional): color. Defaults to Fore.GREEN.
#     """
#     if DEBUG :
#         print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))


DEBUT_FROM_SECONDS_TO_TIME = False
def from_seconds_to_time(sec, debug_function : bool = False):
    """
    converts time to human readable format

    Args:
        sec (int): time
    """
# region def from_seconds_to_time(...):
    time_in_string : str = str(datetime.timedelta(seconds=sec))
# region debug_function
    if debug_function:
        print("[def] sort_by_number_of_videos_and_size.main()")
        print("{")
        print()
# endregion
    # if DEBUT_FROM_SECONDS_TO_TIME:
    #     pretty_print_value(time_in_string, "from_seconds_to_time / time_in_string ")
    if 'day' in time_in_string:
        days = time_in_string.split(',')[0]
        days = int(days.split(' ')[0])
        # if DEBUT_FROM_SECONDS_TO_TIME:
        #     pretty_print_value(days , 'from_seconds_to_time / days',Fore.LIGHTBLUE_EX)

        rest = time_in_string.split(',')[1]
        # if DEBUT_FROM_SECONDS_TO_TIME:
        #     pretty_print_value(rest , 'from_seconds_to_time / rest',Fore.LIGHTBLUE_EX)

        hours = int(rest.split(':')[0])
        hours = hours + days * 24
        # if DEBUT_FROM_SECONDS_TO_TIME:
        #     pretty_print_value(hours , 'from_seconds_to_time / hours',Fore.LIGHTBLUE_EX)

        minutes = rest.split(':')[1]
        # if DEBUT_FROM_SECONDS_TO_TIME:
        #     pretty_print_value(minutes , 'from_seconds_to_time / minutes',Fore.LIGHTBLUE_EX)

        seconds = rest.split(':')[2]
        seconds = seconds.split('.')[0]
        # if DEBUT_FROM_SECONDS_TO_TIME:
        #     pretty_print_value(seconds , 'from_seconds_to_time / seconds',Fore.LIGHTBLUE_EX)
# cSpell: disable
        miliseconds = rest.split(':')[2]
        try:
            miliseconds = miliseconds.split('.')[1]
        except IndexError:
            miliseconds = 0
        # if DEBUT_FROM_SECONDS_TO_TIME:
        # pretty_print_value(miliseconds , 'from_seconds_to_time / miliseconds',Fore.LIGHTBLUE_EX)
# cSpell: enable
        time_in_string = str(hours) + ':' + minutes + ':' + seconds + "."

# region debug_function
    if debug_function:
        print()
        print("}")
# endregion
    return time_in_string
    ...
# endregion def from_seconds_to_time(...):


current_path = os.getcwd()

all_files_and_folders = os.listdir('.')
# print(all_files_and_folders)

all_videos = []
for file in all_files_and_folders:
    if helpers.is_video(file):
        all_videos.append(file)
all_videos.sort()
# print(all_videos)

# change names of all videos to names without special characters
for index, video in enumerate(all_videos):
    new_name = helpers.remove_special_characters(video)

    source = video
    # pretty_print_value(source, "source")
    destination = new_name
    # pretty_print_value(destination, "destination")
    shutil.move(str(source), str(destination))

    all_videos[index] = new_name


accumulated_time_file = open("accumulated_time_of_videos.txt" , "w+")
time_file = open("time_of_videos.txt" , "w+")

ACCUMULATED_TIME = 0
for video in all_videos:
    # pretty_print_value(video , "getting length for")
    length = get_length(video)
    # print('video : ' + str(video) + '\nlength : ' + str(length) + '\n')
    # pretty_print_value(str(video), 'video : ',color=Fore.GREEN)
    # pretty_print_value(str(length), 'Length : ',color=Fore.LIGHTGREEN_EX)

    time_formated = from_seconds_to_time(length)
    ACCUMULATED_TIME += length
    accumulated_time_formatted = from_seconds_to_time(ACCUMULATED_TIME)

    accumulated_time_file.write(video + " : " + str(accumulated_time_formatted) + "\n")
    time_file.write(video + " : " + str(time_formated) + "\n")

    formated = from_seconds_to_time(length)
    # print(video + '   ' + str(formated))
    # pretty_print_value(str(formated), 'Formated : ',color=Fore.YELLOW)

accumulated_time_file.close()
time_file.close()

TOTAL_LENGTH = str(from_seconds_to_time(ACCUMULATED_TIME))

NEW_FILE = str(current_path) + "/" + " [acc_length] " + str(from_seconds_to_time(ACCUMULATED_TIME))
f = open(NEW_FILE, "w+")
f.write(str(TOTAL_LENGTH))
f.close()

src = current_path
FILE_WITH_LENGTH = str(current_path) + "/" + "mark-video-length-finished.data"

f = open(FILE_WITH_LENGTH, "w+")
f.write(TOTAL_LENGTH)
f.close()




def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...):

# region debug_function
    if debug_function:
        print("[def] mark_video_length\n     .main()")
        print("{")
# endregion

    current_path = os.getcwd()
    all_files_and_folders = os.listdir(current_path)


# region debug_function
    if debug_function:
        print("}")
# endregion
    ...
# endregion def main(...):





# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    print("excecuting Mark_video_length.py")
    print()
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    main(
        debug_function = debug_script
        )
    ...
# endregion if __name__ == "__main__":
