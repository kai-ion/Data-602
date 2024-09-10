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
    arr = np.array([1, 2, 3, 4])
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
    odd = array1[array1 % 2 == 1]
    return odd

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------  

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
    print(odd_numbers())
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