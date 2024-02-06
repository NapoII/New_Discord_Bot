from util.__funktion__ import *
import pyautogui
import sys
from datetime import datetime


def add_image_to_markdown(Alt_Text, path, link):
    """
    Returns a Markdown-formatted string that displays an image with a link.

    Parameters:
    - Alt_Text (str): The alternative text for the image.
    - path (str): The file path of the image.
    - link (str): The URL that the image should link to.

    Returns:
    - str: A string containing the Markdown-formatted code for the image with a link.
    """
    add_imge_code = f"[![{Alt_Text}]({path})]({link})"
    return add_imge_code

def readme_gen (name, save_path, Readme_top, readme_img_folder, config_dir, font_path):

    date_str = datetime.now().strftime("%d.%B.%Y")
    Full_readme_str =""
    Git_owner = read_config(config_dir, "readme", "github_user")
    repro_Git_owner = Git_owner
    discord_link = read_config(config_dir, "readme", "discord_link")
    discord_ID = read_config(config_dir, "readme", "discord_ID")
    Description = pyautogui.prompt(text='Description von der Repro', title='README.md' , default="Coming soon...")
    py_version = sys.version.split()[0]

    path_banner_img = copy_image(Readme_top, readme_img_folder)

    add_text_to_image(Readme_top, f"{readme_img_folder}\Readme_top.png", font_path,  name)

    path_banner_img += os.path.sep + "Readme_top.png"
    readme_code = ""

    readme_code += add_image_to_markdown(f"github/{Git_owner}/{name}", f"https://raw.githubusercontent.com/{Git_owner}/{name}/main/README_img/Readme_top.png", f"https://github.com/{Git_owner}/{name}")+"\n"

    badge_line = ""

    Alt_text = f"downloads/total"
    path_img = f"https://img.shields.io/github/downloads/{Git_owner}/{name}/total"
    link_img = f"https://github.com/{Git_owner}/{name}/archive/refs/heads/main.zip"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/repo-size"
    path_img = f"https://img.shields.io/github/repo-size/{Git_owner}/{name}"
    link_img = f"https://github.com/{Git_owner}/{name}/archive/refs/heads/main.zip"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/license"
    path_img = f"https://img.shields.io/github/license/{Git_owner}/{name}"
    link_img = f"https://github.com/{Git_owner}/{name}/blob/main/LICENSE"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/last-commit" 
    path_img = f"https://img.shields.io/github/downloads/{Git_owner}/{name}/total"
    link_img = f"https://img.shields.io/github/issues/{Git_owner}/{name}?style=plastic"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/issues_open"
    path_img = f"https://img.shields.io/github/issues/{Git_owner}/{name}?style=plastic"
    link_img = f"https://img.shields.io/github/issues-raw/{Git_owner}/{name}"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/stars"
    path_img = f"https://img.shields.io/github/stars/{Git_owner}/{name}?style=social"
    link_img = f"https://github.com/{Git_owner}/{name}/stargazers"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"discord"
    path_img = f"{discord_link}"
    link_img = f"https://img.shields.io/discord/{discord_ID}"
    badge_line += add_image_to_markdown(Alt_text, link_img, path_img) + "\n"

    readme_code += badge_line +"\n"
    readme_code += Description +"\n"

    Table_of_Contents ="""## 📝 Table of Contents
+ [Demo / Working](#demo)
+ [Install](#usage)
+ [How it works](#Use)
+ [Buy me a coffee](#coffee)
+ [LICENSE](#LICENSE)"""

    readme_code += Table_of_Contents +"\n"

    rest_fill = f"""## 🎥 Demo / Working <a name = "demo"></a>
coming soon...

## 💻 Install <a name = "usage"></a>
```cmd
git clone https://github.com/{Git_owner}/{name}
pip install -r requirements.txt
```
## 💭 How it works <a name = "Use"></a>

start {name}.py directly from the folder or run in cmd:
```cmd
cd <local path of {name}>
python {name}.py
```

## ☕ Buy me a coffee <a name = "coffee"></a>

Feel free to show your appreciation by treating me to a virtual coffee. Your support means a lot and keeps the creative coding vibes going! 🚀

<a href='https://ko-fi.com/M4M0TS4ZM' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## 📚 LICENSE <a name = "LICENSE"></a>

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)

[{name}]({name}) was created on {date_str} by [{Git_owner}](https://github.com/{Git_owner})


    """
    readme_code += rest_fill +"\n"

    nice_end = """<p align="center">
<img src="https://raw.githubusercontent.com/NapoII/NapoII/233630a814f7979f575c7f764dbf1f4804b05332/Bottom.svg" alt="Github Stats" />
</p>
"""
    readme_code += nice_end
    Create_File("README.md", save_path, readme_code)
    return save_path