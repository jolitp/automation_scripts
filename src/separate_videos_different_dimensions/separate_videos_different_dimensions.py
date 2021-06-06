#! /usr/bin/env python3
"""
separate videos in a folder based on their dimensions
"""
# cSpell: word jolitp pytest miliseconds avidemux isdigit
import os
import csv
from pathlib import Path

from rich.console import Console
import snoop
from snoop import spy


# TODO move to utils module
# region debug_context ================================================= debug_context
# courtesy of stackoverlow:
# https://stackoverflow.com/questions/32163436/python-decorator-for-printing-every-line-executed-by-a-function
import sys

class debug_context():
    """ Debug context to trace any function calls inside the context """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Entering Debug Decorated func')
        # Set the trace function to the trace_calls function
        # So all events are now traced
        sys.settrace(self.trace_calls)

    def __exit__(self, *args, **kwargs):
        # Stop tracing all events
        sys.settrace = None

    def trace_calls(self, frame, event, arg):
        # We want to only trace our call to the decorated function
        if event != 'call':
            return
        elif frame.f_code.co_name != self.name:
            return
        # return the trace function to use when you go into that
        # function call
        return self.trace_lines

    def trace_lines(self, frame, event, arg):
        # If you want to print local variables each line
        # keep the check for the event 'line'
        # If you want to print local variables only on return
        # check only for the 'return' event
        if event not in ['line', 'return']:
            return
        code = frame.f_code
        # print("code = " + str(code))
        func_name = code.co_name
        line_no = frame.f_lineno
        filename = code.co_filename
        local_vars = frame.f_locals
        # print(f"type of frame: {type(frame)}")
        c = Console()
        import inspect
        # source = inspect.getsource(code)
        # source_lines = inspect.getsourcelines(code)
        # c.print(source_lines)
        # print()
        # print("lines:")
        # for line in source_lines:
            # print()
            # c.print(line)
        # print()
        # A named tuple
        # Traceback(filename, lineno, function, code_context, index) is returned.
        frame_info = inspect.getframeinfo(frame, context=1)
        frame_line_no = frame_info.lineno
        code_context = frame_info.code_context
        # c.print(frame_line_no)
        line = (frame_line_no, code_context)
        # for info in frame_info:
            # c.print(info)
        # print(source)
        c.print("===========================================")
        c.print(str(line[0]) + str(line[1][0]))
        # c.print ('{0} {1} {2} locals:'\
        #     .format(
        #             line_no,
        #             func_name,
        #             event))
        c.print(local_vars)
        c.print("---------------------------------------------")

        # c.print ('  {0} {1} {2} locals: {3}'\
        #     .format(func_name,
        #             event,
        #             line_no,
        #             local_vars))
# endregion debug_context ----------------------------------------- debug_context


# region debug_decorator =============================================== debug_decorator
def debug_decorator(func):
    """ Debug decorator to call the function within the debug context """
    def decorated_func(*args, **kwargs):
        with debug_context(func.__name__):
            return_value = func(*args, **kwargs)
        return return_value
    return decorated_func
# endregion debug_decorator ------------------------------------------- debug_decorator


# region ========================================== load_video_infos_csv
def load_video_infos_csv(file_path: str):
    """load the values of a .csv file
    containing the info of all videos
    in the directory

    Args:
        file_path (str): the file path to the file

        debug_function (bool, optional): Defaults to None.

    Returns:
        (list(dict)): the values from .csv file parsed into a dictionary
    """
    c = Console()
    c.print("[green]# region ========================================== load_video_infos_csv[/]")
    c.print("[blue]def[/] [yellow]load_video_infos_csv[/]([cyan]file_path[/]: [green]str[/]):")
    if not os.path.isfile(file_path):
        return []
    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)

    c.print("[green]# region ------------------------------------------ load_video_infos_csv[/]")
    return video_info_list
# endregion --------------------------------------- load_video_infos_csv


# region filter_data ======================================== filter_data
def filter_domensions(data_list:list):
    filtered_data = []
    for input_data in data_list:
        width = input_data["width"]
        height = input_data["height"]
        dimensions = (width,height)
        filtered_data.append(dimensions)
    return filtered_data
    ...
# endregion filter_data ------------------------------------ filter_data


# TODO add to printing library
# region print_range_in_list ======================= print_range_in_list
# @snoop
def print_range_in_list(
    list_name:str,
    input_list:list,
    range_name:str,
    range:list,
    should_print=True,
    ):
    """prints or returns a string of the input list on the vertical
    and points to the specified index to the right

    Args:
        list_name (int): the name to give the list

        input_list (list): the list to print

        range_name (int): the name to give range

        range (int): the position on the list to print

        should_print (bool): whether or not to print the result
    """

    c = Console()
    header = "{} = [\n".format(list_name)
    lines = []
    footer = "]"
    for index, item in enumerate(input_list):
        begin_index, end_index = range
        if begin_index == index and end_index == index:
            this_line = "  " + str(item) + \
                " <- {}\n".format("begin and end of " + range_name)
        if begin_index == index:
            this_line = "  " + str(item) + \
                " <- {}\n".format("begin of " + range_name)
        elif end_index == index:
            this_line = "  " + str(item) + \
                " <- {}\n".format("end of " + range_name)
        else:
            this_line = "  " + str(item) + "\n"
        lines.append(this_line)
        ...
    output = header
    for line in lines:
        output += line
    output += footer
    if should_print:
        c.print(output)
    return output
    ...
# endregion print_range_in_list -------------------- print_range_in_list


# TODO add to printing library
# region print_popsition_in_list =============== print_popsition_in_list
# @snoop
def print_popsition_in_list(
    list_name:str,
    input_list:list,
    position_name:str,
    position:int,
    should_print=True,
    ):
    """prints or returns a string of the input list on the vertical
    and points to the specified index to the right

    Args:
        input_list (list): the list to print

        position (int): the position on the list to print

        should_print (bool): whether or not to print the result
    """

    c = Console()
    c.print("[green]# region print_popsition_in_list =============== print_popsition_in_list[/]")
    header = "{} = [\n".format(list_name)
    lines = []
    footer = "]"
    for index, item in enumerate(input_list):
        if position == index:
            this_line = "  " + str(item) + \
                " <- {}\n".format(position_name)
        else:
            this_line = "  " + str(item) + "\n"
        lines.append(this_line)
        ...
    output = header
    for line in lines:
        output += line
    output += footer
    if should_print:
        c.print(output)
    c.print("[green]# region print_popsition_in_list ------------------- print_popsition_in_list[/]")
    return output
# endregion print_popsition_in_list ------------ print_popsition_in_list


# region segment_by_dimensions =================== segment_by_dimensions
# @debug_decorator
def segment_by_dimensions(dimensions_list:list):
    """
    separate a list of dimensions in a list of segments

    example:

    input: [
        (1920,1080), <- index 0
        (1920,1080), <- index 1
        (1080,720),  <- index 2
        (1080,720),  <- index 3
        (1920,1080), <- index 4
        (1920,1080), <- index 5
    ]

    should return:
        [ (0,1), (2,3), (4,5) ]

    Args:
        dimensions (list(tuple)): a list of dimensions

    Returns:
        (list(list)): a list of segments(start,end)
    """
    # c = Console()
    c.print("[green]# region segment_by_dimensions =============================== segment_by_dimensions [/]")
    c.print("[blue]def[/] [yellow]segment_by_dimensions[/]([cyan]dimensions_list[/]:[green]list[/]):")
    c.print("[cyan]                          dimensions_list[/]:[green]list[/]) -> [cyan]{}[/]:[green]{}[/]"\
        .format(dimensions_list,type(dimensions_list)))
# TODO fix bug: last segment is missing
    segments_list = []
    previous_dimension = None
    dimensions_length = len(dimensions_list)
    current_segment = [0, 0]
    for index, current_dimension in enumerate(dimensions_list):
        # print(f"iteration {index} ============================================ iteration {index}")
        if index > 0:
            if current_dimension == previous_dimension:
                current_segment[1] += 1
                # print(index)
                # print("length ", str(dimensions_length))
                if index == dimensions_length -1:
                    segments_list.append(current_segment)
            else:
                segments_list.append(current_segment)
                current_segment = [index, index]
        previous_dimension = current_dimension
        # print(f"iteration {index} ----------------------------------------------- iteration {index}")

    segments = []
    for element in segments_list:
        begin, end = element
        segments.append((begin,end))
        ...
    c.print("[green]# region segment_by_dimensions ------------------------------- segment_by_dimensions [/]")
    return segments
# endregion segment_by_dimensions ---------------- segment_by_dimensions


def get_folder_number(folder_path:Path):
    cwd = Path(os.getcwd())
    folder_basename = os.path.basename(folder_path)
    folder_number = ''
    last_character_of_folder_basename_is_digit = str(folder_path)[-1].isdigit()
    if last_character_of_folder_basename_is_digit:
        if "videos" in folder_basename:
            only_number = folder_basename.replace("videos", "")
            folder_number = only_number
    return folder_number


def get_absolute_paths_to_videos_in_each_segment(segments, videos_data_list):
    cwd = Path(os.getcwd())
    segment_paths = []
    for segment in segments:
        begin, end = segment
        length = end - begin
        for data_index in range(length):
            current_video_data = videos_data_list[data_index]
            video_path = cwd / Path(current_video_data["full_path"])
            # print(video_path)
            segment_paths.append(video_path)
            ...
        ...
    return segment_paths


def get_segment_lengths(segments):
    segment_lengths = []
    for segment in segments:
        begin, end = segment
        segment_length = end - begin
        segment_lengths.append(segment_length)
    return segment_lengths


# region process_folder ================================================ process_folder
def process_folder(folder_path:Path):
    c = Console()
    c.print("[green]# region ================================================ process_folder[/]")
    c.print("[blue]def[/] [yellow]process_folder[/]([cyan]folder_path[/]:[green]Path[/]):")
    c.print("[cyan]                   folder_path[/]:[green]Path[/]) -> [cyan]{}[/]:[green]{}[/]"\
        .format(folder_path,type(folder_path)))


    folder_number = get_folder_number(folder_path)

    csv_file = folder_path / ".generated/video_infos.csv"
    csv_file_exists = os.path.isfile(csv_file)
    if csv_file_exists:
        videos_data_list = load_video_infos_csv(csv_file)
        dimensions = filter_domensions(videos_data_list)
        segments = segment_by_dimensions(dimensions)
        segment_paths = get_absolute_paths_to_videos_in_each_segment(segments, videos_data_list)
        segment_lengths = get_segment_lengths(segments)

        n_of_segments = len(segments)
        has_a_single_segment = n_of_segments == 1
        print(has_a_single_segment)
        # if has_a_single_segment:
            # return None
        if n_of_segments > 3:
            ...
            # TODO check if segments have many 1 video segment
            # if have more than 3 segments that have 1 video only
        sections_with_one_video = []
        for length in segment_lengths:
            predicate = None
            if length == 1:
                predicate = True
            else:
                predicate = False
            sections_with_one_video.append(predicate)
        c.print(sections_with_one_video)
        # TODO check if segments are short
        # meaning they have less than 5 elements per section
    else:
        c.print("[bold red]no csv file in path:{}[/]" \
            .format(csv_file))
        return None
    c.print("[green]# endregion --------------------------------------------- process_folder[/]")
# endregion process_folder ---------------------------------------------- process_folder


# region main =========================================================== main
def main():
    c = Console()
    c.print("[green]# region main(): ================================================== main[/]", style="green")
    c.print("[blue]def[/] [yellow]main[/]():")

    cwd = Path(os.getcwd())
# TODO also process converted videos if they are available
    videos_folder_paths = []
    for item in cwd.iterdir():
        item_path = Path(item)
        if item_path.is_dir():
            basename = os.path.basename(item_path)
            if "videos" in basename:
                videos_folder_paths.append(item_path)

    if videos_folder_paths:
        for path in videos_folder_paths:
            process_folder(path)

    c.print("[green]# endregion main(): ----------------------------------------------- main[/]", style="green")
# endregion main -------------------------------------------------------- main


# region current_test ====================================== current_test
def current_test():
    c = Console()
    c.print("# region current_test ===================================== current_test", style="green")
    c.print("[blue]def[/] [yellow]current_test[/]():")
    input = [
        (1920,1080),
        (1920,1080),
        (1080,720),
        (1080,720),
        (1920,1080),
        (1920,1080),
    ]

    expected_output = \
    [
        (0,1),
        (2,3),
        (4,5)
    ]

    actual_output = segment_by_dimensions(input)

    assertions = []
    for index, item in enumerate(expected_output):
        assertion = expected_output[index] == actual_output[index]
        assertions.append(assertion)
        ...
    # assertion = expected_output == actual_output

    c.print("input: {}".format(input))
    c.print("expected_output : {}".format(expected_output ))
    c.print("actual_output : {}".format(actual_output))
    c.print("assertion : {}".format(assertions))
    ...

    c.print("    [white]...[/]", style="white")
    c.print("# endregion current_test ---------------------------------- current_test",style="green")
# endregion current_test ----------------------------------- current_test


# region if __name__ == "__main__": ========== if __name__ == "__main__":
if __name__ == "__main__":
    c = Console()
    c.print("# region if __name__ == \"__main__\": ========= if __name__ == \"__main__\":", style="green")

    main()
    # current_test()

    c.print("# endregion if __name__ == \"__main__\": ------ if __name__ == \"__main__\":",style="green")
# endregion if __name__ == "__main__": ------- if __name__ == "__main__":

