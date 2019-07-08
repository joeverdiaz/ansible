import os
import shutil
path = "/home/python/"
names = os.listdir(path)
folder_name = ['music','video','file','picture']
for x in range(0,4):
    if not os.path.exists(path+folder_name[x]):
       os.makedirs(path+folder_name[x])
for files in names:
    if ".mp3" in files and not os.path.exists(path+'music/'+files):
       shutil.move(path+files, path+'music/'+files)
    if ".png" in files and not os.path.exists(path+'picture/'+files):
       shutil.move(path+files, path+'music/'+files)
    if ".txt" in files and not os.path.exists(path+'file/'+files):
       shutil.move(path+files, path+'file/'+files)
    if ".mp4" in files and not os.path.exists(path+'video/'+files):
       shutil.move(path+files, path+'video/'+files)
