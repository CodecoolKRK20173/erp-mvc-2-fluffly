""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

title_list = ["id", "title", "type", "name", "genre"]
games_list = []
with open("game_stat.txt") as games:
        for line in games:
            games_list.append(line.strip().split('\t'))



columns_count = 0
for item in title_list:
    columns_count += 1

title_lenght = 0
for title in title_list:
    title_lenght += len(title)

max_len = len(title_list[0])
max_len2 = len(title_list[1])
max_len3 = len(title_list[2])
max_len4 = len(title_list[3])
max_len5 = len(title_list[4])

column_width = []
x = int(0)

for item in range(5):
    for game_info in games_list:
        len_item2 = len(game_info[item])
        if len_item2 > max_len[item]:
            max_len2 = len_item2
    column_width.append(max_len2)

print(column_width)

'''


for item in games_list:
    len_item3 = len(item[2])
    if len_item3 > max_len3:
        max_len3 = len_item3
column_width.append(max_len3)

for item in games_list:
    len_item4 = len(item[3])
    if len_item4 > max_len4:
        max_len4 = len_item4
column_width.append(max_len4)

for item in games_list:
    len_item5 = len(item[4])
    if len_item5 > max_len5:
        max_len5 = len_item5
column_width.append(max_len5)

print(column_width)


dash_length = "-" * max(column_width)

print("/" + str(dash_length) + "\\")
print("|" + " " * )

print("|" + str(summ) + "|" + str(splitting[1]) + "|")
print("\\" + str(dash_length) + "/")

'''









 









    # your goes code


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


title = 'Main menu'
list_options = ['Store manager',
                'Human resources manager',
                'Inventory manager',
                'Accounting manager',
                'Sales manager',
                'Customer relationship management (CRM)',
                'Exit program']
exit_message = "Back to main menu"


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print('{}:'.format(title))
    for i in range(len(list_options)):
        print('{}({}) {}'.format('    ', i + 1, list_options[i]))
    print('{}(0) {}'.format('    ', exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    list = []
    print(title)
    for question in list_labels:
        answer = input(question + " ")
        input_list.append(answer)

    return list


def get_choice(title, options, exit_message):
    print_menu(title, options, exit_message)
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print('Error: {}'.format(message))

