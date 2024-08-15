pip install pyinstaller
mkdir build
cd build
pyinstaller --onefile ../main.py --icon ../icon.png --name EyeTerminal
rm -r build
rm -r EyeTerminal.spec
pyinstaller --onefile ../crashlog.py --icon ../icon.png --name CrashLog
rm -r build
rm -r CrashLog.spec
ren dist builded
cd builded
mkdir log
mkdir plugin
touch config.cfg
touch plugin.cfg
clear
echo Please don't forget copy folder plugin, folder log, and files config.cfg, plugin.cfg