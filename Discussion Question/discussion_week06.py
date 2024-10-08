"""
1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.
2. What is the ndarray in numPy?
3. Create a 1D array of numbers from 0 to 9 
Desired Output: 
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
4. Extract all odd numbers from array1 
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
5. Get the common items between a and  b  
#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

#Desired Output:

array([2, 4])
6. From array a remove all items present in array  b 
#Input:

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

#Desired Output:

array([1,2,3,4])
7. Find out if iris has any missing values. 
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
"""
"""Sample Output
###Q1### Similarities and Differences of Numpy and Pandas:
numpy provides ndarray while pandas provides Series and DataFrame, both of which are built on top of ndarray

NumPy Array:
[[1 2 3]
 [4 5 6]]

Pandas DataFrame:
   A  B  C
0  1  2  3
1  4  5  6


###Q2### What is the ndarray in NumPy?
multi-dimensional array

[[1 2 3]
 [4 5 6]]


###Q3### Create a 1D array of numbers from 0 to 9.
[0 1 2 3 4 5 6 7 8 9]


###Q4### Extract all odd numbers from array1.
Original array: [0 1 2 3 4 5 6 7 8 9]
Odd numbers: [1 3 5 7 9]


###Q5### Get the common items between a and b.
Array a: [1 2 3 2 3 4 3 4 5 6]
Array b: [ 7  2 10  2  7  4  9  4  9  8]
Common items: [2 4]


###Q6### From array a remove all items present in array b.
Array a: [1 2 3 4 5]
Array b: [5 6 7 8 9]
Array after removing items present in b: [1 2 3 4]


###Q7### Find out if iris has any missing values.
Number of missing values in the iris dataset: 0
"""


import numpy as np
import pandas as pd


###------------------------------------------------------------------------------------------------------  
"""
Q1. What are the similarities and differences between pandas and numpy?
    Include some type of example with code.

numpy provides ndarray while pandas provides Series and DataFrame, both of which are built on top of ndarray
"""
def pandas_numpy():
    print("numpy provides ndarray while pandas provides Series and DataFrame, both of which are built on top of ndarray")
    # Example of NumPy array
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nNumPy Array:")
    print(arr)

    # Example of Pandas DataFrame
    df = pd.DataFrame(arr, columns=["A", "B", "C"])
    print("\nPandas DataFrame:")
    print(df)

###------------------------------------------------------------------------------------------------------  
"""
Q2. What is the ndarray in NumPy?
    Returns an example of ndarray in NumPy.
       
multi-dimensional array
"""
def ndarray_example():
    print("multi-dimensional array\n")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return arr

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
    print("###Q1### Similarities and Differences of Numpy and Pandas:")
    pandas_numpy()
    print("\n")
    
    # Q2 ndarray in NumPy
    print("###Q2### What is the ndarray in NumPy?")
    print(ndarray_example())
    print("\n")
    
    # Q3 1d array
    print("###Q3### Create a 1D array of numbers from 0 to 9.")
    print(create_array())
    print("\n")
    
    # Q4 Odd Num
    print("###Q4### Extract all odd numbers from array1.")
    print("Odd numbers:", odd_numbers())
    print("\n")
    
    # Q5 Common Items
    print("###Q5### Get the common items between a and b.")
    print("Common items:", common_items())
    print("\n")
    
    # Q6 Remove Items
    print("###Q6### From array a remove all items present in array b.")
    print("Array after removing items present in b:", remove_items())
    print("\n")
    
    # Q7 Missing Values
    print("###Q7### Find out if iris has any missing values.")
    print("Number of missing values in the iris dataset:", missing_values())
    print("\n")

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