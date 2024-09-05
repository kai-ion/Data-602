__author__ = "Cai Lin"

"""_summary_
1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger
2. Repeat question 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set a variable len_animals to the length of the animal list.
3. Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
    The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
    Remember, the index number of the 5th element is not 5
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
the_fifth_element = -999
4. Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#Expected output:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

5. Write a program to remove all occurrences of item 20 in the following list.
list2 = [5, 20, 30, 15, 20, 30, 20]

6. Using the following dictionary .. (Use python to solve for the answer.)
dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
a. What is the name of the course?
b. Change the course to DATA602
c. Add new information to the dictionary - "Professor" with "Schettini"
d. Using the len function, find how many keys there are in the dictionary. 
7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}
    """
# Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger
def q1():
    animals = ["cat", "dog", "manta ray", "horse", "crouching tiger"]
    print(animals[:])
    return animals
    
# loop through and print each item in the animal list by iterating through an index number and using range(). 
# Set a variable len_animals to the length of the animal list.
def q2(animals):
    len_animals = len(animals)

    for i in range(len_animals):
        print(animals[i])

"""_summary_
Reorganize the countdown list in descending order and return the 5th element
The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
Remember, the index number of the 5th element is not 5
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
the_fifth_element = -999
    """
def q3():
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999
    countdown_sorted = sorted(countdown, reverse=True)
    the_fifth_element = countdown_sorted[4]  # index 4 corresponds to the 5th element
    print(the_fifth_element)
    print(countdown_sorted)

"""_summary_
Add item 7000 after 6000 in the list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""
def q4():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)  # Append 7000 to the sublist [5000, 6000]
    print(list1)

"""_summary_
Remove all occurrences of item 20 from the list
list2 = [5, 20, 30, 15, 20, 30, 20]
"""
def q5():
    list2 = [5, 20, 30, 15, 20, 30, 20]
    list2 = [num for num in list2 if num != 20]
    print(list2)


"""_summary_
Using the following dictionary .. (Use python to solve for the answer.)
dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
a. What is the name of the course?
b. Change the course to DATA602
c. Add new information to the dictionary - "Professor" with "Schettini"
d. Using the len function, find how many keys there are in the dictionary. 
}
    """
def q6():
    dict_info = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

    # a. Name of the course
    course_name = dict_info["Course"]
    print("Course:", course_name)

    # b. Change the course to DATA602
    dict_info["Course"] = "DATA602"
    print("Course Name Change:", dict_info["Course"])

    # c. Add new information to the dictionary
    dict_info["Professor"] = "Schettini"
    print("Professor:", dict_info["Professor"])

    # d. Find how many keys there are in the dictionary
    num_keys = len(dict_info)
    print("Number of keys:", num_keys)

"""_summary_
Write a Python program to change Brad’s salary to 7500 in the following dictionary.
sample_dict = {
'emp1': {'name': 'Amanda', 'salary': 8200},
'emp2': {'name': 'John', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 700}
"""
def q7():
    sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
    }
    print(sample_dict)
    sample_dict['emp3']['salary'] = 7500
    print(sample_dict)


def main():
    """ Main entry point of the app """
    animals = q1()
    q2(animals)
    q3()
    q4()
    q5()
    q6()
    q7()
    
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
