# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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
    title = 'CRM menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "What is the id of the customer with the longest name?",
               "Which customers has subscribed to the newsletter?"]
    exit_message = "Back to main menu"

    title_list = ["ID", "NAME", "EMAIL", "SUBSCRIBED"]
    table = crm.data_manager.get_table_from_file('model/crm/customers.csv')

    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            record = terminal_view.get_inputs(title_list, 'Please add following informations :')
            updated_table = crm.add(table, record)
            crm.data_manager.write_table_to_file('model/crm/customers.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "2":
            id_ = terminal_view.get_inputs(['Id'], 'Please give ID to remove :')
            updated_table = crm.remove(table, id_)
            crm.data_manager.write_table_to_file('model/crm/customers.csv', updated_table)
            common.exit_prompt()
            common.clear()
        elif choice == "3":
            pass
        elif choice == "4":
            label = "The id of the customer with the longest name is: "
            result = crm.get_longest_name_id(table)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            label = "Customers that has been subscribed to the newsletter: "
            result = crm.get_subscribed_emails(table)
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        else:
            terminal_view.print_error_message("There is no such choice.")
