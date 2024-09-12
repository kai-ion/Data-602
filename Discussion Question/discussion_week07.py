"""
1. What is pandas and why use it?
2. Give an example of how to import a csv file using pandas
3. Show how to view the first 10 rows of a dataset using pandas
4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
5. Change the first character of each word to upper case in each word of df1
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
"""


###------------------------------------------------------------------------------------------------------  
"""
Q1. What is pandas and why use it?

Pandas is a python library for data manipulation and analysis. It provides data structures such as DataFrames and Series, which are ideal for handling structured data.
"""
def q1_pandas():
    return "Pandas is a python library for data manipulation and analysis. It provides data structures such as DataFrames and Series, which are ideal for handling structured data."
    

###------------------------------------------------------------------------------------------------------  
"""
Q2. Give an example of how to import a csv file using pandas
"""
import pandas as pd

def q2_pandas_csv():
    df = pd.read_csv('Discussion Question\kobe.csv')
    print("\nkobe.csv")
    
    return df.head(1)

###------------------------------------------------------------------------------------------------------  
# 3. Create a 1D array of numbers from 0 to 9.
#    Desired Output: 
#    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def create_array():
    array = np.arange(10)
    return array

###------------------------------------------------------------------------------------------------------  
# 4. Extract all odd numbers from array1.
#    array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def odd_numbers():
    array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("Original array:", array1)
    odd_numbers = array1[array1 % 2 == 1]
    return odd_numbers

###------------------------------------------------------------------------------------------------------ 
# 5. Get the common items between a and b.
#    #input
#    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
#    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
#    #Desired Output:
#    array([2, 4])
def common_items():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print("Array a:", a)
    print("Array b:", b)
    common_items = np.intersect1d(a, b)
    return common_items

###------------------------------------------------------------------------------------------------------  
# 6. From array a remove all items present in array b.
#    a = np.array([1, 2, 3, 4, 5])
#    b = np.array([5, 6, 7, 8, 9])
def remove_items():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 6, 7, 8, 9])
    print("Array a:", a)
    print("Array b:", b)
    result = np.setdiff1d(a, b)
    return result

###------------------------------------------------------------------------------------------------------  
# 7. Find out if iris has any missing values.
#    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#    iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
def missing_values():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    missing_values = np.isnan(iris).sum()
    return missing_values

###------------------------------------------------------------------------------------------------------  

def main():
    # Q1 Similarities and Differences:
    print("###Q1### What is pandas and why use it?")
    print(q1_pandas())
    print("\n")
    
    # Q2 Import a CSV file using pandas
    print("###Q2### Give an example of how to import a csv file using pandas")
    print(q2_pandas_csv())
    print("\n")
    
    # # Q3 1d array
    # print("###Q3### Create a 1D array of numbers from 0 to 9.")
    # print(create_array())
    # print("\n")
    
    # # Q4 Odd Num
    # print("###Q4### Extract all odd numbers from array1.")
    # print("Odd numbers:", odd_numbers())
    # print("\n")
    
    # # Q5 Common Items
    # print("###Q5### Get the common items between a and b.")
    # print("Common items:", common_items())
    # print("\n")
    

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