# Data Analysis of IMDb Movies Dataset

## Overview
This project demonstrates how to perform data analysis using the Pandas library in Python. The dataset used for this analysis is the IMDb movies dataset, which provides a rich variety of attributes for understanding and deriving insights from movie data. The goal is to explore and manipulate the dataset to gain insights and perform various data operations.

## Introduction

If you are an aspiring Data Analyst or Data Scientist, you are likely aware that **Data Wrangling** is one of the most crucial and time-consuming steps in any Data Science or Machine Learning project. It involves cleaning, transforming, and preparing data for analysis, which is essential for accurate results.

Python offers a powerful and popular library called **Pandas**, built on top of **Numpy**, which provides numerous data structures and operations for data manipulation and analysis. Pandas has become one of the most widely used tools in data science, significantly enhancing the efficiency of data cleaning and exploratory data analysis (EDA).

In this project, we will explore two of Pandas' most important data structures:

1. **Series**: A one-dimensional labeled array.
2. **DataFrame**: A two-dimensional table of data with labeled axes.

Additionally, we will conduct hands-on **Exploratory Data Analysis (EDA)** using a dataset of movies, demonstrating some of the most useful Pandas operations and functionalities. This guide is beginner-friendly, offering insights into real-world data analysis.

### Learning Objectives

- Understand the pivotal role of data wrangling in data science and machine learning workflows.
- Recognize how Pandas simplifies data cleaning, manipulation, and analysis.
- Differentiate between Pandas' **Series** and **DataFrame** data structures.
- Learn the one-dimensional and two-dimensional representations of Series and DataFrame.
- Gain hands-on experience creating Series and DataFrame objects from various sources, including lists, arrays, dictionaries, and files.

### Steps for Data Analysis

1. **Reading the Data**: Load the IMDb dataset from a `.csv` file into a Pandas DataFrame.
2. **Viewing the Data**: Get a glimpse of the dataset structure and contents.
3. **Basic Information**: Use Pandas to understand the dimensions, data types, and structure of the dataset.
4. **Data Selection - Indexing and Slicing**: Select subsets of the data based on rows and columns.
5. **Data Selection - Conditional Filtering**: Apply filters to retrieve data that meet specific conditions.
6. **Groupby Operations**: Group data based on categorical variables and perform aggregate operations.
7. **Sorting Operations**: Sort the data by specific columns for better organization and analysis.
8. **Handling Missing Values**: Identify and deal with missing data to ensure a clean dataset.
9. **Dropping Columns and Null Values**: Remove irrelevant columns or rows with missing data.
10. **Apply Functions**: Use the `apply()` function to execute custom operations on rows or columns.


## Dataset
We will be working with the fascinating **IMDb Movies Dataset**, which is open-source and available for download from Kaggle: [IMDb Movies Dataset](https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data).

The dataset used in this project contains information about movies, including their title, year of release, genre, and ratings. It is available in CSV format, which is easy to read and manipulate using Pandas.

## Prerequisites
To run the project, you'll need the following:
- Python 3.11
- Pandas library (`pip install pandas`)
- jupyter library (`pip install jupyter`)
- Add Jupyter to the Environment Path

    - If Jupyter is already installed but not recognized, the issue might be with your system’s PATH variable. You can try launching it using the full path (`python -m notebook`)

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:kai-ion/Data-602.git
    ```
2. Navigate to the project directory:
    ```bash
    cd '.\Data Analysis on IMDB movies data\'
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```



## How to Run
1. **To open the notebook in your browser:**

   ```bash
   python -m notebook analysis.ipynb
   ```

2. **To execute all cells and save the output to a new file:**

   ```bash
   python -m jupyter nbconvert --to notebook --execute analysis.ipynb
   ```

3. **To execute all cells and overwrite the original file:**

   ```bash
   python -m jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
   ``` 

These commands will run the notebook as per your preference.

## Project Features
- **Data Loading**: Read the dataset into a Pandas DataFrame.
- **Data Cleaning**: Handle missing values, duplicates, and inconsistent data types.
- **Data Exploration**: Perform summary statistics, group data, and visualize insights.
- **Data Analysis**: Analyze trends in movies' release years, ratings, genres, and more.

## Additional Resources
For a detailed step-by-step guide on using Pandas for data analysis with IMDb movies data, refer to this comprehensive guide:

[A Comprehensive Guide to Data Analysis using Pandas - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/05/a-comprehensive-guide-to-data-analysis-using-pandas-hands-on-data-analysis-on-imdb-movies-data/)

[Quick Guide to Data Analysis Using Pandas - GitHub Repository](https://github.com/lakshanagv/Complete-guide-to-data-analysis-using-Python---IMDB-movies-data/blob/main/Quick%20guide%20to%20Data%20Analysis%20using%20Pandas.ipynb)

## License
This project is licensed under the MIT License.
