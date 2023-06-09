# once the data is read we need to transform the data.
# EDA, handling missing value, handle categorical and numerical data, feature engineering

import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

#column transformer used to create pipeline - onehotencoder, standardscale etc.,

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()        

    def get_data_transformer_obj(self):
        try:
            numerical_features = ['writing_score', 'reading_score']
            categorical_features = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course',
            ]

            #create a numerical pipeline, handle missing values
            #this pipeline will run on train dataset
            '''
            imputer = to handle missing values
            StandardScaler = Standardize features by removing the mean and scaling to unit variance.
            The standard score of a sample x is calculated as:
            z = (x - u) / s
            where u is the mean of the training samples or zero if with_mean=False, and s is the standard deviation of the training samples or one if with_std=False.
            '''
            
            num_pipeline = Pipeline(
                steps= [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
                ]
            )
            logging.info(f"Numerical columns: {numerical_features} ")

            cat_pipeline = Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_features} ")

            #combine cat and num pipeline together
            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_features),
                ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    

    #data transformation techniques
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and Test data is read")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_obj()
            target_column_name = 'math_score'
            numerical_features = ['writing_score', 'reading_score']

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            #print(input_feature_train_df)

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            #print(input_feature_test_df)

            logging.info("Applying preprocessing on train and test data.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            # print("input_feature_train_arr :", input_feature_train_arr)
            # print("input_feature_test_arr :", input_feature_test_arr)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # print("train_arr: ", train_arr)
            # print("Test_arr: ", test_arr)

            logging.info("Preprocessing object saved")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr, 
                test_arr, 
                self.data_transformation_config.preprocessor_obj_file_path
            )



        except Exception as e:
            raise CustomException(e, sys)