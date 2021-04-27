
# desired_window = ['Untitled - Notepad']
# desired_brightness = 50 # Percentage [0-100] For changing the screen
#
# def window_check(current_window, current_brightness):
#   if current_window in desired_window:
#     if current_brightness != desired_brightness:
#       brightness.set_brightness(desired_brightness)
#   else:
#     if current_brightness != 0:
#       brightness.set_brightness(10)

"""
Use the code below if you want to check the foreground window based on time interval
"""
# from brightness import Brightness
# from gui import ForegroundGUI
# import time
#
# brightness = Brightness()
# gui = ForegroundGUI()
#
# while True:
#   current_brightness = brightness.get_brightness()
#   current_window = gui.get_foreground_window()
#
#   window_check(current_window, current_brightness)
#
#   print(current_window)
#   time.sleep(1)

"""
Use the code below if you want to check the foreground window based on hook callback
"""
# from brightness import Brightness
# from event import ForegroundEvent
#
# brightness = Brightness()
# event = ForegroundEvent(callback)
#
# def callback(current_window):
#   print(current_window)
#   window_check(current_window, brightness.get_brightness())