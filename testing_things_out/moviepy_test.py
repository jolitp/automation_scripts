#! /usr/bin/env python3


from moviepy.editor import VideoFileClip, concatenate_videoclips

clip_1 = VideoFileClip("1.mp4")
clip_2 = VideoFileClip("2.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2])
final_clip.write_videofile("final.mp4")
