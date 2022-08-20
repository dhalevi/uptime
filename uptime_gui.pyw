# system uptime applet
"""A System Up Time applet - show uptime in a small window."""

# using core libraries only
from tkinter import Tk, mainloop
from tkinter.ttk import Label
import ctypes
from socket import gethostname

# Use a global window
ROOT = Tk()
ROOT.title('Up Time')
LBL = Label(ROOT, font=("Lucida Console", 14))
LBL.pack(anchor='center', ipady=20)


def stamp(val, stamp_str):
    """For val = 1, return 'stamp '. otherwise, return 'stamps'."""
    if val == 1:
        return f"{stamp_str} "
    return f"{stamp_str}s"


def get_uptime_seconds():
    """get current time message."""
    # getting the library in which GetTickCount64() resides
    lib = ctypes.windll.kernel32
    # calling the function and storing the return value
    my_time = lib.GetTickCount64()
    # since the time is in milliseconds i.e. 1000 * seconds
    # therefore truncating the value
    my_time = int(str(my_time)[:-3])
    return my_time


def uptime():
    """Calculate uptime as a string. Self calling label update of uptime."""
    uptime_sec = get_uptime_seconds()
    days, remainder = divmod(uptime_sec, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    s_d = stamp(days, "Day")
    s_h = stamp(hours, "Hour")
    s_m = stamp(minutes, "Minute")
    s_s = stamp(seconds, "Second")
    host_name = gethostname()
    string = f"  {host_name} Is Up for:  {days:>2} {s_d}, {hours:>2} {s_h}, "
    string += f"{minutes:>2} {s_m}, {seconds:>2} {s_s} "
    LBL.config(text=string)
    LBL.after(1000, uptime)


def main():
    """Do it. The main program."""
    uptime()
    mainloop()


if __name__ == '__main__':
    main()
