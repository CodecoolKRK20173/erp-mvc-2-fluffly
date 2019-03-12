""" Common functions for controllers
implement commonly used functions here
"""
import time
import os
from model import data_manager

def clear(delay=0.5):
    time.sleep(delay)
    os.system("clear")


def exit_prompt():
    print('')
    input('Press enter.')
    

def get_table():
    return data_manager.get_table_from_file()