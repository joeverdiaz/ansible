# import modules
import os, shutil
from pathlib import Path as path_

files = ["files.txt", "music.mp3", "video.mp4", "image1.png", "image2.jpeg"]
dirs = ["Music", "Videos", "Pictures"]

#create directory
for dir_ in dirs:
    os.mkdir(dir_)

#create files
for file_ in files:
  path_("file_).touch()
  # sort
  if ".mp3" in file_:
    shutil.move(file_, dir[0])
  if ".mp4" in file_:
    shutil.move(file_, dir[1])
  if ".jpeg" in file_:
    shutil.move(file_, dir[2])
  else:
    os.remove(files)
