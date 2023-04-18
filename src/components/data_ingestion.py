# code related to reading the data
# dividing the data set into train and test
# validation dataset

#read the data from data sources: could be from cloud, hadoop, mongodb etc.,

import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_train import ModelTraining, ModelTrainingConfig

@dataclass
class DataIngestionConfig:
    '''
    @dataclass is a class typically containing mainly data, used when only variables are ddefined in the class.
    The following are the inputs given to Data Ingestion component.
    The output is saved in the path mentioned.
    '''
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self) -> None:
        '''
        when the class is called it automatically calls the DataIngestionConfig() class 
        and gets the data ready in the given path for further processing.
        '''
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        '''
        Code to read data from database
        '''
        logging.info("Entered the Data Ingestion component")
        try:            
            df= pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train test split initiated")

            #saving all the train and test data into artifact folder
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is complete")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()

    train_array , test_array,_ = data_transformation.initiate_data_transformation(train_data, test_data)
    
    modeltraining = ModelTraining()
    modeltraining.initiate_model_training(train_array, test_array)

    print(modeltraining.initiate_model_training(train_array, test_array))

