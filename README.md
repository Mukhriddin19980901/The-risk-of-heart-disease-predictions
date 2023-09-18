# Heart disease risk prediction model 

<img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/symptom.png" width='800' height='500' />


****Heart disease****, also known as **cardiovascular disease** (CVD), refers to a group of conditions that affect the heart and blood vessels. It is a leading cause of morbidity and mortality worldwide. Common types of heart disease include coronary artery disease (CAD), heart failure, arrhythmias, and heart valve problems.
1. **Data**
   - I used a [data](https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/heart.csv) which is 12Kb csv  consists of 14 columns(dtypes = 1 float 13 integer columns) and 304 rows.It gives the results patients according to their age,gender,health conditions and external factors
   - Column names' meanings :

> Age - patients' age range between 77 and 29
  
> Sex - Gender of the person [1: Male, 0: Female]

> cp - Constrictive pericarditis = is a form of diastolic heart failure that arises because an inelastic pericardium inhibits cardiac filling.[1-Typical Type 1 Angina; 2- Atypical Type Angina; 3- Non-angina pain; 4-Asymptomatic)

> trestbps - the reading of the resting blood pressure.
 
> chol - cholestrol (high cholesterol can increase your risk of heart disease).
 
> fbs - Fasting glucose level
 
> restecg - the resting electrocardiographic result
 
> thalach - the maximum heart rate
 
> exang - the exercise induced angina
 
> oldpeak - ST depression induced by exercise relative to rest
 
> slope - Slope of the Peak Exercise ST segment
 
> ca - Number of major vessels colored by fluoroscopy
 
> thal - 3 – Normal, 6 – Fixed Defect, 7 – Reversible Defect
 
> target - disease risk [1 - yes , 0 - No]
> 

<img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/1.png" width='500' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/2.png" width='600' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/3.png" width='600' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/4.png" width='600' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/5.png" width='600' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/6.png" width='600' height='300' />

 2.**Vizualization** 
   - ***Men***
- The data shows that the more men patients are older,the more cholestrol they gain.
- Surprisingly the risk of heart disease is higher in the men who are thinner.The risk arises among skinny people of the age group between 50 and 60.  
- People who have family members that have had a heart attack may have a higher chance of having a heart attack
- Both low glucose level and impaired fasting glucose should be considered as predictors of risk for stroke and coronary heart disease
  - ***Women***
- There were no differences between the two groups in major clinical features
- As far as women patients concerned the risk is high between thinner and middle age(35-55)ladies.Only about 60% of women around 60 may not complain about heart disease.The oldest women patients are likely to have serius heart problems.obesity is the same issue when they get older.
- ST segment depression induced during the active phase of the exercise stress test, and group 2 comprised patients with no ST segment changes during exercise but who exhibited a significant ST segment depression during the recovery phase of the test
 3.**Code**
 Explanation:

Import Libraries:

import pandas as pd: Imports the pandas library, which provides data structures and data analysis tools.
import seaborn as sb: Imports Seaborn, a data visualization library based on Matplotlib.
import matplotlib.pyplot as plt: Imports Matplotlib for plotting.
from sklearn.model_selection import train_test_split: Imports a function for splitting data into training and testing sets.
from sklearn.naive_bayes import GaussianNB: Imports the Gaussian Naive Bayes model.
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score: Imports metrics for model evaluation.
Load Data:

datas = pd.read_csv(file_path): Loads data from a CSV file specified by file_path.
Plotting with Seaborn:

Uses Seaborn's lmplot to create a scatter plot with a linear regression fit for the given data (age vs chol) with color differentiation based on the target and separate plots for each gender.
Data Preparation:

Separates the features (X) and target variable (y).
Splits the data into training and testing sets using 80% for training and 20% for testing.
Model Training:

Uses a Gaussian Naive Bayes classifier and fits it to the training data.
Model Evaluation: scores  = ***78 % accuracy*** rate which is not bad 

<img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/7.png" width='500' height='300' />

Calculates and prints accuracy, F1 score, precision, and recall for the trained model using the testing data. The results are ~ 78.6% , ~ 78.5% ,77.1% , 84.3% respectively
It's important to note that in the code provided, file_path is used to denote the path to the CSV file containing the dataset, it's  defined in the code snippet. Make sure to replace file_path with the actual path to your CSV file before running the [code](https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/heart_disease_predictions.ipynb).
