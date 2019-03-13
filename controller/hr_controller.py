# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    title = 'HR menu'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table.",
               "Who is the oldest person?",
               "Who is the closest to the average age?"]
    exit_message = "Back to main menu"

    title_list = ["id", "name", "birth_year"]
    table = hr.data_manager.get_table_from_file('model/hr/persons.csv')
    # terminal_view.print_table(table, title_list)

    choice = None
    while choice != "0":
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            result = hr.get_oldest_person(table)
            label = "Who is the oldest person?"
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        elif choice == "5":
            result = hr.get_persons_closest_to_average(table)
            label = "Who is the closest to the average age?"
            terminal_view.print_result(result, label)
            common.exit_prompt()
            common.clear()
        else:
            terminal_view.print_error_message("There is no such choice.")
