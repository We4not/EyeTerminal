@echo off
pip install pyinstaller
mkdir build
cd build
pyinstaller --onefile ../main.py --icon ../icon.png --name EyeTerminal
rmdir /S build
del EyeTerminal.spec
pyinstaller --onefile ../crashlog.py --name CrashLog --icon ../icon.png
rmdir /S build
del CrashLog.spec
ren dist builded
cd builded
mkdir log
mkdir plugin
NUM> config.cfg
NUM> plugin.cfg
NUM> README.txt
echo If you can't run the EyeTerminal.exe, you need a writting full parameters in config.cfg and plugin.cfg, copy config.cfg and plugin.cfg in the build/builded>>README.txt
cls
echo Please don't forget copy files config.cfg and plugin.cfg in the build/builded
pause