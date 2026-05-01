"""You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.



Get the number of survivors by gender (Sex).
Get the number of non-survivors by gender (Sex).
Get the number of survivors by embarkation location (Embarked_S).
Get the number of non-survivors by embarkation location (Embarked_S).
Calculate the percentage of children (Age < 18) who survived.
Calculate the percentage of adults (Age >= 18) who survived.
Get the median age of survivors.
Get the median age of non-survivors.
Get the median fare of survivors.
Get the median fare of non-survivors.


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


Note: Refer to the visible test case for better reference.You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.



Get the number of survivors by gender (Sex).
Get the number of non-survivors by gender (Sex).
Get the number of survivors by embarkation location (Embarked_S).
Get the number of non-survivors by embarkation location (Embarked_S).
Calculate the percentage of children (Age < 18) who survived.
Calculate the percentage of adults (Age >= 18) who survived.
Get the median age of survivors.
Get the median age of non-survivors.
Get the median fare of survivors.
Get the median fare of non-survivors.


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


Note: Refer to the visible test case for better reference."""
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)



# 1
print(data[data['Survived'] == 1]['Sex'].value_counts())

# 2
print(data[data['Survived'] == 0]['Sex'].value_counts())

# 3
print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

# 4
print(data[data['Survived'] == 0]['Embarked_S'].value_counts())

# 5
children = data[data['Age'] < 18]
print(children['Survived'].mean())

# 6
adults = data[data['Age'] >= 18]
print(adults['Survived'].mean())

# 7
print(data[data['Survived'] == 1]['Age'].median())

# 8
print(data[data['Survived'] == 0]['Age'].median())

# 9
print(data[data['Survived'] == 1]['Fare'].median())

# 10
print(data[data['Survived'] == 0]['Fare'].median())