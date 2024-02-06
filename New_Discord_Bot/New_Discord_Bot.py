import os
import sys
import webbrowser

import pyautogui
from util.__funktion__ import *
# from util.gen_readme import readme_gen
from pandas.io import clipboard
from util.gen_readme import readme_gen

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = f"{file_path}{os.path.sep}config{os.path.sep}config.ini"

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
template_folder = f"{file_path}{os.path.sep}Templates"

# start

# name of the Projekt
new_discord_bot_name = pyautogui.prompt(text='What should the project be called?', title='New Discord Bot', default='')

# path of the New Porjekt Folder
default_folder = read_config(config_dir, "default", "default_folder")
default_folder = pyautogui.prompt(text='what is the destination folder?', title='New Discord Bot', default=default_folder)

# Name of the gitHub User
gituser_default = read_config(config_dir, "readme", "github_user")

# Main projekt Folder gets createt
projekt_folder = Folder_gen(new_discord_bot_name, default_folder)

# create LICENSE
template_LICENSE_dir = f"{template_folder}{os.path.sep}LICENSE"
template_LICENSE = Read_File_Out(template_LICENSE_dir)
Create_File("LICENSE", projekt_folder, template_LICENSE)

#create .gitignore
template_gitignore_dir = f"{template_folder}{os.path.sep}.gitignor-temp.txt"
template_gitignore = Read_File_Out(template_gitignore_dir)
Create_File(".gitignore", projekt_folder, template_gitignore)

#create requirements
template_requirements_dir = f"{template_folder}{os.path.sep}requirements-temp.txt"
template_requirements = Read_File_Out(template_requirements_dir)
Create_File("requirements.txt", projekt_folder, template_requirements)

#create ToDo
template_ToDo_dir = f"{template_folder}{os.path.sep}template_TODO_md.txt"
template_ToDo = Read_File_Out(template_ToDo_dir)
Create_File("ToDo.md", projekt_folder, template_ToDo)

#create README
README_img_folder = Folder_gen("README_img",projekt_folder)
discord_bot_gif = f"{template_folder}{os.path.sep}discord_bot.gif"
discord_bot_ico = f"{template_folder}{os.path.sep}discord_bot.ico"
Readme_top_raw_png = f"{template_folder}{os.path.sep}Readme_top.raw.png"
Readme_top_raw_psd = f"{template_folder}{os.path.sep}Readme_top.psd"
copy_image(discord_bot_gif, README_img_folder)
copy_image(discord_bot_ico, README_img_folder)
copy_image(Readme_top_raw_png, README_img_folder)
copy_image(Readme_top_raw_psd, README_img_folder)

Readme_top = f"{template_folder}{os.path.sep}Readme_top.raw.png"
font_path = f"{template_folder}{os.path.sep}readme_header.ttf"
readme_gen(new_discord_bot_name, projekt_folder, Readme_top, README_img_folder, config_dir, font_path)

#create Main Folder
discord_bot_name_folder = Folder_gen(new_discord_bot_name, projekt_folder)

#create main file
main_py_dir = f"{template_folder}{os.path.sep}template_main.py.txt"
main_py = Read_File_Out(main_py_dir)
main_py = change_var_in_template(main_py, "NapoII", gituser_default)
Create_File(f"{new_discord_bot_name}.py", discord_bot_name_folder, main_py)

#create config Folder
discord_bot_config_folder = Folder_gen("config", discord_bot_name_folder)

#create config file
config_temp_dir = f"{template_folder}{os.path.sep}template_config.txt"
config_temp = Read_File_Out(config_temp_dir)
Create_File(f"config.ini", discord_bot_config_folder, config_temp)

#create token file
token_temp_dir = f"{template_folder}{os.path.sep}template_token.txt"
token_temp = Read_File_Out(token_temp_dir)
Create_File(f"token.ini", discord_bot_config_folder, token_temp)

#create util Folder
discord_bot_util_folder = Folder_gen("util", discord_bot_name_folder)

#create __funktion__ token file
__funktions__temp_dir = f"{template_folder}{os.path.sep}template___funktion__.txt"
__funktions__temp = Read_File_Out(__funktions__temp_dir)
__funktions__temp = change_var_in_template(__funktions__temp, "NapoII", gituser_default)
Create_File(f"__funktion__.py", discord_bot_util_folder, __funktions__temp)

#create __Mydiscord_funktions__ token file
__Mydiscord__temp_dir = f"{template_folder}{os.path.sep}template___Mydiscord_funktions__.txt"
__Mydiscord_temp = Read_File_Out(__Mydiscord__temp_dir)
__Mydiscord__temp = change_var_in_template(__Mydiscord_temp, "NapoII", gituser_default)
Create_File(f"__Mydiscord_funktions__.py", discord_bot_util_folder, __Mydiscord__temp)


#create discord_cogs Folder
discord_bot_discord_cogs_folder = Folder_gen("discord_cogs", discord_bot_name_folder)
discord_bot_discord_admin_cogs_folder = Folder_gen("admin", discord_bot_discord_cogs_folder)

#create  say file
say_temp_dir = f"{template_folder}{os.path.sep}template_say.txt"
say_temp_dir = Read_File_Out(say_temp_dir)
say_temp = change_var_in_template(say_temp_dir, "NapoII", gituser_default)
Create_File(f"say.py", discord_bot_discord_admin_cogs_folder, say_temp)

#create  pre_setup file
pre_setup_temp_dir = f"{template_folder}{os.path.sep}template_pre_setup.py.txt"
pre_setup_temp_dir = Read_File_Out(pre_setup_temp_dir)
pre_setup_temp = change_var_in_template(pre_setup_temp_dir, "NapoII", gituser_default)
Create_File(f"pre_setup.py", discord_bot_discord_admin_cogs_folder, pre_setup_temp)

webbrowser.open('file:///' + projekt_folder)
clipboard.copy(projekt_folder)
print("The project was created and the folder address was added to the clipboard..")