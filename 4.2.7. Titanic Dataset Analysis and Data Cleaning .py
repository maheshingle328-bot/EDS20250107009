"""You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.



Calculate the survival rate by class.
Calculate the survival rate by embarkation location (Embarked_S).
Calculate the survival rate by family size (FamilySize).
Calculate the survival rate by being alone (IsAlone).
Get the average fare by passenger class (Pclass).
Get the average age by passenger class (Pclass).
Get the average age by survival status (Survived).
Get the average fare by survival status (Survived).
Get the number of survivors by class (Pclass).
Get the number of non-survivors by class (Pclass).


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
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


print(data.groupby('Pclass')['Survived'].mean())

# 2
print(data.groupby('Embarked_S')['Survived'].mean())

# 3
print(data.groupby('FamilySize')['Survived'].mean())

# 4
print(data.groupby('IsAlone')['Survived'].mean())

# 5
print(data.groupby('Pclass')['Fare'].mean())

# 6
print(data.groupby('Pclass')['Age'].mean())

# 7
print(data.groupby('Survived')['Age'].mean())

# 8
print(data.groupby('Survived')['Fare'].mean())

# 9
print(data[data['Survived'] == 1]['Pclass'].value_counts())

# 10
print(data[data['Survived'] == 0]['Pclass'].value_counts())