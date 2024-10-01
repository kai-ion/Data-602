"""Questions
1. What is matplottlib and seaborn?  When would you choose one over the other?
2. Image you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?
3. Give an example of either a matplotlib or seaborn graphic (give code).  You may also reference an informative article.
4. Read the following:  https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio
What is the data-ink ratio? 
How can you use python libraries such as matplotlib, seaborn, plotly, etc. to incorporate this data-ink ratio in your visualizations?   
"""

"""Sample output
###Q1### What is matplottlib and seaborn?  When would you choose one over the other?
Matplotlib is a python plotting library in Python that lets you change appearance of charts, while Seaborn is built on top of Matplotlib and offers built-in themes and aesthetics for visualizations. Seaborn is easer to use and has more appealing graphs, whereas Matplotlib is better for customization.


###Q2### Imagin you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?

    - Use clear titles and labels for axes.
    - Choose colors and markers for readability.
    - Avoid clutter by minimizing elements.
    - Ensure the visualization is easy to interpret at a glance.
    - Provide context through annotations or legends.



###Q3### Give an example of either a matplotlib or seaborn graphic (give code).  You may also reference an informative article.
Chart opened
Chart closed


###Q4### Read the following:  https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio
What is the data-ink ratio?
How can you use python libraries such as matplotlib, seaborn, plotly, etc. to incorporate this data-ink ratio in your visualizations?

    The data-ink ratio is proportion of ink used to present actual data compared to the total ink used in a visualization, emphasizing the importance of maximizing data representation while minimizing non-essential ink.

    To incorporate this ratio in visualizations with libraries like Matplotlib or Seaborn, focus on simplifying charts by removing unnecessary elements, like excessive grid lines or decorative features, and ensuring the design highlights the data itself.
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q1. What is matplottlib and seaborn?  When would you choose one over the other?
Matplotlib is a python plotting library in Python that lets you change appearance of charts, while Seaborn is built on top of Matplotlib and offers built-in themes and aesthetics for visualizations. Seaborn is easer to use and has more appealing graphs, whereas Matplotlib is better for customization.
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q2. Image you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?
- Use clear titles and labels for axes.
- Choose colors and markers for readability.
- Avoid clutter by minimizing elements.
- Ensure the visualization is easy to interpret at a glance.
- Provide context through annotations or legends.
"""
###------------------------------------------------------------------------------------------------------ 
"""
Q3. Give an example of either a matplotlib or seaborn graphic (give code).  You may also reference an informative article.

"""
def q3_seaborn():
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Sample data
    tips = sns.load_dataset("tips")

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', s=100)
    plt.title('Scatter Plot of Tips vs. Total Bill')
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip ($)')
    plt.legend(title='Day & Time')
    plt.show()
    
###------------------------------------------------------------------------------------------------------ 
"""
Q4. Read the following:  https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio
What is the data-ink ratio? 
How can you use python libraries such as matplotlib, seaborn, plotly, etc. to incorporate this data-ink ratio in your visualizations? 

The data-ink ratio is proportion of ink used to present actual data compared to the total ink used in a visualization, emphasizing the importance of maximizing data representation while minimizing non-essential ink. 

To incorporate this ratio in visualizations with libraries like Matplotlib or Seaborn, focus on simplifying charts by removing unnecessary elements, like excessive grid lines or decorative features, and ensuring the design highlights the data itself.

"""

###------------------------------------------------------------------------------------------------------  
    
def main():
    # Q1 What is matplottlib and seaborn
    print("###Q1### What is matplottlib and seaborn?  When would you choose one over the other?")
    print("Matplotlib is a python plotting library in Python that lets you change appearance of charts, while Seaborn is built on top of Matplotlib and offers built-in themes and aesthetics for visualizations. Seaborn is easer to use and has more appealing graphs, whereas Matplotlib is better for customization.")
    print("\n")
    
    # Q2 guidelines and informative visuals
    print("###Q2### Imagin you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?")
    q2 = """
    - Use clear titles and labels for axes.
    - Choose colors and markers for readability.
    - Avoid clutter by minimizing elements.
    - Ensure the visualization is easy to interpret at a glance.
    - Provide context through annotations or legends.
    """
    
    print(q2)
    
    print("\n")
    
    # Q3 example of either a matplotlib or seaborn graphic
    print("###Q3### Give an example of either a matplotlib or seaborn graphic (give code).  You may also reference an informative article.")
    print("Chart opened")  
    q3_seaborn()
    print("Chart closed")  
    print("\n")
    
    # Q4  https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio
    print("###Q4### Read the following:  https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio")
    print("What is the data-ink ratio?")
    print("How can you use python libraries such as matplotlib, seaborn, plotly, etc. to incorporate this data-ink ratio in your visualizations?")
    
    q4 = """
    The data-ink ratio is proportion of ink used to present actual data compared to the total ink used in a visualization, emphasizing the importance of maximizing data representation while minimizing non-essential ink. 

    To incorporate this ratio in visualizations with libraries like Matplotlib or Seaborn, focus on simplifying charts by removing unnecessary elements, like excessive grid lines or decorative features, and ensuring the design highlights the data itself.
    """
    print(q4)    
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