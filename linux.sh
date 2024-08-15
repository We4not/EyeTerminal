pip install pyinstaller
mkdir build
cd build
pyinstaller --onefile ../main.py --icon ../icon.png --name EyeTerminal
rm -r build
rm -r EyeTerminal.spec
rm -r build
ren dist builded
cd builded
mkdir log
touch config.cfg