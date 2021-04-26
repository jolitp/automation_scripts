#! /usr/bin/python3
import os
import shutil

current_dir_path = os.getcwd()
current_dir = os.path.basename(current_dir_path)

print(current_dir)

all_files_full_path = []
for root, directories, filenames in os.walk(current_dir_path):
  for filename in filenames: 
    all_files_full_path.append(os.path.join(root,filename))

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob', '.ogm', '.rmvb']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

all_videos = []
for file_path in all_files_full_path:
  if is_video(file_path):
    all_videos.append(file_path)

all_files = {}

for file_path in all_videos:


  all_files[file_path] = {
    'file_name' : os.path.basename(file_path),
    'folders' : '/' + os.path.dirname(file_path)
                .replace(current_dir_path,'')[1:]
                .replace('/', ' '),
    'folder_path': os.path.dirname(file_path)
  }

all_videos_with_new_name = []
# rename
for path in all_files:
  new_name = all_files[path]['folder_path']+ all_files[path]['folders']+ ' '+ all_files[path]['file_name']
  if ' BIG' in new_name or ' SMALL' in new_name:
    continue
  os.rename(path, new_name)
  all_videos_with_new_name.append(new_name)

  # print(all_files[path]['folder_path'])
  # print(all_files[path]['folders'])
  # print(all_files[path]['file_name'])
  # print('\n')
  # print(new_name)
  # print('\n')

  # print(str(len(new_name)) + '    '+ new_name)

destination = current_dir_path 
print(destination)

for video in all_videos_with_new_name:
  source = video
  print(source)
  shutil.move(source, destination)
  pass












# what i want to do

# given a root folder (can be the folder the script is in (will need to copy the script each time))
# get every video with a video extension "*.mp4" 
# and change the name to the root directory + other directory + filename.ext
