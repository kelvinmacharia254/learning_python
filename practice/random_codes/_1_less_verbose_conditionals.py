"""
Use linters like pylint, flake8, or black.
They often catch verbose patterns and suggest cleaner alternatives.

We have used pylint to check the code verbosity and readability.
Pylint suggested the condition in the function is_even to be simplified.

Uncomment the verbose function to see the pylint suggestions.
"""

# This function is verbose and can be simplified.
# def is_even(number):
#     """
#     Check if a number is even.
#     :param number: The number to check."""
#     if number%2== 0:
#         return True
#     else:
#         return False

# This function is simplified and more readable.
# It uses a single return statement.
# The modulo operator to check if the number is even.
# Gets a higher score from linters.


def is_even(n):
    """
    Check if a number is even.
    :param n: The number to check."""
    return n % 2 == 0


print(is_even(4))  # True
print(is_even(5))  # False
