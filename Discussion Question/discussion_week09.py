"""Questions
1. Share a link to the dataset you are planning to use for your final project/proposal.
2. Why is this dataset interesting?  Why do you want to analyze it?
3. Display some summary statistics about your dataset.
If you notice other classmates with similar datasets or end goals, you might consider grouping with them to complete the final project.   
"""

"""Sample output
###Q1### Share a link to the dataset you are planning to use for your final project/proposal.
https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022


###Q2### Why is this dataset interesting?  Why do you want to analyze it?
This NFL dataset from 1999 to 2022 is interesting because it provides a comprehensive view of team performance over more than two decades. The data includes metrics such as passing yards, rushing yards, touchdowns, fumbles, and more. By analyzing this dataset, I can gain insights into how strategies have evolved over time, identify correlations between offensive/defensive stats and success, and explore trends in team performance. It also offers an opportunity to compare how different teams adapt to changes in play style over time.


###Q3### Display some summary statistics about your dataset.
       total_snaps  yards_gained   touchdown  passing_yards  rushing_yards  interception        wins      losses
count   384.000000    384.000000  384.000000     384.000000     384.000000    384.000000  384.000000  384.000000
mean   1024.260417   9670.447917   41.651042    4032.023438    1859.200521     13.575521    8.091146    8.153646
std      52.252549   1050.132630    9.114479     535.805255     348.128385      4.494212    3.065776    3.073484
min     866.000000   6761.000000   21.000000    2598.000000    1168.000000      2.000000    0.000000    1.000000
25%     989.000000   8916.500000   35.000000    3644.750000    1616.500000     10.000000    6.000000    6.000000
50%    1018.000000   9669.500000   40.000000    4020.000000    1820.000000     13.000000    8.000000    8.000000
75%    1060.250000  10348.250000   48.000000    4388.750000    2062.500000     16.000000   10.250000   10.000000
max    1181.000000  12913.000000   74.000000    5572.000000    3313.000000     30.000000   15.000000   16.000000
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q1. Share a link to the dataset you are planning to use for your final project/proposal.

https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q2. Why is this dataset interesting?  Why do you want to analyze it?

This NFL dataset from 1999 to 2022 is interesting because it provides a comprehensive view of team performance over more than two decades. The data includes metrics such as passing yards, rushing yards, touchdowns, fumbles, and more. By analyzing this dataset, I can gain insights into how strategies have evolved over time, identify correlations between offensive/defensive stats and success, and explore trends in team performance. It also offers an opportunity to compare how different teams adapt to changes in play style over time.
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q3. Display some summary statistics about your dataset.
       total_snaps  yards_gained   touchdown  passing_yards  rushing_yards  interception        wins      losses
count   384.000000    384.000000  384.000000     384.000000     384.000000    384.000000  384.000000  384.000000
mean   1024.260417   9670.447917   41.651042    4032.023438    1859.200521     13.575521    8.091146    8.153646
std      52.252549   1050.132630    9.114479     535.805255     348.128385      4.494212    3.065776    3.073484
min     866.000000   6761.000000   21.000000    2598.000000    1168.000000      2.000000    0.000000    1.000000
25%     989.000000   8916.500000   35.000000    3644.750000    1616.500000     10.000000    6.000000    6.000000
50%    1018.000000   9669.500000   40.000000    4020.000000    1820.000000     13.000000    8.000000    8.000000
75%    1060.250000  10348.250000   48.000000    4388.750000    2062.500000     16.000000   10.250000   10.000000
max    1181.000000  12913.000000   74.000000    5572.000000    3313.000000     30.000000   15.000000   16.000000

"""


###------------------------------------------------------------------------------------------------------  
import pandas as pd
    
def main():
    # Q1 Link to dataset
    print("###Q1### Share a link to the dataset you are planning to use for your final project/proposal.")
    print("https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022")
    print("\n")
    
    # Q2 why is it interesting
    print("###Q2### Why is this dataset interesting?  Why do you want to analyze it?")
    print("This NFL dataset from 1999 to 2022 is interesting because it provides a comprehensive view of team performance over more than two decades. The data includes metrics such as passing yards, rushing yards, touchdowns, fumbles, and more. By analyzing this dataset, I can gain insights into how strategies have evolved over time, identify correlations between offensive/defensive stats and success, and explore trends in team performance. It also offers an opportunity to compare how different teams adapt to changes in play style over time.")
    print("\n")
    
    # Q3 Summary statistics
    print("###Q3### Display some summary statistics about your dataset.")
    # Load the dataset 
    df = pd.read_csv('Discussion Question\yearly_team_data.csv')
    # Displaying summary statistics for the dataset
    summary_stats = df.describe()

    # Displaying the summary statistics for specific columns of interest
    columns_of_interest = ['total_snaps', 'yards_gained', 'touchdown', 'passing_yards', 
                        'rushing_yards', 'interception', 'wins', 'losses']

    print(summary_stats[columns_of_interest])
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