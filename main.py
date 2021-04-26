import time
from brightness import Brightness
from gui import ForegroundGUI
from event import ForegroundEvent

desired_window = ['Untitled - Notepad']
desired_brightness = 50 # percentage [0-100] For changing the screen

def window_check(current_window, current_brightness):
  if current_window in desired_window:
    if current_brightness != desired_brightness:
      brightness.change_brightness(desired_brightness)
  else:
    if current_brightness != 0:
      brightness.change_brightness(10)

def callback(window_title):
  print(window_title)
  window_check(window_title, brightness.get_current_brightness())

brightness = Brightness()
#gui = ForegroundGUI()
event = ForegroundEvent(callback)
# while True:
#   current_brightness = brightness.get_current_brightness()
#   current_window = gui.get_foreground_window()
#
#   window_check(current_window, current_brightness)
#
#   print(current_window)
#   time.sleep(1)
  