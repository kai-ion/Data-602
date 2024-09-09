__author__ = "Cai Lin"

###------------------------------------------------------------------------------------------------------    
# Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
# lastname, and balance. The default balance should be set to 0.
# In addition, create:
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance.
# ● Use the __str__() method to display the bank name, owner name, and current balance.
# ● Make a series of deposits and withdrawals to test your class.
class BankAccount:
    def __init__(self, bankName, firstName, lastName, balance=0):
        self.bankName = bankName
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print(f"Cannot withdraw ${amount:.2f}. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def __str__(self):
        return f"Bank Name: {self.bankName}\nAccount Holder: {self.firstName} {self.lastName}\nBalance: ${self.balance:.2f}"


###------------------------------------------------------------------------------------------------------    
# Q2: Create a class Box that has attributes length and width that takes values for length
# and width upon construction (instantiation via the constructor).
# In addition, create:
# ● A method called render() that prints out to the screen a box made with asterisks of
#    length and width dimensions.
# ● A method called invert() that switches length and width with each other.
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations.
# ● A method called double() that doubles the size of the box.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
#    their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box.
# ● A method get_dim() that returns a tuple containing the length and width of the box.
# ● A method combine() that takes another box as an argument and increases the length
#    and width by the dimensions of the box passed in.
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle.
# ● Instantiate 3 boxes of dimensions 5,10, 3,4 and 5,10 and assign to variables box1, box2, and box3 respectively.
# ● Print dimension info for each using print_dim().
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly.
# ● Combine box3 into box1 (i.e. box1.combine()).
# ● Double the size of box2.
# ● Combine box2 into box1.

import math

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        for i in range(self.length):
            print("*" * self.width)

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def double(self):
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        return self.length, self.width

    def combine(self, other):
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

###------------------------------------------------------------------------------------------------------    
def main():
    # Q1: BankAccount class
    print("###Q1 BankAccount###")
    account = BankAccount("Chase", "Cai", "Lin")
    print(account)

    account.deposit(1000)
    account.withdrawal(500)
    account.withdrawal(600)
    print(account)
    print("\n\n\n")
    
    # Q2: Box class
    print("###Q2 Box###")
    # Testing Box class

    # Instantiate 3 boxes
    box1 = Box(5, 10)
    box2 = Box(3, 4)
    box3 = Box(5, 10)

    # Print dimensions
    box1.print_dim()
    box2.print_dim()
    box3.print_dim()

    # Check equality of boxes
    print(box1 == box2)  # False
    print(box1 == box3)  # True

    # Combine box3 into box1
    box1.combine(box3)
    box1.print_dim()  # Updated dimensions of box1

    # Double the size of box2
    box2.double()
    box2.print_dim()  # Doubled dimensions of box2

    # Combine box2 into box1
    box1.combine(box2)
    box1.print_dim()  # Final dimensions of box1

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