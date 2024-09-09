"""Sample output
###Q1 StringReverser###
Original String: hello .py
Reversed String: .py hello




###Q2 Circle###
Circle with radius 5:
Area: 78.54
Perimeter: 31.42
"""

###------------------------------------------------------------------------------------------------------
# Q1: Write a Python class to reverse a string word by word.
# Example:
# Input string : 'hello .py'
# Expected Output : '.py hello'
class StringReverser:
    def __init__(self, inputString):
        self.inputString = inputString

    def reverse_words(self):
        words = self.inputString.split()
        reversedWords = ' '.join(reversed(words))
        return reversedWords

###------------------------------------------------------------------------------------------------------    
# Q2: Write a Python class named Circle constructed by a radius and two methods 
# which will compute the area and the perimeter of a circle.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius
###------------------------------------------------------------------------------------------------------    

def main():
    # Q1 StringReverser
    print("###Q1 StringReverser###")
    inputString = 'hello .py'
    reverser = StringReverser(inputString)
    print("Original String:", inputString)
    print("Reversed String:", reverser.reverse_words())
    print("\n\n\n")
    
    # Q2 Circle
    print("###Q2 Circle###")
    radius = 5
    circle = Circle(radius)
    print(f"Circle with radius {radius}:")
    print(f"Area: {circle.compute_area():.2f}")
    print(f"Perimeter: {circle.compute_perimeter():.2f}")
    print("\n\n\n")

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