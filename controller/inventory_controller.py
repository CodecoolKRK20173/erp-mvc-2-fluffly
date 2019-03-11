# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    common.clear()
    title = 'Inventory menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "Which items have not exceeded their durability yet?",
               "What are the average durability times for each manufacturer?"]
    exit_message = "Back to main menu"

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
