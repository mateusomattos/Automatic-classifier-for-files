# Automatic classifier for files
A simple automatic classifier for files in a folder. Whenever a new file is placed in the folder, the file is directed to a subfolder according to its format. It is verry usefull for the Download folder. The code was bassed in https://www.youtube.com/watch?v=qbW6FRbaSl0&t=106s.

# How to use
Put the script inside a hidden folder in the home and edit the "folder_track" variable to which folder you whant to track. If desired, you can add new types of folder, just by adding it to the code.
The idea is to use the code in the background, initializing it at start-up.

To use, put the file "autostart.service" in the folder "/lib/systemd/system/" and edit the file for your system (the home folder, the folder where is the code...). After, run the command `sudo systemctl start autostart` and `sudo systemctl enable autostart`. 

