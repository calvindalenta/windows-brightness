| WARNING: These scripts are OS (Windows) specific |
| --- |

# Windows Brightness

These scripts will provide you the functionalities for getting the current window on the foreground and getting and setting your computer's brightness

[Click here if you just want to use the binary](https://github.com/calvindalenta/windows-brightness#binary-usage)

## Dependencies
Before using this script, there are several dependencies that need to be installed. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip install WMI
pip install win32gui
```

## Script Usage

### Brightness
```python
from brightness import Brightness
b = Brightness()
b.get_brightness() # Get the current brightness
b.set_brightness(30) # Percentage [0-100]
```

### Checking foreground window by interval
```python
from brightness import Brightness
from gui import ForegroundGUI
import time

brightness = Brightness()
gui = ForegroundGUI()
interval = 1

while True:
  current_brightness = brightness.get_brightness()
  current_window = gui.get_foreground_window()

  #Your app logic here based on the current brightness and current window

  time.sleep(interval)
```

### Checking foreground window by the callback event
```python
from brightness import Brightness
from event import ForegroundEvent

brightness = Brightness()
event = ForegroundEvent(callback)

def callback(current_window):
  #Your app logic based on current window provided
```

## Binary Usage
The binary can be downloaded on the [release](https://github.com/calvindalenta/windows-brightness/releases) page
### Specify one window to watch
```bash
program.exe start one "Untitled - Notepad" 40
```

### Specify multiple windows to watch
```bash
program.exe start file yourfile.csv
```
The csv file specified should have two columns (without header). The first column is the window name and the second one is the brightness value if true.

See [example.csv](https://github.com/calvindalenta/windows-brightness/blob/master/example.csv) for reference

### Specify default brightness if all the windows specified don't exist
```bash
program.exe start -d 40 one "Untitled - Notepad" 40
program.exe start -d 40 file yourfile.csv
```

### If you just want to see what's your current window
```bash
program.exe test
```
