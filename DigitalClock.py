from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")


def get_time():
    tim = time.strftime("%I:%M:%S %p")
    clock.config(text=tim)
    clock.after(200, get_time)


clock = Label(master, font=("Ariel", 90), bg="black", fg="white")
clock.pack()

get_time()
