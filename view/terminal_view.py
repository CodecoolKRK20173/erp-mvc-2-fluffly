""" Terminal view module """
from model import common


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
    table.insert(0, title_list)
    
    len_col = []
    x = 0
    for i in table:
        len_col.append([])
        for j in range(len(i)):
            longest_name = len(i[j])
            len_col[x].append(longest_name)
        x += 1

    max_line_len = []
    for i in range(len(title_list)):
        max_line_len.append([])
        for k in len_col:
            max_line_len[i].append(k[i])

    max_line_len = [(max(i)) for i in max_line_len]
    max_line = common.sum_position(max_line_len)

    dashed_line = ("═" * int(max_line + 1 + len(title_list)))
    head = [(title_list[q].rjust(max_line_len[q])+'│') for q in range(len(title_list))]
    header = '│' + ''.join(head)
    table.pop(0)
    print(dashed_line)
    print(header)
    print(dashed_line)
    for i in table:
        body_list = [(i[q].rjust(max_line_len[q])+'│') for q in range(len(i))]
        body = '│' + ''.join(body_list)
        print(body)
    print(dashed_line)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if isinstance(result, dict):
        print('{0:>35}'.format(label))
        to_print_a = [[i[0], i[1]] for i in result.items()]
        to_print_b = [('{0:>35} : {1:>1}'.format(i[0], i[1])) for i in to_print_a]
        [print(i) for i in to_print_b]
    
    elif isinstance(result, list):
        if isinstance(result[0], list):
            print('{0:>20}'.format(label))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    result[i][j] = str(result[i][j])
            for i in result:
                body_list = [('{0:^21}-'.format(i[q])) for q in range(len(i))]
                body = '-' + ''.join(body_list)
                print(body)
        else:
            print('{0:>20}'.format(label))
            [print('{0:>20}'.format(i)) for i in result]
    
    elif isinstance(result, str):
        print('{} : {}'.format(label, result))


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


def get_inputs(list_labels, title, table=None):
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
    headers = ["ID", "MONTH", "DAY", "YEAR", "BIRTH YEAR", "PURCHASE YEAR", "PRICE", "IN STOCK", "DURABILITY"]

    head = ['TYPE', "SUBSCRIBED"]
    input_list = []
    print(title)
    for question in list_labels:
        if question == headers[0]:
            answer = common.generate_random(table)
            input_list.append(answer)
        elif question in headers[0:(len(headers)+1)]:
            answer = input(question + " ")
            if answer.isnumeric():
                input_list.append(answer)
            else:
                command = True
                while command:
                    print('Please give a number.')
                    answer = input(question + " ")
                    if answer.isnumeric():
                        command = False
                input_list.append(answer)
        elif question in head[0]:
            answer = input(question + " ")
            if answer in ['in', 'out']:
                input_list.append(answer)
            else:
                command = True
                while command:
                    print('Please give in/out.')
                    answer = input(question + " ")
                    if answer in ['in', 'out']:
                        command = False
                input_list.append(answer)
        elif question in head[1]:
            answer = input(question + " ")
            if answer in ['0', '1']:
                input_list.append(answer)
            else:
                command = True
                while command:
                    print('Please give 0/1.')
                    answer = input(question + " ")
                    if answer in ['0', '1']:
                        command = False
                input_list.append(answer)
        else:
            answer = input(question + " ")
            input_list.append(answer)

    return input_list


def get_choice(title, options, exit_message, table=None):
    print_menu(title, options, exit_message)
    inputs = get_inputs(["Please enter a number: "], "", table)
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

