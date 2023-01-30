# import ctypes
import sys
import select
import os

if os.name == "nt":
    import win32event, win32api, msvcrt
    hStdin = win32api.GetStdHandle(win32api.STD_INPUT_HANDLE)

# _kbhit = ctypes.CDLL('./kbhit/kbhit.so')


def check_key():
    # select system call, unix only.
    if os.name == "nt":
        return win32event.WaitForSingleObject(hStdin, 1000) == win32event.WAIT_OBJECT_0 and msvcrt.kbhit()
    else:
        _, w, _ = select.select([], [sys.stdin], [], 0)
        return len(w)