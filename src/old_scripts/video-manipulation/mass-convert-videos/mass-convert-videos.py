#! /usr/bin/python3

import subprocess
import pathlib
import os
import sys
import json

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

path_to_current_directory = pathlib.Path(__file__).parent.absolute()
all_files_and_folders = os.listdir('.')

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
    pass
all_videos.sort()


histogram_general_format = {}
histogram_general_format_profile = {}
histogram_general_codec_id = {}
histogram_general_codec_id_compatible = {}
histogram_general_frame_rate = {}
histogram_general_overall_bit_rate_mode = {}
histogram_general_overall_bit_rate= {}

histogram_video_format = {}
histogram_video_format_profile = {}
histogram_video_codec_id = {}
histogram_video_duration = {}
histogram_video_bit_rate = {}
histogram_video_width = {}
histogram_video_height = {}
histogram_video_frame_rate_mode = {}
histogram_video_frame_rate = {}
histogram_video_encoded_library_name = {}
histogram_video_encoded_library_version = {}
histogram_video_encoded_library_settings = {}
histogram_video_format_level = {}
histogram_video_display_aspect_ratio = {}
histogram_video_color_space = {}
histogram_video_chroma_subsampling = {}

histogram_audio_format = {}
histogram_audio_codec_id = {}
histogram_audio_bit_rate = {}
histogram_audio_bit_rate_mode = {}
histogram_audio_sampling_rate = {}
histogram_audio_frame_rate = {}

def add_to_histogram(key, histogram):
    if key in histogram:
        histogram[key] = int(histogram[key]) + 1
    else: 
        histogram[key] = 1
    
    
for video in all_videos:
    result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', video], 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    # print('\n')
    parsed = json.loads(result.stdout)
    # print(json.dumps(parsed, indent=2))
    general_category = parsed["media"]["track"][0]
    print(general_category)

    if "Duration" in general_category:
        general_duration = general_category["Duration"]

    general_frame_rate = general_category["FrameRate"]
    add_to_histogram(general_frame_rate, histogram_general_frame_rate)
    if "OverallBitRate_Mode" in general_category:
        overall_bit_rate_mode = general_category["OverallBitRate_Mode"]
        add_to_histogram(overall_bit_rate_mode, histogram_general_overall_bit_rate_mode)
    
    general_overall_bit_rate = general_category["OverallBitRate"]
    add_to_histogram(general_overall_bit_rate, histogram_general_overall_bit_rate)
    general_format = general_category["Format"]
    add_to_histogram(general_format, histogram_general_format)
    if "Format_Profile" in general_category:
        general_format_profile = general_category["Format_Profile"]
        add_to_histogram(general_format_profile, histogram_general_format_profile)
    general_codec_id = general_category["CodecID"]
    add_to_histogram(general_codec_id, histogram_general_codec_id)
    general_codec_id_compatible = general_category["CodecID_Compatible"]
    add_to_histogram(general_codec_id_compatible, histogram_general_codec_id_compatible)
    general_overall_bit_rate = general_category["OverallBitRate"]
    add_to_histogram(general_frame_rate, histogram_general_frame_rate)

    video_category = parsed["media"]["track"][1]
    print(video_category)

    video_duration = video_category["Duration"]

    video_format = video_category["Format"]
    add_to_histogram(video_format, histogram_video_format)
    video_format_profile = video_category["Format_Profile"]
    add_to_histogram(video_format_profile, histogram_video_format_profile)
    video_codec_id = video_category["CodecID"]
    add_to_histogram(video_codec_id, histogram_video_codec_id)
    video_bit_rate = video_category["BitRate"]
    add_to_histogram(video_bit_rate, histogram_video_bit_rate)
    video_width = video_category["Width"]
    add_to_histogram(video_width, histogram_video_width)
    video_height = video_category["Height"]
    add_to_histogram(video_height, histogram_video_height)
    video_frame_rate_mode = video_category["FrameRate_Mode"]
    add_to_histogram(video_frame_rate_mode, histogram_video_frame_rate_mode)
    video_frame_rate = video_category["FrameRate"]
    add_to_histogram(video_frame_rate, histogram_video_frame_rate)
    # video_encoded_library_name = video_category["Encoded_Library_Name"]
    # add_to_histogram(video_encoded_library_name, histogram_video_encoded_library_name)
    # video_encoded_library_version = video_category["Encoded_Library_Version"]
    # add_to_histogram(video_encoded_library_version, histogram_video_encoded_library_version)
    # video_encoded_library_settings = video_category["Encoded_Library_Settings"]
    # add_to_histogram(video_encoded_library_settings, histogram_video_encoded_library_settings)
    video_color_space = video_category["ColorSpace"]
    add_to_histogram(video_color_space, histogram_video_color_space)
    video_format_level = video_category["Format_Level"]
    add_to_histogram(video_format_level, histogram_video_format_level)
    video_display_aspect_ratio = video_category["DisplayAspectRatio"]
    add_to_histogram(video_display_aspect_ratio, histogram_video_display_aspect_ratio)
    video_chroma_subsampling = video_category["ChromaSubsampling"]
    add_to_histogram(video_chroma_subsampling, histogram_video_chroma_subsampling)

    audio_category = parsed["media"]["track"][2]
    # print(audio_category)

    audio_format = audio_category["Format"]
    add_to_histogram(audio_format, histogram_audio_format)
    audio_codec_id = audio_category["CodecID"]
    add_to_histogram(audio_codec_id, histogram_audio_codec_id)
    audio_bit_rate = audio_category["BitRate"]
    add_to_histogram(audio_bit_rate, histogram_audio_bit_rate)
    audio_bit_rate_mode = audio_category["BitRate_Mode"]
    add_to_histogram(audio_bit_rate_mode, histogram_audio_bit_rate_mode)
    audio_sampling_rate = audio_category["SamplingRate"]
    add_to_histogram(audio_sampling_rate, histogram_audio_sampling_rate)
    audio_frame_rate = audio_category["FrameRate"]
    add_to_histogram(audio_frame_rate, histogram_audio_frame_rate)

print("=======> general <==============")
print("general format                : " + str(histogram_general_format))
print("general format profile        : " + str(histogram_general_format_profile))
print("general codec id              : " + str(histogram_general_codec_id))
print("general codec id compatible   : " + str(histogram_general_codec_id_compatible))
print("general frame rate            : " + str(histogram_general_frame_rate))
print("general overall bit rate mode : " + str(histogram_general_overall_bit_rate_mode))
print("general overall bit rate      : " + str(histogram_general_overall_bit_rate))
print("=====> video <====================")
print("video format                    : " + str(histogram_video_format))
print("video format profile            : " + str(histogram_video_format_profile))
print("video bit rate                  : " + str(histogram_video_bit_rate))
print("video codec id                  : " + str(histogram_video_codec_id))
print("video width                     : " + str(histogram_video_width))
print("video height                    : " + str(histogram_video_height))
print("video frame rate mode           : " + str(histogram_video_frame_rate_mode))
print("video frame rate                : " + str(histogram_video_frame_rate))
# print("video encoding library name     : " + str(histogram_video_encoded_library_name))
# print("video encoding library version  : " + str(histogram_video_encoded_library_version))
# print("video encoding library settings : " + str(histogram_video_encoded_library_settings))
print("video format level              : " + str(histogram_video_format_level))
print("video display aspect ratio      : " + str(histogram_video_display_aspect_ratio))
print("video color space               : " + str(histogram_video_color_space))
print("video chroma subsampling        : " + str(histogram_video_chroma_subsampling))
print("=====> audio<==========")
print("audio format        : " + str(histogram_audio_format))
print("audio codec id      : " + str(histogram_audio_codec_id))
print("audio bitrate       : " + str(histogram_audio_bit_rate))
print("audio bitrate mode  : " + str(histogram_audio_bit_rate_mode))
print("audio sampling rate : " + str(histogram_audio_sampling_rate))
print("audio frame rate    : " + str(histogram_audio_frame_rate))

"""
things to check for in media info:

General:format profile
General:Codec ID
General:overal bit rate mode
General:overal bit rate

Video:Format profile
Video:CodecID
Video:Width
Video:Height
Video:Aspect Ratio
Video:Frame rate mode
Video:Frame rate

Audio:Format
Audio:CodecID
Audio:Bit rate mode
Audio:sampling rate
Audio:frame rate
"""


path_to_converted_directory = str(path_to_current_directory) + '/converted/'

if not os.path.isdir(path_to_converted_directory):
    os.mkdir(path_to_converted_directory)

for video in all_videos:
    output_video = path_to_converted_directory + video
    print(output_video)
    'ffmpeg -i input -r 30 -c:v libx264 -crf 17 -c:a aac -b:a 128k output.m4v'
    # result = subprocess.run(["ffmpeg",
    #                         f' -i {video}', 
    #                         ' -r 30 ', 
    #                         ' -c:v libx264 ', 
    #                         ' -crf 17 ', 
    #                         ' -c:a aac ', 
    #                         ' -b:a 128k ', 
    #                         output_video
    #                         ], 
    #                         stdout=subprocess.PIPE,
    #                         stderr=subprocess.STDOUT)
    # print(result)
    os.system(f'ffmpeg -i \"{video}\" -r 30 -c:v libx264 -crf 17 -c:a aac -b:a 128k \"{output_video}\"')















