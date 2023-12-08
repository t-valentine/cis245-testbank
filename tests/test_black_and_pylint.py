# After adding Black and Pylint to Poetry, you can them using the following commands in your terminal:
# poetry run black filename.py // This reformats the code
# poetry run pylint filename.py // This checks for errors, coding standards, etc...

"""
This is a module that adds two numbers
"""


def add_numbers(a, b):
    """This is a function that adds two numbers"""
    return a + b


print(add_numbers(2, 3))
