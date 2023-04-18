# training code
# train model and look for accuracy.
# model selection

import os
import sys

from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression   
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException

from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainingConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTraining:
    def __init__(self):
        self.model_train_config = ModelTrainingConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Split train and test data")

            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            #create dictionary of models
            #perform hyperparameter tuning

            models ={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regrssion": KNeighborsRegressor(),
                "XGBRegression": XGBRegressor(),
                "CatBoosting Regression": CatBoostRegressor(),
                "AdaBoost": AdaBoostRegressor()
            }

            # identify the model that performs well
            model_report:dict = evaluate_model(x_train=X_train, y_train=y_train, x_test = X_test, y_test = y_test, models = models)
            
            #get best model score
            best_model_score = max(sorted(model_report.values()))

            #get model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info("Best model found on train and test dataset")

            #load it to pkl file if we need to use it further           

            save_object(
                file_path=self.model_train_config.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)
            r2_scores = r2_score(y_test, predicted)
            return r2_scores

        except Exception as e:
            raise CustomException(e, sys)