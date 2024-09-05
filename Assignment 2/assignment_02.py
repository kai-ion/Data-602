__author__ = "Cai Lin"


"""_summary_
What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
Can you debug and fix the output?  The code should return the entire list
"""
def q1():
    numbers = [1, 2, 3, 4, 5]
    print(numbers) # remove string splitting

'''
Q2.Design a program that asks the user to enter a store’s sales for each day of the
week. The amounts should be stored in a list. Use a loop to calculate the total sales for
the week and display the result.
'''
def q2():
    # Initialize an empty list to store daily sales
    sales = []

    # Use a loop to collect sales data for each 7 weekday
    for day in range(1, 8):
        sale = float(input(f"Enter the sales for day {day}: "))
        sales.append(sale)

    # Calculate the total sales for the week
    total_sales = sum(sales)

    # Display the total sales to 2 decimal place
    print(f"Total sales for the week: ${total_sales:.2f}")

"""_summary_
Q3.Create a list with at least 5 places you’d like to travel to.   Make sure the list isn’t in
alphabetical order
● Print your list in its original order.
● Use the sort() function to arrange your list in order and reprint your list.
● Use the sort(reverse=True) and reprint your list.
"""
def q3():
    # Create a list of at least 5 places you'd like to travel to (not in alphabetical order)
    places_to_travel = ["China", "Japan", "France", "Italy", "Bali"]

    # Print the list in its original order
    print("Original list:")
    print(places_to_travel)

    # Use the sort() function to arrange the list in alphabetical order and reprint it
    places_to_travel.sort()
    print("\nList in alphabetical order:")
    print(places_to_travel)

    # Use the sort(reverse=True) to arrange the list in reverse alphabetical order and reprint it
    places_to_travel.sort(reverse=True)
    print("\nList in reverse alphabetical order:")
    print(places_to_travel)

'''
Q4.Write a program that creates a dictionary containing course numbers and the room
numbers of the rooms where the courses meet. The program should also create a
dictionary containing course numbers and the names of the instructors that teach each
course. After that, the program should let the user enter a course number, then it should
display the course’s room number, instructor, and meeting time.
'''
def q4():
    # Dictionary containing course numbers and room numbers
    course_rooms = {
        "Data602": "Online",
        "Data606": "Online",
        "Data607": "Online",
        "Data608": "Online",
        "Data698": "Online"
    }

    # Dictionary containing course numbers and instructors
    course_instructors = {
        "Data602": "Prof. schettini",
        "Data606": "Prof. A",
        "Data607": "Prof. B",
        "Data608": "Prof. C",
        "Data698": "Prof. D"
    }

    # Dictionary containing course numbers and meeting times
    course_times = {
        "Data602": "Asynchronous",
        "Data606": "Asynchronous",
        "Data607": "Asynchronous",
        "Data608": "Asynchronous",
        "Data698": "Asynchronous"
    }
    
    # Prompt the user to enter a course number
    course_number = input("Enter the course number: ")
    
    # Check if the course number is found in each dictionary and print the corresponding information
    if course_number in course_rooms:
        print(f"Room Number: {course_rooms[course_number]}")
    else:
        print("Course number not found in room numbers.")

    if course_number in course_instructors:
        print(f"Instructor: {course_instructors[course_number]}")
    else:
        print("Course number not found in instructors.")

    if course_number in course_times:
        print(f"Meeting Time: {course_times[course_number]}")
    else:
        print("Course number not found in meeting times.")


"""_summary_
Q5. Write a program that keeps names and email addresses in a dictionary as
key-value pairs. The program should then demonstrate the four options:
● look up a person’s email address,
● add a new name and email address,
● change an existing email address, and
● delete an existing name and email address.
    """
def q5():
    # Initialize the dictionary to store names and email addresses
    email_dict = {
        "Person A": "personA@example.com",
        "Person B": "personB@example.com",
        "Person C": "personC@example.com",
        "Person D": "personD@example.com",
        "Person E": "personE@example.com"
    }

    def look_up_email():
        """
        Prompt the user to enter a name and look up the corresponding email address
        in the email_dict. If the name is found, display the email address; otherwise,
        inform the user that the name is not found.
        """
        name = input("Enter the name to look up: ")
        if name in email_dict:
            print(f"{name}'s email address is {email_dict[name]}")
        else:
            print(f"{name} not found.")

    def add_email():
        """
        Prompt the user to enter a name and an email address, and add this information
        to the email_dict. If the name already exists in the dictionary, inform the user
        that the name already exists. Otherwise, add the new name and email address
        to the dictionary.
        """
        name = input("Enter the name to add: ")
        email = input("Enter the email address: ")
        if name in email_dict:
            print(f"{name} already exists.")
        else:
            email_dict[name] = email
            print(f"{name} has been added with email {email}")

    def change_email():
        """
        Prompt the user to enter a name and a new email address to update the existing
        email address for the given name in the email_dict. If the name is found,
        update the email address; otherwise, inform the user that the name is not found.
        """
        name = input("Enter the name to update: ")
        if name in email_dict:
            new_email = input("Enter the new email address: ")
            email_dict[name] = new_email
            print(f"{name}'s email address has been updated to {new_email}")
        else:
            print(f"{name} not found.")

    def delete_email():
        """
        Prompt the user to enter a name to delete from the email_dict. If the name is
        found, remove it from the dictionary; otherwise, inform the user that the name
        is not found.
        """
        name = input("Enter the name to delete: ")
        if name in email_dict:
            del email_dict[name]
            print(f"{name} has been deleted from the address book.")
        else:
            print(f"{name} not found.")

    def main():
        """
        Display a menu of options and prompt the user to select an option. Based on the
        user's choice, call the corresponding function to look up, add, change, or delete
        an email address. Continue displaying the menu and processing choices until the
        user chooses to quit.
        """
        while True:
            print("\nMenu")
            print("q. Look up an email address")
            print("w. Add a new name and email address")
            print("e. Change an existing email address")
            print("r. Delete an existing name and email address")
            print("t. Quit")
            choice = input("Enter your choice: ")
            
            if choice == "q":
                look_up_email()
            elif choice == "w":
                add_email()
            elif choice == "e":
                change_email()
            elif choice == "r":
                delete_email()
            elif choice == "t":
                print("Quitting")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    # Run the program
    main()



def main():
    """ Main entry point of the app """
    q1()
    q2()
    q3()
    q4()
    q5()
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()