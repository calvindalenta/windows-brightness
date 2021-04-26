# https://stackoverflow.com/questions/4407631/is-there-windows-system-event-on-active-window-changed

import sys
import time
import ctypes
import ctypes.wintypes

class ForegroundEvent():

    EVENT_SYSTEM_DIALOGSTART = 0x0010
    EVENT_FOCUS = 0x8005
    EVENT_SYSTEM_FOREGROUND = 0x0003
    WINEVENT_OUTOFCONTEXT = 0x0000

    user32 = ctypes.windll.user32
    ole32 = ctypes.windll.ole32

    hook = None

    user_callback = None

    def __init__(self, user_callback):
        self.user_callback = user_callback

        self.ole32.CoInitialize(0)

        WinEventProcType = ctypes.WINFUNCTYPE(
            None,
            ctypes.wintypes.HANDLE,
            ctypes.wintypes.DWORD,
            ctypes.wintypes.HWND,
            ctypes.wintypes.LONG,
            ctypes.wintypes.LONG,
            ctypes.wintypes.DWORD,
            ctypes.wintypes.DWORD
        )

        WinEventProc = WinEventProcType(self.callback)

        self.user32.SetWinEventHook.restype = ctypes.wintypes.HANDLE
        self.hook = self.user32.SetWinEventHook(
            self.EVENT_FOCUS,
            self.EVENT_FOCUS,
            0,
            WinEventProc,
            0,
            0,
            self.WINEVENT_OUTOFCONTEXT
        )
        if self.hook == 0:
            print('SetWinEventHook failed')
            sys.exit(1)

        msg = ctypes.wintypes.MSG()
        while self.user32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
            self.user32.TranslateMessageW(msg)
            self.user32.DispatchMessageW(msg)

    def callback(self, hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
        length = self.user32.GetWindowTextLengthA(hwnd)
        buff = ctypes.create_string_buffer(length + 1)
        self.user32.GetWindowTextA(hwnd, buff, length + 1)
        if buff.value:
            #print(buff.value)
            try:
                string = buff.value.decode(encoding='utf-8')
                self.user_callback(string)
            except UnicodeDecodeError:
                print("Error decoding string: {}".format(buff.value))

    def __del__(self):
        self.user32.UnhookWinEvent(self.hook)
        self.ole32.CoUninitialize()

