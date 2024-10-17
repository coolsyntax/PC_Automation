import ctypes
import subprocess
import winshell
import time
from voice_engine import speak


def lock_window():
    speak("Locking the device")
    ctypes.windll.user32.LockWorkStation()


def shutdown_system():
    speak("Hold On a Sec! Your system is on its way to shut down")
    subprocess.call('shutdown / p /f')


def empty_recycle_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    speak("Recycle Bin Recycled")


def restart_system():
    speak("Restarting the system")
    subprocess.call(["shutdown", "/r"])


def log_off():
    speak("Make sure all the applications are closed before sign-out")
    time.sleep(5)
    subprocess.call(["shutdown", "/l"])
