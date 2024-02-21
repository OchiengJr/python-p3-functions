import io
import sys

def greet_programmer():
    print(u"Hello, programmer!")

def greet(name):
    print("Hello, %s!" % name)

def greet_with_default(name="programmer"):
    print("Hello, %s!" % name)

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2