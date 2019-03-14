# everything you'll need is imported:
from controller import common
from model.accounting import accounting
from view import terminal_view


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    title = 'Accounting  menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "Which year has the highest profit? (profit = in - out)",
               "What is the average (per item) profit in a given year? [(profit)/(items count)]"]
    exit_message = "Back to main menu"
    title_list = ["ID", "MONTH", "DAY", "YEAR", 'TYPE', 'DURABILITY']
    table = accounting.data_manager.get_table_from_file('model/accounting/items.csv')

    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :')
            updated_table = accounting.add(table, record)
            accounting.data_manager.write_table_to_file('model/accounting/items.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID to remove :')
            updated_table = accounting.remove(table, id_)
            accounting.data_manager.write_table_to_file('model/accounting/items.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID of changed line :')
            record = terminal_view.get_inputs(title_list, 'Please add following informations :')
            updated_table = accounting.update(table, id_, record)
            accounting.data_manager.write_table_to_file('model/accounting/items.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "4":
            label = "Which year has the highest profit?"
            result = str(accounting.which_year_max(table))
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            year = terminal_view.get_inputs(['year : '], 'Please give  a year :')
            year = year[0]
            result = str(accounting.avg_amount(table, year))
            label = "the average (per item) profit in {} ".format(year)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        else:
            terminal_view.print_error_message("There is no such choice.")
