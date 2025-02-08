# EyeTerminal
EyeTerminal - a console program, created just for fun.

## Commands
- `clear` - clear from screen
- `exit` - exit from program
- `echo [TEXT]` - prints the line
- `version` - shows current version
### Default package
- `calc [NUM1] [OPERATOR] [NUM2]` - calculator

## Update list
|Version|  Description  |
|-------|---------------|
| v1.0b | First version |
| v1.0  |     N/A       |
-------------------------

## How to build
Usually after changing the source code, this question arises. Let's try to build it.

To do this you need to install the auto-py-to-exe package
```
pip3 install auto-py-to-exe
```
Next we need to open using this command
```
auto-py-to-exe
```
Follow the steps
```
Script Location:
<path to main.py>

Onefile:
One File

Console Window:
Console Based

Icon:
<path to icon.png>

Additional Files:
-> Add Folder
    <path to packages folder>

Advanced:
    --name EyeTerminal
```
$${\color{red}Before\space we\space build,\space we\space need\space to\space check\space that\space everything\space is\space exactly\space as\space it\space should\space be!}$$

After that, scroll down and click on the `Convert .py to .exe` button

After the build, we need to copy folder `cfg`, folder `packages`, and file `icon.png` to the new `output` folder that appears.

Tadam! We got it, the program works

## How to create your own package
First of all, you need to create a folder in `packages` and name the package (for example, let's call it helloworld)
```
mkdir helloworld
```
Next, go to the folder and create a file `core.py`
```
cd helloworld
touch core.py
```
After that we need to write some code, for example we will write a package that prints `Hello world` at the start of startup. The syntax will look like this
``` python
def main(args):
    print("Hello world")
```
`args` is a variable that contains an array of arguments.
For example, we can get the value of the first argument.
In EyeTerminal it will look like this
```
 $ helloworld 23
```
The array will look like this
```
['23']
```
However as a string it won't work
```
 $ helloworld "Hello world"
```
```
['"Hello', 'world"']
```
It is important to note that `args` MUST be inserted, otherwise there will be errors