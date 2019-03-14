""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common



def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """

    table.append(record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    

    return common.remove(table, id_)


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """
    
    remove(table, int(id_))
    table.insert(int(id_), record)

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    years = []
    year = table[0][3]
    years.append(year)

    for line in table:
        year = line[3]
        if year not in years:
            years.append(year)

    dict_of_years = { i : 0 for i in years }

    for line in table:
        if line[3] in dict_of_years:
            if line[4] == "in":
                dict_of_years[line[3]] += int(line[5])
            elif line[4] == "out":
                dict_of_years[line[3]] -= int(line[5])

    highest_profit = int(max(dict_of_years, key=lambda k: dict_of_years[k]))


    return highest_profit




def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    sum_of_outcome = 0
    sum_of_income = 0
    items_count = 0

    for line in table:
        if int(line[3]) == int(year):
            items_count += 1
            if line[4] == "out":
                sum_of_outcome += int(line[5])
            elif line[4] == "in":
                sum_of_income += int(line[5])
        
    profit = sum_of_income - sum_of_outcome
    number = profit / items_count

    return number
