## This is a complete machine learning project

##### Reference: https://www.youtube.com/watch?v=S_F_c9e2bz4&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG 

### 1. Create a new environment
##### conda create -p venv python==3.8 -y

### 2. Activate venv
##### conda activate venv/

### 3. Github commands

 - git init
 - git add
 - git commit -m "message"
 - git status
 - git branch -M main
 - git remote add origin repolink
 - git config --global user.name "username" 
 - git config --global user.email "email"
 - git push -u origin main

### 4. Add .gitignore file on github

### 5. Create src folder and build the package with setup.py and requirements.txt
- The libraries mentioned in the requirements.txt will be downloaded automatically
- Setup.py allows our ML application used as a package.

### 6. pip install -r requirements.txt
- It will install all the libraries mentioned in the requirements.txt

### 7. Create exception.py and logger.py 
- Handle the exception by writing the custom exceptions and log all those exception using logger.py file

### 8. Create notebook folder 
- Handle the EDA and Model Training process under project/notebook/data that holds dataset and all related python EDA code in ipynb file for reference in future.

### 9. Data Ingestion 
- Read the data from any source, we have read it from csv file in this project
- Split the data into train and test data.
- We have split it in 80-20 ratio
- save the split data in a artifact folder
- artifacts has train, test and original raw data.
- create the artifacts folder path -> makedir for the arifacts -> split the data into train and test -> save train, test and raw data into artifacts

### 10. Data Transformation
- Once the data is read from data ingestion we perform preprocessing in transformation.
- There are two types of data: Numerical data and Categorical data.
- We create numerical and categorical pipeline using ColumnTransformer.
- We handle the missing value in numerical data using sklearn.impute, SimpleImputer.
- we handle missing values in Categorical data using sklearn.preprocessing, OneHotEncoder 
- Normalize the data using StandardScaler.

### 11. Model Training
- we import all the regressor models from sklearn
- split the train and test data from the train_array and test_array we get from the data_transformation file.
- we evaluate each model to find the best model.
- evaluate_model() function is written in the utils.py file
- we identify the best model by calculating the r2_score on each model.

### 12. create prediction pipeline
- Automate the process of reading data from any source, load the model that works best for that kind of data, run the data through model and predict the value.
- In this project we have used flask to build front end.
- we are receving data from the webpage.
- pass the data through prediction pipeline.
- get the predicted output.
- post the prediction on webpage.

### 13. Deploy ML pipelines
- Make few config changes.
- we are using Elastic BeanStalk : AWS Elastic Beanstalk helps you deploy and manage web applications with capacity provisioning, app health monitoring, and more.
- create .ebextentions : config file for AWS Elastic Beanstalk
- - create python config file inside .ebextentions: python.config: to set up entry point of application.
- - WSGIPath: application:application , application is the app.py name, that's the entry point for our application.


### 14. Creating an Application in aws elastic beanstalk
- aws elastic beanstlk application, create application
- fill all the fields
-

### 15. Create codepipeline on AWS
- creating CI/CD pipeline usingh aws codepipeline.



