#! /usr/bin/env python3
"""join video and sound"""
# cSpell: words ffmpeg ruido aula separado cmdline

from pathlib import Path
import os
import subprocess

from rich import print

# command
# ffmpeg -i "videos com ruido/AULA\ 15-06-2021.mp4"
# 	     -i "som separado sem ruido/AULA\ 15-06-2021.wav"

#        -c:v copy
# 		 -map 0:v:0
# 	     -map 1:a:0
# 		 -c:a aac
#        -b:a 192k

# 		AULA\ 15-06-2021.mp4



if __name__ == '__main__':
    cwd = Path(os.getcwd())

    input_videos_path = cwd / Path("input_videos")
    input_audios_path = cwd / Path("input_audios")
    output_videos_path = cwd / Path("output_videos")

    if not output_videos_path.exists():
        os.mkdir(output_videos_path)

    all_videos = list(input_videos_path.iterdir())
    all_videos.sort()
    all_audios = list(input_audios_path.iterdir())
    all_audios.sort()

    print(f"\n{all_videos = }")
    print(f"\n{all_audios = }")

    for index, _ in enumerate(all_videos):
        video_path = input_videos_path / all_videos[index]
        audio_path = input_audios_path / all_audios[index]
        output_file_path = output_videos_path / video_path.name

        command = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:a", "aac",
            "-b:a", "192k",
            output_file_path
        ]
        cmd = subprocess.list2cmdline(command)

        print()
        print(cmd)
        print()

        subprocess.run(command)
        # os.system(cmd)
        ...

    ...
