"""Questions
1. How would you delete:
An index from your dataframe
A column from your dataframe
A row from your dataframe
2. How do you iterate over a pandas dataframe?
3. How would you convert a string to a date?
4. What is data aggregation?  Give an example in Python. 
5. What is GroupBy in Pandas (groupby()). Give an example in Python.
"""

"""Sample output

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
"""
Q5. Change the first character of each word to upper case in each word of df1
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
"""
def q5_pandas_upper():
    df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])

    print("Original Series:")
    print(df1)

    df1 = df1.str.capitalize()

    print("\nSeries after capitalization:")
    print(df1)

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
    print("###Q3### Show how to view the first 10 rows of a dataset using pandas")
    print(q3_pandas_head(df))
    print("\n")
    
    # Q4 compare the elements of the two Pandas Series
    print("###Q4### Write a Pandas program to compare the elements of the two Pandas Series.")
    q4_pandas_comparison()
    print("\n")
    
    # Q5 pandas uppercase
    print("###Q5### Change the first character of each word to upper case in each word of df1.")
    q5_pandas_upper()
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