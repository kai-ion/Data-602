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
###Q1### How would you delete: An index from your dataframe, A column from your dataframe, A row from your dataframe
Original DataFrame with Name as index:
         Age         City   Birthdate
Name
Alice     24     New York  1990-05-15
Bob       27  Los Angeles  1985-06-22
Charlie   22      Chicago  1992-07-30
David     32      Houston  1988-11-02

DataFrame after resetting index:
   index     Name  Age         City   Birthdate
0      0    Alice   24     New York  1990-05-15
1      1      Bob   27  Los Angeles  1985-06-22
2      2  Charlie   22      Chicago  1992-07-30
3      3    David   32      Houston  1988-11-02

DataFrame after deleting the 'City' column:
      Name  Age   Birthdate
0    Alice   24  1990-05-15
1      Bob   27  1985-06-22
2  Charlie   22  1992-07-30
3    David   32  1988-11-02

DataFrame after deleting the row at index 1 (Bob):
      Name  Age      City   Birthdate
0    Alice   24  New York  1990-05-15
2  Charlie   22   Chicago  1992-07-30
3    David   32   Houston  1988-11-02


###Q2### How do you iterate over a pandas dataframe?

Iterating over rows using iterrows():
Index: 0, Name: Alice, Age: 24, City: New York
Index: 1, Name: Bob, Age: 27, City: Los Angeles
Index: 2, Name: Charlie, Age: 22, City: Chicago
Index: 3, Name: David, Age: 32, City: Houston

Iterating over rows using itertuples():
Index: 0, Name: Alice, Age: 24, City: New York
Index: 1, Name: Bob, Age: 27, City: Los Angeles
Index: 2, Name: Charlie, Age: 22, City: Chicago
Index: 3, Name: David, Age: 32, City: Houston

Iterating over columns:
Column: Name, Data: ['Alice', 'Bob', 'Charlie', 'David']
Column: Age, Data: [24, 27, 22, 32]
Column: City, Data: ['New York', 'Los Angeles', 'Chicago', 'Houston']
Column: Birthdate, Data: ['1990-05-15', '1985-06-22', '1992-07-30', '1988-11-02']


###Q3### How would you convert a string to a date?

DataFrame after converting 'Birthdate' from string to datetime:
      Name  Age         City  Birthdate
0    Alice   24     New York 1990-05-15
1      Bob   27  Los Angeles 1985-06-22
2  Charlie   22      Chicago 1992-07-30
3    David   32      Houston 1988-11-02

Data types after conversion:
Name                 object
Age                   int64
City                 object
Birthdate    datetime64[ns]
dtype: object


###Q4### What is data aggregation?  Give an example in Python.

Aggregated Age Data:
total_age      105.00
average_age     26.25
max_age         32.00
min_age         22.00
Name: Age, dtype: float64


###Q5### What is GroupBy in Pandas (groupby()). Give an example in Python.

Aggregated Age Data by City:
             total_age  average_age  max_age  min_age
City
Chicago             22         22.0       22       22
Houston             32         32.0       32       32
Los Angeles         27         27.0       27       27
New York            24         24.0       24       24

"""

import pandas as pd

###------------------------------------------------------------------------------------------------------  
"""
Q1. How would you delete:
An index from your dataframe
A column from your dataframe
A row from your dataframe
"""
def q1_datafram_delete(data):
    df = pd.DataFrame(data)

    # Set the 'Name' column as the index
    df_reset_index = df.set_index('Name')
    
    print("Original DataFrame with Name as index:")
    print(df_reset_index)

    # Delete the index (reset the index)
    df_reset_index = df.reset_index()
    print("\nDataFrame after resetting index:")
    print(df_reset_index)

    # Delete a column ('City')
    df_drop_column = df.drop('City', axis=1)
    print("\nDataFrame after deleting the 'City' column:")
    print(df_drop_column)

    # Delete a row (row at index 1)
    df_drop_row = df.drop(1)
    print("\nDataFrame after deleting the row at index 1 (Bob):")
    print(df_drop_row)
    

###------------------------------------------------------------------------------------------------------  
"""
Q2. How do you iterate over a pandas dataframe?
"""
import pandas as pd

def q2_pandas_iterate(data):
    df = pd.DataFrame(data)
    # Iterating over DataFrame using iterrows()
    print("\nIterating over rows using iterrows():")
    for index, row in df.iterrows():
        print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

    # Iterating over DataFrame using itertuples()
    print("\nIterating over rows using itertuples():")
    for row in df.itertuples():
        print(f"Index: {row.Index}, Name: {row.Name}, Age: {row.Age}, City: {row.City}")

    # Iterating over DataFrame columns
    print("\nIterating over columns:")
    for column in df:
        print(f"Column: {column}, Data: {df[column].tolist()}")

###------------------------------------------------------------------------------------------------------  
"""
Q3. How would you convert a string to a date?
"""
def q3_string_date(data):
    df = pd.DataFrame(data)
    # Convert the 'Birthdate' column from string to datetime
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])

    print("\nDataFrame after converting 'Birthdate' from string to datetime:")
    print(df)

    # Check the data type of the 'Birthdate' column to confirm it's datetime
    print("\nData types after conversion:")
    print(df.dtypes)

###------------------------------------------------------------------------------------------------------  
"""
Q4. What is data aggregation?  Give an example in Python. 
"""
def q4_aggregation(data):
    df = pd.DataFrame(data)
    # Perform aggregation on the 'Age' column
    age_aggregation = df['Age'].agg(
        total_age='sum',
        average_age='mean',
        max_age='max',
        min_age='min'
    )

    print("\nAggregated Age Data:")
    print(age_aggregation)

###------------------------------------------------------------------------------------------------------ 
"""
Q5. What is GroupBy in Pandas (groupby()). Give an example in Python.
"""
def q5_pandas_groupby(data):
    df = pd.DataFrame(data)
    # Perform GroupBy on 'City' and aggregate the 'Age' column
    grouped_data = df.groupby('City').agg(
        total_age=('Age', 'sum'),
        average_age=('Age', 'mean'),
        max_age=('Age', 'max'),
        min_age=('Age', 'min')
    )

    print("\nAggregated Age Data by City:")
    print(grouped_data)

###------------------------------------------------------------------------------------------------------  

def main():
    # Create a sample DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [24, 27, 22, 32],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
            'Birthdate': ['1990-05-15', '1985-06-22', '1992-07-30', '1988-11-02']}
    
    # Q1 delete data
    print("###Q1### How would you delete: An index from your dataframe, A column from your dataframe, A row from your dataframe")
    q1_datafram_delete(data)
    print("\n")
    
    # Q2 iterate dataframe
    print("###Q2### How do you iterate over a pandas dataframe?")
    q2_pandas_iterate(data)
    print("\n")
    
    # # Q3 convert string to date
    print("###Q3### How would you convert a string to a date?")
    q3_string_date(data)
    print("\n")
    
    # Q4 data aggregation
    print("###Q4### What is data aggregation?  Give an example in Python.")
    q4_aggregation(data)
    print("\n")
    
    # Q5 groupby function
    print("###Q5### What is GroupBy in Pandas (groupby()). Give an example in Python.")
    q5_pandas_groupby(data)
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