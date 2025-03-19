# Lesson 09: Exception Handling

# Exception handling with custom exception
class NegativeNumberError(Exception):
    pass

def divide_numbers(a, b):
    if a < 0 or b < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return a / b

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = divide_numbers(num1, num2)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
except NegativeNumberError as e:
    print("Error:", e)