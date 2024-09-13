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
def q5_pandas_groupby():
    df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])

    print("Original Series:")
    print(df1)

    df1 = df1.str.capitalize()

    print("\nSeries after capitalization:")
    print(df1)

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
    
    # # Q5 groupby function
    # print("###Q5### What is GroupBy in Pandas (groupby()). Give an example in Python.")
    # q5_pandas_groupby()
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