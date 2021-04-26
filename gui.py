from win32gui import GetWindowText, GetForegroundWindow

class ForegroundGUI():

    def get_foreground_window(self):
        return GetWindowText(GetForegroundWindow())