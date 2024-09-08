__Author__ = "Cai Lin"

# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner.
# Then using if statements and else statements print the user a message recommending a meal.
# For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
def q1_recommend_meal(meal):
    if meal.lower() == 'breakfast':
        print("How about some bacon and eggs?")
    elif meal.lower() == 'lunch':
        print("How about a delicious sandwich or salad?")
    elif meal.lower() == 'dinner':
        print("How about a hearty pasta or stir-fry?")
    else:
        print("Sorry, I can only recommend meals for breakfast, lunch, or dinner.")

###------------------------------------------------------------------------------------------------------        
# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay,
# including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times
# their regular hourly pay rate for all hours over 20. You should take in the user’s input for the number of hours worked,
# and their rate of pay.
def q2_calculate_gross_pay(hoursWorked, hourlyRate):
    regularHours = 20
    overtimeRate = 1.5

    if hoursWorked > regularHours:
        regularPay = regularHours * hourlyRate
        overtimeHours = hoursWorked - regularHours
        overtimePay = overtimeHours * hourlyRate * overtimeRate
        totalPay = regularPay + overtimePay
    else:
        totalPay = hoursWorked * hourlyRate

    print(f"The gross pay is: ${totalPay:.2f}")
    return totalPay

def q2_helper_handleExceptions():
    while True:
        print("Q2. Calculate a student employee’s gross pay")
        try:
            hoursWorked = float(input("Enter the number of hours worked in a week: "))
            hourlyRate = float(input("Enter the hourly pay rate: "))
            
            if hoursWorked < 0 or hourlyRate < 0:
                print("Error: Hours worked and hourly rate must be non-negative.")
                continue
            
            return hoursWorked, hourlyRate
        
        except ValueError:
            print("Error: Please enter valid numeric values.")

###------------------------------------------------------------------------------------------------------
# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
def times_ten(number):
    product = number * 10
    print(f"The product of {number} times 10 is: {product}")
    
def q3_helper_handleExceptions():
    while True:
        try:
            number = float(input("Enter a number to multiply by 10: "))
            return number
        except ValueError:
            print("Error: Please enter a valid numeric value.")

###------------------------------------------------------------------------------------------------------
# Q4: Find the errors, debug the program, and then execute to show the output.
def showCalories(calories1, calories2):
    # change the format and fix grammer
    print(f"The total calories you ate today: {calories1 + calories2:.2f}")

###------------------------------------------------------------------------------------------------------
# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
# 1/30 + 2/29 + 3/28 + ... + 30/1
def q5_calculate_series_total():
    total = 0.0  # Initialize the total sum to 0
    for i in range(1, 31):
        numerator = i
        denominator = 31 - i  # This will start from 30 and end at 1
        total += numerator / denominator

    return total

###------------------------------------------------------------------------------------------------------
# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for the area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT
def q6_triangle_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

def q6_helper_handleExceptions():
    while True:
        try:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base <= 0 or height <= 0:
                print("Base and height must be positive numbers. Please try again.")
                continue
            return base, height
        except ValueError:
            print("Invalid input. Please enter numeric values.")


###------------------------------------------------------------------------------------------------------
def main():
    # # Question 1
    # meal = input("Q1. What meal would you like recommendations for? (breakfast, lunch, or dinner): ")
    # q1_recommend_meal(meal)
    
    # # Question 2
    # hoursWorked, hourlyRate = q2_helper_handleExceptions()
    # q2_calculate_gross_pay(hoursWorked, hourlyRate)
    
    # # Question 3
    # number = q3_helper_handleExceptions()
    # times_ten(number)
    
    # # Question 4
    # # Prompt the user to input the calories for two foods
    # # Convert user input to floats for proper calculation
    # # change variable to lowercase
    # # change input to second food
    # calories1 = float(input( "How many calories are in the first food? "))
    # calories2 = float(input( "How many calories are in the second food? "))
    # showCalories(calories1, calories2)
    
    # # Question 5
    # total = q5_calculate_series_total()
    # print(f"The total of the series is: {total:.6f}")
    
    # question 6
    # Get the user input with error handling
    base, height = q6_helper_handleExceptions()
    # Call the function to calculate and display the area
    q6_triangle_area(base, height)



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
