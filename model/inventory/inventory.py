""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    # your code

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

    # your code

    return table


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

    # your code

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    list_of_actual_items = []
    actual_year = 2017

    for line in table:
        if (int(line[3]) + int(line[4])) >= actual_year:
            list_of_actual_items.append(line)

    for line in list_of_actual_items:
        line[3] = int(line[3])
        line[4] = int(line[4])

    return list_of_actual_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    list_of_manufacturers_names = []

    for line in table: 
        if line[2] not in list_of_manufacturers_names:
            list_of_manufacturers_names.append(line[2])

    dict_of_no_of_times_inthetable = { i : 0 for i in list_of_manufacturers_names }
    dict_of_durability = { i : 0 for i in list_of_manufacturers_names }

    for line in table:
        if line[2] in dict_of_no_of_times_inthetable:
            dict_of_no_of_times_inthetable[line[2]] += 1

    for line in table:
        if line[2] in dict_of_durability:
            dict_of_durability[line[2]] += int(line[4])

    dict_with_divided_values = {k: dict_of_durability[k] / dict_of_no_of_times_inthetable[k] for k in dict_of_no_of_times_inthetable if k in dict_of_durability}

    for key, value in dict_with_divided_values.items():
        if value.is_integer():
            dict_with_divided_values[key] = int(value)

    return dict_with_divided_values
    