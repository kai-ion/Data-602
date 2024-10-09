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
###------------------------------------------------------------------------------------------------------ 
"""
Q1. How do you plot a histogram in Seaborn?  
"""
def q1_histogram():
    # Load a dataset (e.g., the 'penguins' dataset)
    data = sns.load_dataset('penguins')

    # Plot a histogram of the 'flipper_length_mm' feature
    sns.histplot(data['flipper_length_mm'])
    plt.show()
    
###------------------------------------------------------------------------------------------------------ 
"""
Q2. Plot a histogram with NAs dropped.
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q3. How do you set the color for a histogram?

"""

###------------------------------------------------------------------------------------------------------ 
"""
Q4. What type of plot would allow you to compare two continuous features?  Give an example of code.
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q5. Give example of a correlation plot.
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q4. Change the figure size of your plot(s).
"""

###------------------------------------------------------------------------------------------------------  
    
def main():
    # Q1 Histogram in seaborn
    print("###Q1### How do you plot a histogram in Seaborn?  ")
    print("You can use Seaborn's histplot() function to plot a histogram")
    q1_histogram()
    print("\n")
    
    # Q2 Plot a histogram with NAs dropped.
    print("###Q2### Plot a histogram with NAs dropped.")
    
    
    print("\n")
    
    # Q3 Set color for a histogram
    print("###Q3### How do you set the color for a histogram?")
    
    print("\n")
    
    # Q4  Compare two continuous features
    print("###Q4### What type of plot would allow you to compare two continuous features?  Give an example of code.")
    
    print("\n")
    
    # Q5  Correlation plot
    print("###Q5### Give example of a correlation plot.")
    
    print("\n")
    
    # Q6  figure size of plots
    print("###Q5### Change the figure size of your plot(s).")
    
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