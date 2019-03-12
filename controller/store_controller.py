# everything you'll need is imported:
from model.store import store
from view import terminal_view
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
    title = 'Store menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "How many different kinds of game are available of each manufacturer?",
               "What is the average amount of games in stock of a given manufacturer?"]
    exit_message = "Back to main menu"
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    table = store.data_manager.get_table_from_file('model/store/games.csv')
    terminal_view.print_table(table, title_list)
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
            label = "kinds of game are available of each manufacturer"
            result = store.get_counts_by_manufacturers(store.data_manager.get_table_from_file('model/store/games_test.csv'))
            terminal_view.print_result(result, label)
        elif choice == "5":
            manufacturer = terminal_view.get_inputs(['Manufacturer : '], 'Please select  a manufacturer :')
            manufacturer = manufacturer[0]
            result = str(store.get_average_by_manufacturer(store.data_manager.get_table_from_file('model/store/games_test.csv'), manufacturer))
            label = "The average amount of games in stock of {} ".format(manufacturer)
            terminal_view.print_result(result, label)

        else:
            terminal_view.print_error_message("There is no such choice.")