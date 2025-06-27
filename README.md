# mBot-Hap
## About
With **mBot-Hap** you can steer an [mBot robot](https://www.makeblock.com/pages/mbot-robot-kit) with a gamepad.

## What you need
- A computer. It's not tested on non-Windows computers, but it might work... 
- An mBot with a 2.4GHz-dongle (or coding skills to make this code work with a bluetooth version, or with another type of robot)
- A usb game controller like [this one](https://www.kabelshop.nl/Gembird-Controller-pc-Gembird-2-controllers-USB-Vibratie-D-pad-10-knoppen-2-joysticks-JPD-UDV2-01-i24279-t1437173.html) (or coding skills to make it work with other controllers)
## Get it running
- Download this repository as a zip file, **unblock** the zip file and extract it
- Install [Python 3.13](https://www.python.org/)
- Install the following Python libraries:
```
pip install cython
pip install pyserial
pip install hidapi
pip install pygame 
```

- **NOTE** - On Windows, pip.exe is usually installed in *C:\Users\YourUserName\AppData\Local\Programs\Python\Python311\Scripts\pip.exe* (change *YourUserName* and Python version) and might be added to the path. If pip is not recognized, add its folder to your PATH environment variable, or adapt and run the helper script **install_libs.bat**
- Connect the game controller and the mBot 2.4GHz dongle
- Switch to the **src** directory and run **mbot-controller.py**:
```
python mbot-controller.py
```
- **NOTE** - On Windows, python.exe is usually installed in *C:\Users\YourUserName\AppData\Local\Programs\Python\Python312\python.exe* (change *YourUserName* and Python version) and might be added to the path. If python is not recognized, add its folder to your PATH environment variable, or adapt and run the helper script **run.bat**

- **NOTE** - On Windows, running python.exe might launch the Microsoft Store App. If so, use the Windows search bar to find "Manage app execution aliases" and disable the python aliases.

## Controlling the mBot
Turn on the **Analog**-mode of the usb controller
- **Button 'Select'** - Switch steering mode
- **Joysticks** - Drive the mBot (depending on the steering mode)