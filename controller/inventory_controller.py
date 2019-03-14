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
    title_list = ["ID", "NAME", "MANUFACTURER", "PURCHASE YEAR", 'DURABILITY']
    table = inventory.data_manager.get_table_from_file('model/inventory/inventory.csv')

    choice = None
    
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :')
            updated_table = inventory.add(table, record)
            inventory.data_manager.write_table_to_file('model/inventory/inventory.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID to remove :')
            updated_table = inventory.remove(table, id_)
            inventory.data_manager.write_table_to_file('model/inventory/inventory.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            pass
        elif choice == "4":
            label = "The items that have not exceeded their durability yet: "
            result = inventory.get_available_items(table)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            label = "What are the average durability times for each manufacturer?"
            result = inventory.get_average_durability_by_manufacturers(table)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        else:
            terminal_view.print_error_message("There is no such choice.")
