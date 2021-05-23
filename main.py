import time
from args_helper import Args
from csv_helper import read_file
from brightness import Brightness
from gui import ForegroundGUI
from event import ForegroundEvent

brightness = Brightness()
global_desired_dict = {}


def window_check(current_window, current_brightness):
    if current_window in global_desired_dict:
        brightness_true = global_desired_dict[current_window]
        if current_brightness != brightness_true:
            brightness.set_brightness(brightness_true)
        if args.verbose:
            print(
                'Same window name detected. Window name: "{}" | Brightness: {}'.format(current_window, brightness_true))
    else:
        if args.verbose:
            print(
                '"{}" does not exist. Setting brightness to default {}'.format(current_window, args.default_brightness))
        brightness.set_brightness(args.default_brightness)


def hook_callback(current_window):
    if args.verbose:
        print("Window returned from hook: {}".format(current_window))
    window_check(current_window, brightness.get_brightness())


def start():
    # Check if hook or timer
    if args.hook:
        if args.verbose:
            print("Method hook used")
        event = ForegroundEvent(hook_callback)
    else:
        if args.verbose:
            print("Method timer used")
        gui = ForegroundGUI()
        while True:
            current_brightness = brightness.get_brightness()
            current_window = gui.get_foreground_window()
            window_check(current_window, current_brightness)
            time.sleep(1)


def start_one(window_name, brightness_true):
    data = {
        window_name: brightness_true,
    }
    global global_desired_dict
    global_desired_dict = data
    start()


def start_file(file_path):
    # Read the file
    data = read_file(file_path)
    global global_desired_dict
    global_desired_dict = data
    start()


a = Args()
a.init()
args = a.get_args()
if args.verbose:
    print(vars(args))

if args.test:
    # Just do printing and do nothing else
    gui = ForegroundGUI()
    while True:
        print(gui.get_foreground_window())
        time.sleep(1)

if args.start:
    # Check if one or file
    if args.one:
        start_one(args.window_name, args.brightness_true)
    elif args.file:
        start_file(args.path)
