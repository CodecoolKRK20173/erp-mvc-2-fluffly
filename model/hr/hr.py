""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    oldest_people = []
    oldest_person_age = table[0][2]
    
    for line in table: 
        if oldest_person_age > line[2]:
            oldest_person_age = line[2]
    
    for line in table:
        if line[2] == oldest_person_age:
            oldest_people.append(line[1]) 

    return oldest_people



def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    sum_of_ages = 0
    amount_of_persons = 0
    ages_list = []
    actual_year = 2019
    closes_to_avg_age_results = []

    for line in table:
        ages_list.append(actual_year - int(line[2]))

    for line in table:
        age = 2019 - int(line[2])
        sum_of_ages += age
        amount_of_persons += 1
    
    average_age = sum_of_ages / amount_of_persons

    find_closest_number = lambda average_age,ages_list:min(ages_list,key=lambda x:abs(x-average_age))

    age_closest_to_avg_age = find_closest_number(average_age, ages_list)
    year_closest_to_avg_was_born = actual_year - age_closest_to_avg_age

    for line in table:
        if line[2] == str(year_closest_to_avg_was_born):
            closes_to_avg_age_results.append(line[1])

    return closes_to_avg_age_results
    