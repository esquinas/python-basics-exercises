def get_largest_number(numbers):
    """Gets the largest number from the list received.

    You CANNOT use `max` built-in method.

    :param numbers: List containing corresponding numbers
    :return: Largest number found
    """
    if len(numbers) == 1:
        return numbers[0]
    else:
        return get_largest_number([x for i, x in enumerate(numbers) if x > numbers[i - 1]])


def get_smallest_number(numbers):
    """Gets the smallest number from the list received.

    You CANNOT use `min` built-in method.

    :param numbers: List containing corresponding numbers
    :return: Smallest number found
    """
    if len(numbers) == 1:
        return numbers[0]
    else:
        return get_smallest_number([x for i, x in enumerate(numbers) if x < numbers[i - 1]])


def is_even(number):
    return True if number % 2 == 0 else False


def is_odd(number):
    return not is_even(number)


def get_even_numbers(numbers):
    """Gets all even numbers from the list received.

    This function MUST NOT modify the received `numbers` list.

    :param numbers: - List containing corresponding numbers
    :return: New list containing all even numbers found
    """
    return [x for x in numbers if is_even(x)]


def filter_even_numbers(numbers):
    """Filters even numbers in the list received.

    This function MUST modify the received `numbers` list.

    :param numbers: List containing corresponding numbers
    :return: Nothing
    """
    i = len(numbers) - 1

    while i >= 0:
        if is_odd(numbers[i]):
            numbers.pop(i)
        i -= 1
    return None


def string_from_2d(two_d_list):
    result = ''
    new_line = '\n'

    for line in two_d_list:
        result += ''.join(line) + new_line

    return result.rstrip(new_line)


def draw_solid_rectangle(x, y):
    """Generates a string with a solid rectangle made of * symbols with `x` columns and `y` rows.

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding solid rectangle
    """
    SOLID = '*'
    result = []

    for _ in range(y):
        result.append([])

        for _ in range(x):
            result[-1].append(SOLID)

    return string_from_2d(result)


def draw_rectangle_borders(x, y):
    """Generates a string with a rectangle borders made of * symbols with `x` columns and `y` rows.

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding rectangle border
    """
    SOLID = '*'
    EMPTY = ' '
    x_boundaries = 0, x - 1
    y_boundaries = 0, y - 1

    result = []

    for curr_y in range(y):
        result.append([])

        for curr_x in range(x):
            if curr_y in y_boundaries or curr_x in x_boundaries:
                result[-1].append(SOLID)
            else:
                result[-1].append(EMPTY)

    return string_from_2d(result)


def draw_pyramid(height):
    """Generates a string with a pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding pyramid
    """
    pass  # <--- remove this `pass` and put your code here


def draw_inverted_pyramid(height):
    """Generates a string with a inverted pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding inverted pyramid
    """
    pass  # <--- remove this `pass` and put your code here


def chars_counter(string):
    """Counts number of times each char appears in a string.

    You CANNOT use `collections.Counter` class.

    Note that uppercase and lowercase are different letters (e.g. 'A' is different from 'a')

    :param string: String to count chars
    :return: Dictionary with char and counter key-value pairs
    """
    pass  # <--- remove this `pass` and put your code here


def sort_list_ascending(elements):
    """Sorts list received in a new list with ascending order.

    You CANNOT use `sorted` built-in method.

    :param elements: List of elements to be sorted
    :return: New list with elements sorted
    """
    pass  # <--- remove this `pass` and put your code here


def check_date(day, month, year):
    """Checks if received date is valid or not.

    You CANNOT use `datetime` nor `calendar` modules

    Be careful with leap years ;)

    :param day: Day number
    :param month: Month number
    :param year: Year number
    :return: True if date is valid, False otherwise
    """
    pass  # <--- remove this `pass` and put your code here


def check_palindrome(string):
    """Checks if received string is palindrome or not.

    Be careful with white spaces, special symbols, lowercase and uppercase ;)

    :param string: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    pass  # <--- remove this `pass` and put your code here


def join_strings(strings):
    """Concatenates a list of words with intervening occurrences of comma.

    You CANNOT use `str.join` method.

    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    pass  # <--- remove this `pass` and put your code here


if __name__ == '__main__':
    # if you need to execute custom code to check results, do it here!
    pass
