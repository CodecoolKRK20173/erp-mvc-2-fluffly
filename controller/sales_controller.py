# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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
    title = 'Sales menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "Question: What is the id of the item that was sold for the lowest price?",
               "Which items are sold between two given dates? (from_date < sale_date < to_date)"]
    exit_message = "Back to main menu"
    title_list = ["id", "title", "price", "month", 'day', 'year']
    table = sales.data_manager.get_table_from_file('model/sales/sales.csv')
    
    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :')
            updated_table = sales.add(table, record)
            sales.data_manager.write_table_to_file('model/sales/sales.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['ID'], 'Please give ID to remove :')
            updated_table = sales.remove(table, id_[0])
            sales.data_manager.write_table_to_file('model/sales/sales.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
