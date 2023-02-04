import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/frank/Downloads/sample" 
to_dir = "C:/Users/frank/OneDrive/Desktop/Downloaded_files"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded " + file_name)
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name
                if os.path.exists(path2):
                    print("Directory Exists...")
                    time.sleep(1)
                    if os.path.exists(path3):
                        print ("file Already exists in " + key +"....")
                        print("Renaming file " + file_name +"...")
                        new_file_name=os.path.splitext(file_name)[0] + str(random.randint(0,999))+ os.path.splitext(file_name)[1]
                        path4 = to_dir + '/' + key + '/' + new_file_name
                        print("Moving " + new_file_name + "....")
                        shutil.move(path1, path4)
                        time.sleep(1)
                    else:
                        print("Moving " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)
                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
