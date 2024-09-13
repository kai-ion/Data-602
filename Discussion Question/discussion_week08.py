"""Questions
1. What is pandas and why use it?
2. Give an example of how to import a csv file using pandas
3. Show how to view the first 10 rows of a dataset using pandas
4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
5. Change the first character of each word to upper case in each word of df1
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
"""
"""Sample output
###Q1### What is pandas and why use it?
Pandas is a python library for data manipulation and analysis. It provides data structures such as DataFrames and Series, which are ideal for handling structured data.


###Q2### Give an example of how to import a csv file using pandas

kobe.csv
    vs  game quarter  time                              description basket
0  ORL     1       1  9:47  Kobe Bryant makes 4-foot two point shot      H


###Q3### Show how to view the first 10 rows of a dataset using pandas
    vs  game quarter  time                                        description basket
0  ORL     1       1  9:47            Kobe Bryant makes 4-foot two point shot      H
1  ORL     1       1  9:07                          Kobe Bryant misses jumper      M
2  ORL     1       1  8:11                   Kobe Bryant misses 7-foot jumper      M
3  ORL     1       1  7:41  Kobe Bryant makes 16-foot jumper (Derek Fisher...      H
4  ORL     1       1  7:03                    Kobe Bryant makes driving layup      H
5  ORL     1       1  6:01                          Kobe Bryant misses jumper      M
6  ORL     1       1  4:07                  Kobe Bryant misses 12-foot jumper      M
7  ORL     1       1  0:52                  Kobe Bryant misses 19-foot jumper      M
8  ORL     1       1  0:00                           Kobe Bryant misses layup      M
9  ORL     1       2  6:35                           Kobe Bryant makes jumper      H


###Q4### Write a Pandas program to compare the elements of the two Pandas Series.
Series 1:
0     2
1     4
2     6
3     8
4    10
dtype: int64

Series 2:
0     1
1     3
2     5
3     7
4    10
dtype: int64

Comparison (Series 1 == Series 2):
0    False
1    False
2    False
3    False
4     True
dtype: bool


###Q5### Change the first character of each word to upper case in each word of df1.
Original Series:
0     hello
1        to
2      cuny
3    class?
dtype: object

Series after capitalization:
0     Hello
1        To
2      Cuny
3    Class?
dtype: object
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