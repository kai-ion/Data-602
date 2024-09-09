"""
1. Write a function to calculate the area and perimeter of a rectangle.
2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.
3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample string: “CUNY sps”
# of upper case characters: 4
# of lower case characters: 3
4. Write a Python function to sum all the numbers in a list
5. Create a function that shows an example of global vs local variables.
6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
"""

###------------------------------------------------------------------------------------------------------
# Q1. Function to calculate the area and perimeter of a rectangle
def rectangle_size(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    # print(f"Area of the rectangle: {area}")
    # print(f"Perimeter of the rectangle: {perimeter}")
    return area, perimeter

###------------------------------------------------------------------------------------------------------
# Q2. Function to check if a number is even or odd
def check_even(number):
    return "even" if number % 2 == 0 else "odd"

###------------------------------------------------------------------------------------------------------
# Q3. Function to calculate the number of upper case and lower case letters in a string
def count_case(string):
    upperCase = 0
    lowerCase = 0
    # For loop checking each letter
    for char in string:
        if char.isupper():
            upperCase += 1
        elif char.islower():
            lowerCase += 1
    return upperCase, lowerCase

###------------------------------------------------------------------------------------------------------
# Q4. Function to sum all the numbers in a list
def sum_numbers(numList):
    return sum(numList)

###------------------------------------------------------------------------------------------------------
# Q5. Example of global vs local variables with the same name
var = 10  # Global variable

def local_var():
    var = 5  # Local variable (same name as global variable)
    return var

###------------------------------------------------------------------------------------------------------
import random

def multiply_number(number):
    unknownNumber = random.randint(1, 100)  # Randomly generates an integer between 1 and 100
    res = number * unknownNumber
    return res, unknownNumber

###------------------------------------------------------------------------------------------------------
def main():
    # 1. Rectangle area and perimeter
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area, perimeter = rectangle_size(length, width)
    print(f"Area of the rectangle: {area}, Perimeter of the rectangle: {perimeter}")

    # 2. Even or odd check
    number = int(input("Enter a number to check if it's even or odd: "))
    res = check_even(number)
    print(f"The number {number} is {res}.")

    # 3. Count upper and lower case letters
    string = input("Enter a string: (Sample string: “CUNY sps”)")
    upperCase, lowerCase = count_case(string)
    print(f"Number of upper case characters: {upperCase}, Number of lower case characters: {lowerCase}")

    # 4. Sum of a list
    numList = [1, 2, 3, 4, 5]
    totalSum = sum_numbers(numList)
    print(f"The sum of the list is: {totalSum}")

    # 5. Global vs local variable (nonlocal example)
    print(f"Global variable: {var}")
    print(f"Local variable inside function: {local_var()}")  # Refers to the local variable

    # 6. Multiply with a random unknown number
    number = int(input("Enter a number to multiply with a random unknown number: "))
    result, unknownNumber = multiply_number(number)
    print(f"The result of multiplying {number} with the randomly generated number {unknownNumber} is: {result}")

if __name__ == "__main__":
    main()

"""
*    *
*  *
* *
* *
*  *
*    *
"""