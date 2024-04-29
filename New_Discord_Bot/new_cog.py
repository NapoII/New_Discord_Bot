import os
import sys
import pyautogui
file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = f"{file_path}{os.path.sep}config{os.path.sep}config.ini"

template_folder = f"{file_path}{os.path.sep}Templates"

print(file_path)


cog_name = pyautogui.prompt(text='Was ist der name des Discord Cog', title='Create a New Cog' , default='')
