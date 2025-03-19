# Lesson 08: Control Modules & Functions

# Example of a module and functions
import random

def greet(name):
    greetings = ["Hello", "Hi", "Hey", "Welcome"]
    return f"{random.choice(greetings)}, {name}!"

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Using the functions
greeting = greet("Aleha")
print(greeting)
print("Factorial of 5:", factorial(5))