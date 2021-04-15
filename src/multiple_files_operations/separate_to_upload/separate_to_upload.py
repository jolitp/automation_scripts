#! /usr/bin/python3
"""
    separate the videos of a folder to be uploaded to youtube
"""
import os
import sys
import importlib.util # needed for importing scripts using the scripts path
import shutil # needed to move files
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
    shutil.move(source,destination)


def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)
# region debug_function
    if debug_function:
        print("[def] main()")
        print("{")
# endregion
    current_directory_path = os.getcwd()
    all_files_and_folders = os.listdir(current_directory_path)
    videos_only = []
# region debug_function
    if debug_function:
        print()
        print("> [FOR] video in all_files_and_folders:")
        print()
# endregion
    for file_or_folder in all_files_and_folders:
# region debug_function
        if debug_function:
            print("> > [iteration] START")
            print("> > file_or_folder: {}".format(file_or_folder))
            print()
            print("> > [if] is_video(file_or_folder): {}"\
                .format(is_file_video_script.is_video(file_or_folder)))
# endregion
        if is_file_video_script.is_video(file_or_folder):
            videos_only.append(file_or_folder)
# region debug_function
        if debug_function:
            print()
            print("> > [iteration] END")
            print()
# endregion
    videos_only.sort()
# region debug_function
    if debug_function:
        print()
        print("> [FOR] video in videos_only:")
        print()
# endregion
    count = 0
    batches = []
    batch = []
    for video in videos_only:
# region debug_function
        if debug_function:
            print("> > [iteration] START")
            print("> > video: {}".format(video))
            print()
            print("> > count = {}".format(count))
# endregion
        if count == 0:
# region debug_function
            print()
            print("> > batches(before): \n{}".format(batches))
            print()
            batches.append(batch)
            print()
            print("> > batches(before): \n{}".format(batches))
            print()
# endregion
# region debug_function
        if debug_function:
            print("> > count(before)= {}".format(count))
# endregion
        count += 1
# region debug_function
        if debug_function:
            print("> > count(after)= {}".format(count))
# endregion
# region debug_function
        if debug_function:
            print()
            print("> > batch(before): \n{}".format(batch))
            print()
# endregion
        batch.append(video)
# region debug_function
        if debug_function:
            print()
            print("> > batch(after): \n{}".format(batch))
            print()
# endregion
        ...
# region debug_function
        if debug_function:
            print()
            print("> > if count > 15: {}".format(count > 15))
            print()
# endregion
        if count >= 15:
# region debug_function
            if debug_function:
                print()
                print("> > count(before): \n{}".format(count))
                print()
# endregion
            count = 0
# region debug_function
            if debug_function:
                print()
                print("> > count(after): \n{}".format(count))
                print()
# endregion
# region debug_function
            if debug_function:
                print()
                print("> > batch(before): \n{}".format(batch))
                print()
# endregion
            batch = []
# region debug_function
            if debug_function:
                print()
                print("> > batch(after): \n{}".format(batch))
                print()
# endregion
# region debug_function
        if debug_function:
            print()
            print("> > [iteration] END")
            print()
# endregion debug_function
# region debug_function
    if debug_function:
        print()
        print("> [FOR] index, batch in enumerate(batches):")
        print()
# endregion
    for index, batch in enumerate(batches):
# region debug_function
        if debug_function:
            print()
            print("> > [iteration] START")
            print()
# endregion
# region debug_function
        if debug_function:
            print()
            print("> [FOR] video in batch:")
            print()
# endregion
        for video in batch:
# region debug_function
            if debug_function:
                print()
                print("> > [iteration] START")
                print()
# endregion
            folder_name = "[upload_{0:02d}]".format(index)
# region debug_function
            if debug_function:
                print("> > > folder_name = {}".format(folder_name))
# endregion
            if not os.path.isdir(folder_name):
                print("making directory: {}".format(folder_name))
                os.mkdir(folder_name)
            source = current_directory_path + "/" + video
            destination = current_directory_path + "/" + folder_name + "/" + video
            print()
            print("source : \n{}".format(source))
            print()
            print("destination : \n{}".format(destination))
            print()
            move_video(source,destination)
# region debug_function
            if debug_function:
                print()
                print("> > [iteration] END")
                print()
# endregion
            ...
# region debug_function
        if debug_function:
            print()
            print("> > [iteration] END")
            print()
# endregion
        ...
    uploaded_folder = current_directory_path + "/" + "[_0_uploaded_0_]"
# region debug_function
    if debug_function:
        print()
        print("> > if not os.path.isdir(uploaded_folder): {}"\
            .format(not os.path.isdir(uploaded_folder)))
        print()
# endregion
    if not os.path.isdir(uploaded_folder):
        os.mkdir(uploaded_folder)

# region debug_function
    if debug_function:
        print("}")
# endregion

# endregion def main(...)


# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    print("module_template.py.__main__")
    print()

    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('filename.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('This message will be written to a file.')

        main(
            debug_function = debug_script
            )
        sys.stdout = original_stdout # Reset the standard output to its original value
    ...
# endregion if __name__ == "__main__":
