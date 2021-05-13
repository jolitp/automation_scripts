#! /usr/bin/python3

import os
import importlib.util
# import pathlib


spec = importlib.util.spec_from_file_location("module.name",
    "/home/jolitp/Dropbox/PROJECTS/python-scripts/helpers/helpers/helpers.py")
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)


# region def get_first_common_characters(first_name : str, second_name : str) -> str:
def get_first_common_characters(first_name : str, second_name : str) -> str:
    """ get the first set of characters that two names have in common
        Parameters:
            first_name (str): the first name
            second_name (str): the second name
            prefer (str): if the names don't have any starting characters in common
                        prefer either the first or the second as a return value
        Returns:
            characters_in_common_at_the_start (str): the characters in common from both
                first and second names
    """

    # print()
    # print("[def] get_first_common_characters")
    # print("  first_name : " + first_name )
    # print("  second_name : " + second_name )
    # print("{")
    # print()

    characters_in_common_at_the_start = ""

    # print("->[for] index_fun, character_in_first in enumerate(first_name):")

    for index_fun, character_in_first in enumerate(first_name):

        # print("[for] iteration start")
        # print("->->index_fun : " + str(index_fun) )
        # print("->->character_in_first : " + str(character_in_first) )
        # print()

        characters_in_second : str = second_name[index_fun]
        chars_are_the_same : bool = character_in_first == characters_in_second

        # print("  characters_in_second : " + str(characters_in_second) )

        if chars_are_the_same:
            is_index_at_the_start : bool = index_fun == 0
            if is_index_at_the_start:
                characters_in_common_at_the_start : str = ""

            characters_in_common_at_the_start += character_in_first
            ...
        else:
            break

        # print("[for] iteration end")
        # print("  index_fun : " + str(index_fun) )
        # print("  character_in_first : " + str(character_in_first) )
        # print()
        ...

    # print("->[for] end")
    pred_1 = characters_in_common_at_the_start == first_name
    pred_2 = characters_in_common_at_the_start == second_name
    is_first_or_second_name = pred_1 or pred_2

    if is_first_or_second_name:
        name_without_extension : str = os.path.splitext(characters_in_common_at_the_start)[0]
        characters_in_common_at_the_start = name_without_extension
        ...

    numbers_found : bool = False
    letters_found : bool = False
    # last_char_was_number = False
    index_to_cut : int = len(characters_in_common_at_the_start)
    for index_function, character in enumerate(characters_in_common_at_the_start):

        is_char_number : bool = character.isdigit()

        if is_char_number:
            numbers_found = True
            ...
        else:
            letters_found = True
            ...
        if is_char_number and numbers_found and letters_found:
            index_to_cut = index_function
            break
            # ...
        else:
            ...
        ...

    first_part = characters_in_common_at_the_start[:index_to_cut]

    print()
    print("}")
    print()
    return first_part
# endregion


# region def get_sections(list_of_filenames):
def get_sections(list_of_filenames):
    """get sections that correspond to the first part of the names files
    in a list

    Args:
        list_of_file_names (list): the list of files

    Returns:
        dict(str:list(str)): a dictionary with sections as keys and
        list of files as values
    """
    print()
    print("get_sections BEGIN")
    print()
    sections = {}
    for index, _ in enumerate(list_of_filenames):
        file_names_in_this_section = []
        section_name : str = ""
        is_not_last_index = index < len(list_of_filenames) -1

        if is_not_last_index:
            this_index : int = index
            next_index : int = index + 1

            this_item = list_of_filenames[this_index]
            next_item = list_of_filenames[next_index]

            section_name = get_first_common_characters(this_item, next_item)
            current_index = index

            while current_index < len(list_of_filenames) -1:
                current_item = list_of_filenames[current_index]
                # print(" if : " + current_item)
                if section_name in current_item:
                    file_names_in_this_section.append(current_item)

                current_index += 1

                ...

            section_name_in_sections : bool = section_name in sections

            if section_name_in_sections:
                continue

            ...
        else: # if is last index
            this_index : int = index
            previous_index : int = index - 1

            this_item = list_of_filenames[this_index]
            previous_item = list_of_filenames[previous_index]

            section_name = get_first_common_characters(
                            this_item, previous_item)

            current_index = index

            while current_index >= 0:
                # print("current index in else : " + str(current_index))
                current_item = list_of_filenames[current_index]
                # print("current item: " + current_item)
                if section_name in current_item:
                    file_names_in_this_section.append(current_item)

                current_index -= 1

            section_name_in_sections : bool = section_name in sections

            # if section_name_in_sections:
            #     continue
    # for index, item in enumerate(list_of_filenames): end

        sections[section_name] = file_names_in_this_section

    # TODO remove sections that fit in other sections

    for section, filenames in sections.items():
        for name in filenames:
            for other_section, other_filenames in sections.items():

                for other_name in other_filenames:

                    if section == other_section:

                        continue
# TODO FIXME BUG not all duplicate files are being removed from dict

                    if section in other_section:

                        if name == other_name:
                            sections[section].remove(name)


                ...
            ...
        ...
# TODO inside the sections dictionary = key(str): value[set] instead of key(str): value[list]
    """
    https://www.w3schools.com/python/python_sets.asp
    """

    print()
    print("get_sections  END")
    print()
    return sections
# endregion


def get_all_videos_from_directory(directory: str):
    """get all videos from a directory

    Args:
        directory (str): the directory to scan for videos

    Returns:
        [type]: a list of all videos
    """
    all_files_and_folders = os.listdir(directory)

    all_videos = []
    for video in all_files_and_folders:
        if helpers.is_video(video):
            all_videos.append(video)
    all_videos.sort()

    return all_videos



def main():
    """
    main
    """
    all_videos : list(str) = get_all_videos_from_directory(os.getcwd())

    print("\tall videos\n")
    for video in all_videos:
        print(video)

    sections = get_sections(all_videos)

    print("\tsections\n")
    for key, value in sections.items():
        print(key)
        for video in value:
            print("\t" + video)

    source_paths = []
    for video in all_videos:
        full_path : str = os.getcwd() + "/" + video
        source_paths.append(full_path)
        ...

    destination_paths = []
    for section, list_of_videos in sections.items():
        for video in list_of_videos:
            full_path = os.getcwd() + "/" + section + '/' + video
            destination_paths.append(full_path)
            # print("section : " + section + " video " + video)
        ...

    for path in destination_paths:
        print(path)
        ...

    ...

if __name__ == "__main__":
    main()
