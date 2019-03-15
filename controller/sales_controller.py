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
               "What is the id of the item that was sold for the lowest price?",
               "Which items are sold between two given dates? (from_date < sale_date < to_date)"]
    exit_message = "Back to main menu"
    title_list = ["ID", "TITLE", "PRICE", "MONTH", 'DAY', 'YEAR']
    table = sales.data_manager.get_table_from_file('model/sales/sales.csv')
    
    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :', table)
            updated_table = sales.add(table, record)
            sales.data_manager.write_table_to_file('model/sales/sales.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID to remove :', table)
            updated_table = sales.remove(table, id_)
            sales.data_manager.write_table_to_file('model/sales/sales.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID of changed line :', table)
            record = terminal_view.get_inputs(title_list, 'Please add following informations :', table)
            updated_table = sales.update(table, id_, record)
            sales.data_manager.write_table_to_file('model/sales/sales.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "4":
            label = "What is the id of the item that was sold for the lowest price?"
            result = str(sales.get_lowest_price_item_id(table))
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            label = "Which items are sold between two given dates? (from_date < sale_date < to_date)"
            month_from = terminal_view.get_inputs(['Month from'], "Please give starting month.")
            day_from = terminal_view.get_inputs(['Day from'], "Please give starting day.")
            year_from = terminal_view.get_inputs(['Year from'], "Please give starting year.")
            month_to = terminal_view.get_inputs(['Month to'], "Please give ending month.")
            day_to = terminal_view.get_inputs(['Day to'], "Please give ending day.")
            year_to = terminal_view.get_inputs(['Year to'], "Please give ending year.")
            month_from = int(month_from[0])
            day_from = int(day_from[0])  
            year_from = int(year_from[0])
            month_to = int(month_to[0])
            day_to = int(day_to[0])
            year_to = int(year_to[0])
            result = str(sales.get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to))
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice != 0:
            terminal_view.print_error_message("There is no such choice.")
