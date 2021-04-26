#! /usr/bin/python3.8
"""
convert, resize and concatenate all videos in a directory
"""
# import pathlib
import os
import sys
import json
import shutil
import subprocess
# import re
# import collections
import importlib.util
from colorama import Fore
from colorama import Style

# TODO create a file in the directory with the size of videos
# TODO create a file in the directory with the size of converted videos
# TODO create a file in the directory with the size of concatenated video

# TODO create a file in the directory with wether or not the concatenated video and converted ...
# TODO ... videos are the same size


# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

spec = importlib.util.spec_from_file_location("remove_special_characters.name",
                                        python_scripts_folder_path + \
                            "helpers/remove_special_characters/remove_special_characters.py")
remove_special_characters_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(remove_special_characters_script)


spec = importlib.util.spec_from_file_location("remove_special_characters.name",
                                        python_scripts_folder_path + \
                            "helpers/filter_videos/filter_videos.py")
filter_videos_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filter_videos_script)



spec = importlib.util.spec_from_file_location("remove_special_characters.name",
                                        python_scripts_folder_path + \
"helpers/get_absolute_path_before_moving_to_directory/" + \
    "get_absolute_path_before_moving_to_directory.py")
get_absolute_path_before_moving_to_directory_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_absolute_path_before_moving_to_directory_script)


spec = importlib.util.spec_from_file_location("remove_special_characters.name",
                                        python_scripts_folder_path + \
                                        "helpers/filter_videos/" + "filter_videos.py")
filter_videos_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filter_videos_script)



DEBUG = False
DEBUG = True


# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    """pretty print array

    Args:
        array ([type]): [description]
        message ([type]): [description]
        color ([type], optional): [description]. Defaults to Fore.GREEN.
    """
    if DEBUG :
        print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG :
            print(start + str(index) + reset + str(name))


def pretty_print_value(value_in_function,message,color=Fore.BLUE):
    """[summary]

    Args:
        value ([type]): [description]
        message ([type]): [description]
        color ([type], optional): [description]. Defaults to Fore.BLUE.
    """
    if DEBUG :
        print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value_in_function))


def make_video_list_file(root_dir, videos_path_list):
    # cSpell:disable
    """create a file for ffmpeg to use as a list of videos

    Args:
        videos_path_list (list(str)): the list with all the path to the videos
    """
    # cSpell:enable
    video_list_file = open('video_list.txt', 'w+')
    video_list_file.close()

    video_list_file = open('video_list.txt', 'a')
    for video_path in videos_path_list:
        video_path_2 = os.path.splitext(video_path)[0] + '.mp4'
        path = root_dir + video_path_2
        video_list_file.write(f"file \'{path}\'\n")
    video_list_file.close()
    return 'video_list.txt'


def add_to_histogram(key_in_function, histogram):
    """[summary]

    Args:
        key ([type]): [description]
        histogram ([type]): [description]
    """
    if key_in_function in histogram:
        histogram[key_in_function] = int(histogram[key_in_function]) + 1
    else:
        histogram[key_in_function] = 1

# current_directory_path = ""

# TODO make the script choose if the concatenation is in one file or on multiple parts
def main():
    """
    the main function for the script
    """

    concatenated_video_found = False

    current_directory_path = os.getcwd()

    current_directory_name = os.path.basename(current_directory_path)

    source = current_directory_path
    destination = remove_special_characters_script.remove_special_characters(source)

    if source != destination:
        shutil.move(source, destination)
        current_directory_path = destination
    all_files_and_folders = os.listdir(current_directory_path)

    all_videos = []
    all_videos = filter_videos_script.filter_videos(all_files_and_folders)

    videos_folder_path = str(current_directory_path) + '/videos/'
    has_videos_folder = os.path.isdir(videos_folder_path)
    # print(isDirectory)

    if not has_videos_folder:
        os.mkdir(videos_folder_path)

    # move videos to videos folder

    for video in all_videos:
        concatenated_video_name : str = str(current_directory_name + ".mp4")
        if video == concatenated_video_name:
            print("concatenated video found : {0}".format(concatenated_video_name))
            sys.exit()
            ...
        source = str(current_directory_path) + '/' + str(video)
        destination = get_absolute_path_before_moving_to_directory_script \
            .get_absolute_path_before_moving_to_directory_script(current_directory_path,
                                                                        "videos",
                                                                        video)
        print("> source: \n{0}\n\n> destination: \n{1}".format(source, destination))
        shutil.move(source, destination)                                      # deactivate to test
        ...

    all_files_and_folders_in_videos_folder = os.listdir('./videos/')
    all_videos_in_videos_folder : list = []

    all_videos = filter_videos_script.filter_videos(all_files_and_folders_in_videos_folder)

    width_and_height_occurrences = []

    histogram_video_width = {}
    histogram_video_height = {}

    # check wether or not the videos have the same dimensions and save on the 'histograms'
    for video in all_videos:
        if video == str(current_directory_name + ".mp4"):
            concatenated_video_found = True
            continue
        path_to_video = videos_folder_path + '/' + video
        # print(path_to_video)
        result = subprocess.run([
                                "mediainfo",
                                '--Inform=\"Video;%Height%\"',
                                '--Output=JSON',
                                path_to_video],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                check=True)
        parsed = json.loads(result.stdout)

        try:
            video_category = parsed["media"]["track"][1]
            video_width = video_category["Width"]
            video_height = video_category["Height"]
        except IndexError as error:
            video_width = 0
            video_height = 0
    # if the video don't have the information it means it is corrupted
    # TODO move the video to the broken folder and delete from the array, don't even add 0:0
    # as width or height

            print()
            print(error)
            print()
            print(subprocess.PIPE)
            print()
        add_to_histogram(video_width, histogram_video_width)
        add_to_histogram(video_height, histogram_video_height)

        width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))

    print("width_and_height_occurrences : ")
    for item in width_and_height_occurrences:
        print("item : {0}".format(item))
    # pretty_print_array(width_and_height_occurrences, "width_and_height_occurrences", Fore.YELLOW)

    # get the most common dimensions
    width_and_height_count = {}
    for element in width_and_height_occurrences:
        if element in width_and_height_count:
            width_and_height_count[element] += 1
        else:
            width_and_height_count[element] = 1

    width_and_height_count_array = []
    for key, value in width_and_height_count.items():
        temp = [value,key]
        width_and_height_count_array.append(temp)

    # pretty_print_array(width_and_height_count, "width_and_height_count", Fore.YELLOW)

    # pretty_print_value(width_and_height_count, "width_and_height_count")

    # pretty_print_array(width_and_height_count_array, "width_and_height_count_array", Fore.YELLOW)

# most_common_width_and_height = width_and_height_count_array[len(width_and_height_count_array) -1]
    # pretty_print_value(most_common_width_and_height, "most_common_width_and_height")

    # BUG the most common width and height is not the most common
    # most_common_width_and_height = re.findall('\'([^"]*)\'', str(most_common_width_and_height))
    # most_common_width_and_height : str = most_common_width_and_height[0]
    # most_common_width_and_height = most_common_width_and_height.replace('\'','')


    # pretty_print_value(most_common_width_and_height, "most_common_width_and_height")
    # print(type(most_common_width_and_height))


    current_directory_path = ""
    converted_directory_path = str(current_directory_path) + '/converted'

    if not os.path.isdir(converted_directory_path):
        os.mkdir(converted_directory_path)

    # convert the videos
    for video in all_videos_in_videos_folder:
        output_video = converted_directory_path + '/' + video

        if os.path.isfile(output_video):
            continue
        output_video = os.path.splitext(output_video)[0] + '.mp4'
        path_to_video_in_videos_folder = str(current_directory_path) + '/videos/' + video
        # print(f'{Fore.GREEN}video : {Style.RESET_ALL}' + str(path_to_video_in_videos_folder))
        most_common_width_and_height = 0
        # cSpell:disable

        flag_framerate = " -r 30 "
        flag_video_config = " -c:v libx264 -pix_fmt yuv420p -crf 17 "
        flag_audio_config = " -c:a aac -b:a 128k "
        flag_youtube_config = " -movflags +faststart "
        flag_scale_config = " -vf scale={0} ".format(most_common_width_and_height)

        flags = flag_framerate + \
            flag_video_config + \
            flag_audio_config + \
            flag_youtube_config + \
            flag_scale_config
        command = "ffmpeg -i \"{0}\" \\\n {1} \\\n \"{2}\"" \
            .format(path_to_video_in_videos_folder, flags, output_video)
        # cSpell:enable
        # print(f'{Fore.GREEN}command : {Style.RESET_ALL}' + command)

        print("> os.system(command) : {0}".format(command))
        print()
        os.system(command)                                                       # comment to test

    # if not (len(histogram_video_height) == 1 and len(histogram_video_width) == 1):
    #     print(f'{Fore.RED}videos have different dimensions{Style.RESET_ALL}')
    #     make_different_dimensions_file()
    #     # sys.exit()



    # concatenate videos

    # if DEBUG :
    #     print(f'{Fore.GREEN}videos in video folder{Style.RESET_ALL}')

    for video in all_videos_in_videos_folder:
        # if DEBUG :
        #     print(f'{Fore.YELLOW}video {Style.RESET_ALL}: ' + str(video))
        ...

    output_video = str(current_directory_path) + '.mp4'
    # pretty_print_value(output_video,"output_video")

    output_video = current_directory_path + '/' + current_directory_name + '.mp4'
    if os.path.isfile(str(current_directory_path) + '/' + output_video):
        # print(f'{Fore.RED}output video already exists{Style.RESET_ALL}')
        sys.exit()
        ...

    if concatenated_video_found:
        # if DEBUG :
        #     print(f'{Fore.MAGENTA}concatenated video found{Style.RESET_ALL}')
        sys.exit()

    video_list_file = '{0}{1}' \
        .format(current_directory_path, make_video_list_file(current_directory_path,
                                                            all_videos_in_videos_folder))
    # cSpell: disable
    ffmpeg_command = 'ffmpeg -f concat -safe 0 -i \'{0}\' -c copy \'{1}\'' \
                        .format(video_list_file, output_video)

    print("> os.system(ffmpeg_command) : \n\n{0}".format(ffmpeg_command))
    print()
    # if DEBUG :
    #     print(f'{Fore.BLUE}ffmpeg command{Style.RESET_ALL}: ' + FFMPEG_COMMAND)

    os.system(ffmpeg_command)      # deactivate to test
    # cSpell: enable



    ...







if __name__ == "__main__":
    main()
    ...
