""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    common.remove(table, id_)
    table = add(table, record)

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    longest_name = 0
    longest_names_list = []
    alphabetically_ordered_names_list = []


    for line in table:
        if len(line[1]) > longest_name:
            longest_name = len(line[1])

    for line in table:
        if len(line[1]) == longest_name:
            longest_names_list.append([line[1], line[0]])

    for name in range(len(longest_names_list)-1,0,-1):
        for i in range(name):
            if longest_names_list[i] > longest_names_list[i+1]:
                temp = longest_names_list[i]
                longest_names_list[i] = longest_names_list[i+1]
                longest_names_list[i+1] = temp

    return longest_names_list[-1][-1]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subs_list = []
    for item in table:
        is_y_or_no = int(item[3])
        if is_y_or_no == 1:
            subs_list.append(item[2] + ";" + item[1])

    return subs_list
