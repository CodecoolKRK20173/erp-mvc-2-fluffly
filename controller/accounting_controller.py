# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
    title = 'Accounting  menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "Which year has the highest profit? (profit = in - out)",
               "What is the average (per item) profit in a given year? [(profit)/(items count)]"]
    exit_message = "Back to main menu"
    title_list = ["id", "month", "day", "year", 'type', 'durability']
    table = accounting.data_manager.get_table_from_file('model/accounting/items.csv')
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
            label = "Which year has the highest profit?"
            result = str(accounting.which_year_max(accounting.data_manager.get_table_from_file('model/accounting/items.csv')))
            terminal_view.print_result(result, label)
        elif choice == "5":
            year = terminal_view.get_inputs(['year : '], 'Please give  a year :')
            year = int(year[0])
            result = str(accounting.avg_amount(accounting.data_manager.get_table_from_file('model/accounting/items.csv'), year))
            label = "the average (per item) profit in {} ".format(year)
            terminal_view.print_result(result, label)
        else:
            terminal_view.print_error_message("There is no such choice.")
