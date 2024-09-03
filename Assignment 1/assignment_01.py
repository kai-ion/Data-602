#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = int(input('Enter the score for test 1: ')) # converted inputs to integers
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) # added test3
# Calculate the average test score.10
average = (test1 + test2 + test3) / 3 # added () around 3 testscores
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: # fix highscore var name
    print('Congratulations!')
    print('That is a great average!') # corrected indentation

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

### calculate the area of two rectangles

# Get the length and width of the first rectangle as floats for decimals
length1 = float(input('Enter the length of the first rectangle: '))
width1 = float(input('Enter the width of the first rectangle: '))

# Calculate the area of the first rectangle
area1 = length1 * width1

# Get the length and width of the second rectangle
length2 = float(input('Enter the length of the second rectangle: '))
width2 = float(input('Enter the width of the second rectangle: '))

# Calculate the area of the second rectangle
area2 = length2 * width2

# Print the areas of both rectangles
print('The area of the first rectangle is', area1)
print('The area of the second rectangle is', area2)


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Get user's first name and age
name = input('Enter your first name: ')  # Input as string for name
age = int(input('Enter your age: '))  # Input converted to integer for age

# Print a birthday message to the user
print(f"Happy birthday, {name}! You are {age} years old today!")





