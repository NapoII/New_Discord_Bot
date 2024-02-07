[![github/NapoII/New_Discord_Bot](https://raw.githubusercontent.com/NapoII/New_Discord_Bot/main/README_img/Readme_top.png)](https://github.com/NapoII/New_Discord_Bot)
[![github/repo-size](https://img.shields.io/github/repo-size/NapoII/New_Discord_Bot)](https://github.com/NapoII/New_Discord_Bot/archive/refs/heads/main.zip) [![github/license](https://img.shields.io/github/license/NapoII/New_Discord_Bot)](https://github.com/NapoII/New_Discord_Bot/blob/main/LICENSE) [![github/issues_open](https://img.shields.io/github/issues/NapoII/New_Discord_Bot?style=plastic)](https://img.shields.io/github/issues-raw/NapoII/New_Discord_Bot) [![github/stars](https://img.shields.io/github/stars/NapoII/New_Discord_Bot?style=social)](https://github.com/NapoII/New_Discord_Bot/stargazers) [![discord](https://img.shields.io/discord/190307701169979393)](https://discord.gg/knTKtKVfnr)

This Python program is your ultimate ticket to unleashing the power of Discord bots with sheer ease and excitement! 🎉 Designed to be the turbocharged engine for your Discord bot dreams, it's powered by the sleek Discord.py library. 🚀💥

Say goodbye to the mundane setup process! With just a few clicks, you'll dive into a mesmerizing world of possibilities. 🌟 This program swiftly crafts a vibrant template, complete with a meticulously organized folder structure and dazzling cogs. 📁💫

Ready to embark on your bot-building adventure? Let's soar to new heights together! 🚀🌈

## 📝 Table of Contents
+ [Demo / Working](#demo)
+ [Install](#usage)
+ [How it works](#Use)
+ [Buy me a coffee](#coffee)
+ [LICENSE](#LICENSE)
## 🎥 Demo / Working <a name = "demo"></a>
The following folder structure will be created:
```folder
Test_example/
┣ README_img/
┃ ┣ discord_bot.gif
┃ ┣ discord_bot.ico
┃ ┣ Readme_top.png
┃ ┣ Readme_top.psd
┃ ┗ Readme_top.raw.png
┣ Test_example/
┃ ┣ config/
┃ ┃ ┣ config.ini
┃ ┃ ┗ token.ini
┃ ┣ discord_cogs/
┃ ┃ ┗ admin/
┃ ┃   ┣ pre_setup.py
┃ ┃   ┗ say.py
┃ ┣ util/
┃ ┃ ┣ __funktion__.py
┃ ┃ ┗ __Mydiscord_funktions__.py
┃ ┗ Test_example.py
┣ .gitignore
┣ LICENSE
┣ README.md
┣ requirements.txt
┗ ToDo.md
```
After [set up the config](#usage), the first start of the bot will create the required channel.

![💻-bot-cmd](/README_img/new_channel.png)

And informs you what he has done and what you still have to set on the discord

![💻-bot-cmd](/README_img/first_setup_msg.png)

Every time you start the bot from now on, it will show you which Git status it is currently running on and when it was started

![💻-bot-cmd](/README_img/start_status.png)

In the template folder you will find useful examples of how you can programme things with [Discord.py](https://discordpy.readthedocs.io/en/stable/)

## 💻 Install <a name = "usage"></a>
1. Clone the Git
```cmd
git clone https://github.com/NapoII/New_Discord_Bot
pip install -r requirements.txt
```
2. Fill in the required configs:
  
`config/token.ini`
```config
[discord]
discord_bot_name = 
token = 
application_id = 
```

`config/config.ini`
```config
[client]
guild_name = 
guild_id = 
activity = "Hello World"
praefix = !
```
The *channel ID*s do not have to be entered, the bot does this automatically the first time it is started, unless you want to predetermine certain channels.

3. You can now build your Discord Bot on the template have fun.
4. Tell me thank you with a [coffee](#coffee)
*Dont forget the templates are unter the* [GNU GENERAL PUBLIC LICENSE Version 3 LICENSE](.\[New_Discord_Bot]\LICENSE). So you also have to make your Discord bot public, like I do with the templates

create a new repository on the command line
```cmd
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/{your_git_hub_name}/{prjekt_name}.git
git push -u origin main
```
…or push an existing repository from the command line
```cmd
git remote add origin https://github.com/{your_git_hub_name}/{prjekt_name}.git
git branch -M main
git push -u origin main
```

## 💭 How it works <a name = "Use"></a>

start [New_Discord_Bot.py](.\[New_Discord_Bot]\New_Discord_Bot\New_Discord_Bot.py) directly from the [folder](.\[New_Discord_Bot]\New_Discord_Bot) or run in cmd:
```cmd
cd <local path of New_Discord_Bot>
python New_Discord_Bot.py
```

## ☕ Buy me a coffee <a name = "coffee"></a>

Feel free to show your appreciation by treating me to a virtual coffee. Your support means a lot and keeps the creative coding vibes going! 🚀

<div style="text-align:center;">
    <a href="https://ko-fi.com/napo_ii"><img src="/README_img/kofi.gif" alt="Buy me a coffee" width="200" height="auto"></a>
</div>



## 📚 LICENSE <a name = "LICENSE"></a>

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)

[New_Discord_Bot](New_Discord_Bot) was created on 28.January.2024 by [NapoII](https://github.com/NapoII)


    
<p align="center">
<img src="https://raw.githubusercontent.com/NapoII/NapoII/233630a814f7979f575c7f764dbf1f4804b05332/Bottom.svg" alt="Github Stats" />
</p>
