""" Common functions for controllers
implement commonly used functions here
"""
import time
import os


def clear(delay=0.5):
    time.sleep(delay)
    os.system("clear")

