#!/usr/bin/python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        files = (file for file in os.listdir(folder_track) if os.path.isfile(os.path.join(folder_track, file)))
        for file_name in files:
            scr = os.path.join(folder_track, file_name)

            if scr.lower().endswith(('.txt', '.doc','.docx')):
                name_folder = 'Text Files'
            elif scr.lower().endswith(('.png', '.jpg','.jpeg')):
                name_folder = 'Image Files'
            elif scr.lower().endswith('.pdf'):
                name_folder = 'PDF Files'
            elif scr.lower().endswith('.iso'):
                name_folder = 'ISO Files'
            elif scr.lower().endswith(('.rar', '.zip', '.tar', '.7z')):
                name_folder = 'Compacted Files'
            elif scr.lower().endswith(('.py', '.sh', '.ipynb')):
                name_folder = 'Script Files'
            elif scr.lower().endswith(('.csv')):
                name_folder = 'Table Files'
            else:
                name_folder = 'Others'

            new_folder = os.path.join(folder_track, name_folder)
            new_file_location = os.path.join(new_folder, file_name)
            if os.path.isdir(new_folder):
                os.rename(scr, new_file_location)
            else:
                os.mkdir(new_folder)
                os.rename(scr, new_file_location)


folder_track = '/home/mateusm/Downloads/'
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
