"""Questions
1. How do you plot a histogram in Seaborn?  
2. Plot a histogram with NAs dropped.
3. How do you set the color for a histogram?
4.  What type of plot would allow you to compare two continuous features?  Give an example of code.
5. Give example of a correlation plot.
6. Change the figure size of your plot(s).
You can use any dataset for examples to these questions. Some datasets can be found using seaborn: https://seaborn.pydata.org/generated/seaborn.load_dataset.html  
"""

"""Sample output
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
###------------------------------------------------------------------------------------------------------ 
"""
Q1. How do you plot a histogram in Seaborn?  
You can use Seaborn's histplot() function to plot a histogram
"""
def q1_histogram(data):
    

    # Plot a histogram of the 'flipper_length_mm' feature
    sns.histplot(data['flipper_length_mm'])
    plt.show()
    
###------------------------------------------------------------------------------------------------------ 
"""
Q2. Plot a histogram with NAs dropped.
To drop missing values before plotting, you can use the .dropna() function
"""
def q2_histogram_dropNA(data):
    # Plot a histogram after dropping NAs
    sns.histplot(data['flipper_length_mm'].dropna())
    plt.show()
###------------------------------------------------------------------------------------------------------ 
"""
Q3. How do you set the color for a histogram?
You can set the color of the histogram using the color argument
"""
def q3_histogram_color(data):
    # Set the color of the histogram to blue
    sns.histplot(data['flipper_length_mm'].dropna(), color='blue')
    plt.show()
###------------------------------------------------------------------------------------------------------ 
"""
Q4. What type of plot would allow you to compare two continuous features?  Give an example of code.
A scatter plot is commonly used to compare two continuous features
"""
def q4_scatterplot(data):
    # Scatter plot comparing 'flipper_length_mm' and 'body_mass_g'
    sns.scatterplot(x='flipper_length_mm', y='body_mass_g', data=data)
    plt.show()

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q5. Give example of a correlation plot.
A heatmap shows the correlation between numerical features.
"""

###------------------------------------------------------------------------------------------------------  
def q5_heatmap(data):
    # Calculate the correlation matrix
    matrix = data[['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'bill_depth_mm']].corr()

    # Plot the correlation heatmap
    sns.heatmap(matrix, annot=True, cmap='coolwarm')
    plt.show()

###------------------------------------------------------------------------------------------------------ 
"""
Q6. Change the figure size of your plot(s).
You can change the figure size using plt.figure()
"""
def q6_figsize(data):
    # Change the figure size for a histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['flipper_length_mm'].dropna())
    plt.show()


###------------------------------------------------------------------------------------------------------  
    
def main():
    # Load a dataset (e.g., the 'penguins' dataset)
    data = sns.load_dataset('penguins')
    
    # Q1 Histogram in seaborn
    print("###Q1### How do you plot a histogram in Seaborn?  ")
    print("You can use Seaborn's histplot() function to plot a histogram")
    q1_histogram(data)
    print("\n")
    
    # Q2 Plot a histogram with NAs dropped.
    print("###Q2### Plot a histogram with NAs dropped.")
    print("To drop missing values before plotting, you can use the .dropna() function")
    q2_histogram_dropNA(data)
    print("\n")
    
    # Q3 Set color for a histogram
    print("###Q3### How do you set the color for a histogram?")
    print("You can set the color of the histogram using the color argument")
    q3_histogram_color(data)
    print("\n")
    
    # Q4  Compare two continuous features
    print("###Q4### What type of plot would allow you to compare two continuous features?  Give an example of code.")
    print("A scatter plot is commonly used to compare two continuous features")
    q4_scatterplot(data)
    print("\n")
    
    # Q5  Correlation plot
    print("###Q5### Give example of a correlation plot.")
    print("A heatmap shows the correlation between numerical features.")
    q5_heatmap(data)
    print("\n")
    
    # Q6  figure size of plots
    print("###Q6### Change the figure size of your plot(s).")
    print("You can change the figure size using plt.figure()")
    q6_figsize(data)
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