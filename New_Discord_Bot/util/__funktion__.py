"""
Use: - from util.__funktion__ import *

ChatGPT promt for docstrgs:

In copy code mode,

write me a .py docstr ("""""") with the content:
Args, Returns and Example Usage.
For Args and Returns create a list with "- ".
and for Example Usage create a list with ">>>  ".
Here is the code:


"""

import os
import re
from configparser import ConfigParser
import shutil
import time
import sys
from PIL import Image, ImageDraw, ImageFont

def new_path(base_path, *additional_paths):
    """
    Combines paths based on a base and optional additional paths.
    
    Args:
        base_path (str): The base path.
        *additional_paths (str): Any number of additional paths.
        
    Returns:
        str: The combined and normalised path.
    """
    # Normalise the base path
    base_path = os.path.normpath(base_path)
    
    # Add all additional paths and create the combined path
    combined_path = os.path.join(base_path, *additional_paths)
    
    # Normalise and return the combined path
    return os.path.normpath(combined_path)


def read_config(config_dir, section, option, arg=None):
    """Reads a configuration file and returns the specified value as the desired data type.

Args:
- config_dir (str): The directory where the configuration file is located.
- section (str): The section of the configuration file where the option is located.
- option (str): The option to retrieve from the configuration file.
- arg (str, optional): The desired data type of the retrieved value. Can be "float", "int", or "tuple". Defaults to None.

Returns:
- If arg is not provided: the value of the specified option as a string.
- If arg is "float": the value of the specified option as a float.
- If arg is "int": the value of the specified option as an integer.
- If arg is "tuple": the value of the specified option as a tuple of integers.

Example Usage:
>>> read_config("config.ini", "database", "port")
'5432'

>>> read_config("config.ini", "database", "port", "int")
5432

>>> read_config("config.ini", "database", "credentials", "tuple")
(123456, 'password')
"""

    if arg == "float":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_float = float(load_config)
        print(f"Config loaded: [ ({option})  = ({config_float}) ] conv to float", "g")

        return config_int
    if arg == "int":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_int = int(load_config)
        print(f"Config loaded: [ ({option})  = ({config_tuple}) ] conv to int", "g")

        return config_int
    
    if arg == "tuple":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_tuple = tuple(map(int, load_config.split(",")))
        print(f"Config loaded: [ ({option})  = ({config_tuple}) ] conv to tuple", "g")

        return config_tuple
    
    else:
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])

        print(f"Config loaded: [ ({option})  = ({load_config}) ]", "g")

        return load_config


def write_config(config_dir, section, Key, option):
    """
Args:
    - config_dir (str): The directory where the configuration file is located.
    - section (str): The section name in the configuration file.
    - Key (str): The key to update or add in the specified section.
    - option (str): The value to assign to the specified key.

Returns:
    - None

Example Usage:
    - Updating an existing key in a section of a configuration file
    >>>  write_config('config.ini', 'section1', 'key1', 'new_value')

    >>>  Adding a new key in a section of a configuration file
    >>>  write_config('config.ini', 'section2', 'key2', 'value2')
"""
    config = ConfigParser()
    # update existing value
    config.read(config_dir)
    try:
        config.add_section(section)
    except:
        pass
    config.set(section, Key,option) #Updating existing entry 
    with open(config_dir, 'w') as configfile:
        config.write(configfile)
    print (f"\nChange settings -> {config_dir}\n[{section}]\n{Key}) = {option}\n")



def Folder_gen(Folder_Name, Folder_dir):
    """Creates a new folder if it does not already exist.

            Args:
            - folder_name (str): The name of the folder to be created.
            - folder_dir (str): The directory in which the folder is to be created.

            Returns:
            - str: The full path of the created folder.

            Example usage :
            >>> Folder_Name = "my_folder"
            >>> Folder_dir = "path/to/parent/directory"
            >>> created_folder_path = Folder_gen(Folder_Name, Folder_dir)
            >>> print("Created folder path:", created_folder_path)
    """

    print("Folder structure is checked and created if necessary...\n")
    folder = Folder_Name
    # Specifies desired file path
    #dir = "~/"+str(Folder_dir)+"/"+str(folder)
    full_path = Folder_dir + os.path.sep + Folder_Name
    # Adds file path with PC user name
    #full_path = os.path.expanduser(dir)
    # Checks file path for exsistance Ture/False
    if os.path.exists(full_path):
        print("Folder structure already exists")
        print("  ->   " + str(full_path))
    else:                                               # Creates folder if not available
        os.makedirs(full_path)
        print(f"The folder [{folder}] was created in the directory:\n  ->   {full_path}")
        print("\n")
    return(os.path.normpath(full_path))


def Create_File(File_name, save_path, Inhalt):
    """Creates a new text file if it does not already exist and fills it with the specified content.

    Args:
    - File_name (str): The name of the text file.
    - save_path (str): The path where the text file should be saved.
    - Content (str): The content to be written to the text file.

    Returns:
    - str: The complete path of the created text file.

    Example usage:
    >>> file_name = "my_text_file.txt"
    >>> save_path = "/path/to/save/directory"
    >>> content = "This is the content of my text file."
    >>> created_file_path = Create_File(file_name, save_path, content)
    >>> print(created_file_path)
    '/path/to/save/directory/my_text_file.txt'
    """

    complete_Path_Text = save_path + os.path.sep + File_name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        # Create file
        file1 = open(complete_Path_Text, "w", encoding='utf-8')
        # toFile = input("Write what you want into the field")                   # File input def.
        # File is filled with input
        file1.write(f"{Inhalt}")
        file1.close()
        print(f"\nfile [{File_name}] is created...with conetnt:\{Inhalt}","b")
        return complete_Path_Text


def Read_File_Out(dir):
    """
    Reads the contents of a file located at the given directory path and returns it as a string.

    Args:
    - dir (str): The directory path of the file to be read.

    Returns:
    - content (str): The contents of the file as a string.

    Example usage:
    >>> file_path = "/path/to/file.txt"
    >>> content = Read_File_Out(file_path)
    >>> print(content)
    'This is the content of the file.'
    """
    with open(dir, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


def copy_image(source_file, dest_file) -> None:
    """Copies an image file from the source path to the destination path.

    Args:
    - source_file (str): The path of the image file to be copied.
    - dest_file (str): The path where the image file should be copied to.

    Returns:
    - file (str) full path of the img

    Raises:
    - IOError: If an error occurs while copying the file.
    
    Example usage:
    >>> source_path = "/path/to/source/image.jpg"
    >>> dest_path = "/path/to/destination/image.jpg"
    >>> copy_image(source_path, dest_path)
    '/path/to/destination/image.jpg'
    """
    try:
        shutil.copy(source_file, dest_file)
        file = dest_file
        print(f"Image [{file}] successfully copied!", "b")
        return file
    except IOError as e:
        print(f"Error when copying the file: {e}", "r")


def File_name_with_time(FileName):
    """Generate a filename with a timestamp.

    Args:
    - FileName (str): The name of the file.

    Returns:
    - FullName (str): The full name of the file with a timestamp in the format of "FileName-DD_MM_YYYY-HH.MM".

    Example usage:
    >>> Datei_name_mit_Zeit("report")
    'report-04_04_2023-15.30'
    """
    Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generates date formater
    FullName = (FileName+"-"+(Date))                           # Generates file name
    return FullName


def TimeStemp():
    """
    Generates a timestamp string in the format of "dd_mm-yyyy_HH:MM:SS".

    Args:
        None

    Returns:
        A string representing the current date and time in the format "dd_mm-yyyy_HH:MM:SS".

    Example Usage:
        >>> TimeStemp()
        '04_04-2023_11:22:33'
    """
    TimeStemp = Date_Time=(time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp


def cheack_config(default_long_Str):
    """
    Generate a config file path in the 'config' directory of the current main file's directory.
    
    Args:
    - default_long_Str (str): A long string representing the default configuration
    
    Returns:
    - config_path (str): The absolute path to the generated config file
    
    Example Usage:
    >>> default_config = "This is the default configuration"
    >>> check_config(default_config)
    '/path/to/main_dir/config/config.ini'
    """
    main_file = sys.modules['__main__'].__file__
    main_dir = os.path.dirname(main_file)
    config_path =  Folder_gen("config", main_dir)
    config_path = Create_File("config.ini", config_path, default_long_Str)
    return config_path

if __name__ == "__funktion__":
    print("__function should not be executed when the file is imported as a module.\nThis was not the case!", "r")
else:
    cheack_config("""[Test]
    abc = 123""")

################################################################################################################################
#def spez.

def add_license(license_path, license_destination_path):
    try:
        # Copy the license file from license_path to license_destination_path
        license_destination_path = license_destination_path+"/LICENSE"
        shutil.copy(license_path, license_destination_path)
        print(f"License successfully copied from {license_path} to {license_destination_path}.")
    except FileNotFoundError:
        print("Error: The specified license file was not found.")
    except PermissionError:
        print("Error: Access denied. Please check permissions.")


def add_text_to_image(img_path_in, img_path_out, font_path, text):
    # Bild laden
    img = Image.open(img_path_in)

    # Zeichenfläche erstellen
    draw = ImageDraw.Draw(img)

    # Schriftart laden
    font_size = 120
    font = ImageFont.truetype(font_path, size=font_size)

    # Textgröße berechnen (ohne draw.textsize)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[:2]

    x_position = 1350
    y_position = 145

    # Text auf das Bild zeichnen

    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    draw.text((x_position +10 , y_position+ 10), text, font=font, fill=(0, 0, 0))
    draw.text((x_position, y_position), text, font=font, fill=(255, 255, 255))
    
    img.save(img_path_out)
    #img.show()


def change_var_in_template(input_str, var_to_change, var_input):
    return re.sub(re.escape(var_to_change), str(var_input), input_str)