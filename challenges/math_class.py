"""
Implement a math class with methods for addition, subtraction,
multiplication and division. If an input is provided that is not an
int, a message should be returned instead of raising an error.

    'a' + 3  # should return 'Inputs must be numbers!'

"""

class Math:
    """Implement a math class with methods for addition, subtraction,
    multiplication and division. If an input is provided that is not an
    int, return error message as string, else return answers as an int or float."""
    def add(self, a, b):
        math_check = Math.int_check(self, a,b)
        return a + b if math_check == '' else math_check


    def subtract(self, a, b):
        math_check = Math.int_check(self, a,b)
        return a - b if math_check == '' else math_check


    def multiply(self, a, b):
        math_check = Math.int_check(self, a,b)
        return a * b if math_check == '' else math_check


    def divide(self, a, b):
        # assumption 1: floating point division rather than floor division
        # assumption 2: if any non int should not throw error, division by 0 doesn't throw error.
        math_check = Math.int_check(self, a,b)
        zero_check = Math.zero_check(self, b)  # check divisor is not 0
        if math_check == '' and zero_check == '':
            return a / b
        elif math_check != '':
            return math_check
        elif zero_check != '':
            return zero_check


    def int_check(self, a, b):
        """Check that given values a,b are int type.
        Return error message as string or '' as string."""
        return 'Inputs must be numbers!' if not ((isinstance(a, int)) and (isinstance(b, int))) else ''


    def zero_check(self, b):
        """Check that given input b is not 0.
        Return error message as string or '' as string."""
        return 'Cannot divide by zero!' if b == 0 else ''