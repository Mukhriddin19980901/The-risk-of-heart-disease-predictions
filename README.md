# Heart disease risk prediction model 

<img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/symptom.png" width='800' height='500' />


****Heart disease****, also known as **cardiovascular disease** (CVD), refers to a group of conditions that affect the heart and blood vessels. It is a leading cause of morbidity and mortality worldwide. Common types of heart disease include coronary artery disease (CAD), heart failure, arrhythmias, and heart valve problems.
1. **Data**
   - I used a [data](https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/heart.csv) which is 12Kb csv  consists of 14 columns(dtypes = 1 float 13 integer columns) and 304 rows.It gives the results patients according to their age,gender,health conditions and external factors
   - Column names' meanings :

> Age - patients' age range between 77 and 29
  
> Sex - Gender of the person [1: Male, 0: Female]

> cp - Constrictive pericarditis = is a form of diastolic heart failure that arises because an inelastic pericardium inhibits cardiac filling.[1-Typical Type 1 Angina; 2- Atypical Type Angina; 3- Non-angina pain; 4-Asymptomatic)

> trestbps - the reading of the resting blood pressure.
 
> chol - cholestrol (high cholesterol can increase your risk of heart disease).
 
> fbs - Fasting glucose level(Both low glucose level and impaired fasting glucose should be considered as predictors of risk for stroke and coronary heart disease).
 
> restecg - the resting electrocardiographic result
 
> thalach - the maximum heart rate
 
> exang - the exercise induced angina
 
> oldpeak - ST depression induced by exercise relative to rest
 
> slope - Slope of the Peak Exercise ST segment
 
> ca - Number of major vessels colored by fluoroscopy
 
> thal - 3 – Normal, 6 – Fixed Defect, 7 – Reversible Defect
 
> target - disease risk [1 - yes , 0 - No]
> 

<img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/1.png" width='500' height='300' /> <img src="https://github.com/Mukhriddin19980901/the-risk-of-heart-disease-predictions/blob/main/images/2.png" width='800' height='300' />

- The data shows that the more men patients are older,the more cholestrol they gain.But surprisingly the risk of heart disease is higher in the men who are thinner.The risk arises among skinny people of the age group between 50 and 60.

 - As far as women patients concerned the risk is high between thinner and middle age(35-55)ladies.Only about 60% of women around 60 may not complain about heart disease.The oldest women patients are likely to have serius heart problems.obesity is the same issue when they get older
