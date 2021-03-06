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
    title_list = ["ID", "TITLE", "MANUFACTURER", "PRICE", "IN STOCK"]
    table = store.data_manager.get_table_from_file('model/store/games.csv')

    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :', table)
            updated_table = store.add(table, record)
            store.data_manager.write_table_to_file('model/store/games.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID to remove :', table)
            updated_table = store.remove(table, id_)
            store.data_manager.write_table_to_file('model/store/games.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID of changed line :', table)
            record = terminal_view.get_inputs(title_list, 'Please add following informations :', table)
            updated_table = store.update(table, id_, record)
            store.data_manager.write_table_to_file('model/store/games.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "4":
            label = "The kinds of game that are available of each manufacturer: "
            result = store.get_counts_by_manufacturers(table)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            manufacturer = terminal_view.get_inputs(['Manufacturer : '], 'Please select a manufacturer :')
            manufacturer = manufacturer[0]
            result = str(store.get_average_by_manufacturer(table, manufacturer))
            label = "The average amount of games in stock of {} ".format(manufacturer)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice != 0:
            terminal_view.print_error_message("There is no such choice.")