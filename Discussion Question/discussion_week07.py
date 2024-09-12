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
    
    return df

###------------------------------------------------------------------------------------------------------  
"""
Q3. Show how to view the first 10 rows of a dataset using pandas
"""
def q3_pandas_head(df):
    return df.head(10)

###------------------------------------------------------------------------------------------------------  
"""
Q4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
"""
def q4_pandas_comparison():
    series1 = pd.Series([2, 4, 6, 8, 10])
    series2 = pd.Series([1, 3, 5, 7, 10])

    
    print("Series 1:")
    print(series1)

    print("\nSeries 2:")
    print(series2)

    comparison = series1 == series2
    print("\nComparison (Series 1 == Series 2):")
    print(comparison)

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

def main():
    # Q1 Similarities and Differences:
    print("###Q1### What is pandas and why use it?")
    print(q1_pandas())
    print("\n")
    
    # Q2 Import a CSV file using pandas
    print("###Q2### Give an example of how to import a csv file using pandas")
    df = q2_pandas_csv()
    print(df.head(1))
    print("\n")
    
    # Q3 First 10 rows of df
    print("###Q3### Write a Pandas program to compare the elements of the two Pandas Series.")
    print(q4_pandas_comparison())
    print("\n")
    
    # # Q4 compare the elements of the two Pandas Series
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