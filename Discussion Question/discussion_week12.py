"""Questions
1. What are the different types of machine learning? 
2. What is the difference between supervised and unsupervised machine learning? When would you use one method over another?
3. What is overfitting, how can you avoid it?
4. What is 'training' and 'test' set in a machine learning model?
5. How can you handle missing or corrupted data in a dataset? 
6. What are some applications of supervised machine learning? 
7. What is the KNN algorithm? (Write a brief description)
8. What are advantaged of the KNN algorithm? 
9. What are disadvantages of the KNN algorithm? 
"""

"""Sample output

"""
###------------------------------------------------------------------------------------------------------ 
"""
Q1. What are the different types of machine learning? 
"""
q1 = """Answer: 
There are several types of machine learning, each with special characteristics and applications. Some of the main types of machine learning algorithms are as follows:
- Supervised Learning: The model is trained on labeled data, learning the relationship between input features and target outputs (e.g., classification, regression).
- Unsupervised Learning: The model finds patterns and relationships in data without labeled outcomes (e.g., clustering, dimensionality reduction).
- Semi-Supervised Learning: A combination of labeled and unlabeled data is used, where the model learns from a small amount of labeled data and a large amount of unlabeled data.
- Reinforcement Learning: An agent interacts with an environment and learns to make decisions by receiving feedback in the form of rewards or penalties.
"""
    
###------------------------------------------------------------------------------------------------------ 
"""
Q2. What is the difference between supervised and unsupervised machine learning? When would you use one method over another?
"""
q2 = """Answer:
- Supervised Learning: The model is provided with labeled training data (input-output pairs) to learn the mapping from inputs to outputs. 
Use supervised learning when you have labeled data and need to predict outcomes, such as predicting stock prices or classifying emails.
- Unsupervised Learning: The model is provided with data that does not have labeled outputs. It looks for patterns or groupings in the data. 
Use unsupervised learning when you want to find patterns or groupings in unlabeled data, like customer segmentation or anomaly detection.
"""

###------------------------------------------------------------------------------------------------------ 
"""
Q3. What is overfitting, how can you avoid it?
"""
q3 = """Answer:
Overfitting is when a model learns too much from the training data, capturing noise and irrelevant details, resulting in poor generalization to new data.
To avoiding Overfitting:
- Use cross-validation.
- Apply regularization methods (L1, L2).
- Simplify the model by reducing the number of features or parameters.
- Gather more data or use data augmentation.
- Use early stopping during training for models like neural networks.
"""

###------------------------------------------------------------------------------------------------------ 
"""
Q4. What is 'training' and 'test' set in a machine learning model?
"""
q4 = """Answer:
- Training Set: A subset of the dataset used to train the model, where the model learns patterns from the input features and their corresponding outputs.
- Test Set: A separate subset that is not used during training but is used to evaluate the model's performance and generalization to unseen data.
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q5. How can you handle missing or corrupted data in a dataset?
"""
q5 = """Answer:
You can start wtih removing data by dropping rows or columns with missing values.
Or you can replace missing values with statistical methods (mean, median, mode) or use advanced methods like KNN or regression imputation.
Then you can add an additional column indicating whether data was missing, to give the model information about missingness.
"""
###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q6. What are some applications of supervised machine learning? 
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q7. What is the KNN algorithm? (Write a brief description)
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q8. What are advantaged of the KNN algorithm?
"""

###------------------------------------------------------------------------------------------------------  

###------------------------------------------------------------------------------------------------------ 
"""
Q9. What are disadvantages of the KNN algorithm? 
"""

###------------------------------------------------------------------------------------------------------  

def main():
    
    
    # Q1 Types of machine learning
    print("###Q1### What are the different types of machine learning?   ")
    print(q1)
    print("\n")
    
    # Q2 Supervised vs unsupervised ML
    print("###Q2### What is the difference between supervised and unsupervised machine learning? When would you use one method over another?")
    print(q2)
    print("\n")
    
    # Q3 Overfitting
    print("###Q3### What is overfitting, how can you avoid it?")
    print(q3)
    print("\n")
    
    # Q4  training and test set
    print("###Q4### What is 'training' and 'test' set in a machine learning model?")
    print(q4)
    print("\n")
    
    # Q5  Missing or corrupted data
    print("###Q5### How can you handle missing or corrupted data in a dataset?")
    
    print("\n")
    
    # Q6  applications of supervised ML
    print("###Q6### What are some applications of supervised machine learning? ")
    
    print("\n")
    
    # Q7  KNN
    print("###Q7### What is the KNN algorithm? (Write a brief description) ")
    
    print("\n")
    
    # Q8  Advantaged of KNN
    print("###Q8### What are advantaged of the KNN algorithm? ")
    
    print("\n")
    
    # Q9  applications of supervised ML
    print("###Q9### What are disadvantages of the KNN algorithm?  ")
    
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