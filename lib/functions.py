import io
import sys

def greet_programmer():
    """Prints a greeting message for a programmer."""
    print("Hello, programmer!")

def greet(name):
    """Prints a greeting message with the provided name."""
    print("Hello, %s!" % name)

def greet_with_default(name="programmer"):
    """Prints a greeting message with the provided name, defaults to 'programmer' if no name is provided."""
    print("Hello, %s!" % name)

def add(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2

def halve(number):
    """Halves the given number and returns the result."""
    return number / 2
