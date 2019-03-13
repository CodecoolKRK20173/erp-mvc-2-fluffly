""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table=None):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    letter1 = random.choice('abcdefghijklmnopqrstuvwxyz')
    letter2 = random.choice('abcdefghijklmnopqrstuvwxyz')
    capital_letter1 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    capital_letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_character1 = random.choice('!#$%&*+-<?@^_~')
    special_character2 = random.choice('!#$%&*+-<?@^_~')

    id_raw = (str(number1) + str(number2) + special_character1 + letter1 + capital_letter1 + letter2 + special_character2 + capital_letter2)
    id_finall = ''.join(random.sample(id_raw, len(id_raw)))

    return id_finall

    '''open_file = open(file_name, "r")
    with open_file as f:
        for i, x in enumerate(f, 1):
            line = x.split(";")
            if line[0] == file_name[0]:
               return i
               break'''  # jeszcze nie zrobione, zignorujcie

def sum_position_by_ind(table, table_index):

    sum_pos = 0
    for i in range(len(table)):
        sum_pos += float(table[i][table_index])


def sum_position(table):

    sum_pos = 0
    for i in range(len(table)):
        sum_pos += float(table[i])

    return sum_pos


def get_index_by_element(table, element):
    
    start = 0
    search_res = False

    while start < len(table) and search_res is False:
        if table[start] == element:
            search_res = True
        else:
            start = start + 1

    return start
