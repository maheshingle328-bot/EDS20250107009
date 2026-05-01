"""You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset. For each question, perform necessary data cleaning, transformations, and calculations as required.



Display the first 5 rows of the dataset.
Display the last 5 rows of the dataset.
Get the shape of the dataset (number of rows and columns).
Get a summary of the dataset (using .info()).
Get basic statistics (mean, standard deviation, etc.) of the dataset using .describe().
Check for missing values and display the count of missing values for each column.
Fill missing values in the ‘Age’ column with the median age.
Fill missing values in the ‘Embarked’ column with the most frequent value (mode()).
Drop the ‘Cabin’ column due to many missing values.
Create a new column, 'FamilySize' by adding the 'SibSp' and 'Parch' columns.


The Titanic dataset contains columns as shown below,

PassengerId

Survived

Pclass

Name

Sex

Age

SibSp

Parch

Ticket

Fare

Cabin

Embarked
Sample Data:

PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S
9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,11.1333,,S
10,1,2,"Nasser, Mrs. Nicholas (Adele Achem)",female,14,1,0,237736,30.0708,,C


Note: Refer to the visible test case for better reference.

"""
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
print(data.head())
# 1. Display the first 5 rows of the dataset


# 2. Display the last 5 rows of the dataset
print(data.tail())

# 3. Get the shape of the dataset
print(data.shape)

# 4. Get a summary of the dataset (info)
data.info()
print("None")
# 5. Get basic statistics of the dataset
print(data.describe())

# 6. Check for missing values
print(data.isnull().sum())

# 7. Fill missing values in the ‘Age’ column with the median age
data['Age'].fillna(data['Age'].median(),inplace=True)

# 8. Fill missing values in the ‘Embarked’ column with the mode
data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

# 9. Drop the ‘Cabin’ column due to many missing values
data.drop('Cabin',axis=1,inplace=True)

# 10. Create a new column 'FamilySize’ by adding ‘SibSp' and ‘Parch'
data['FamilySize']=data['SibSp']+data['Parch']