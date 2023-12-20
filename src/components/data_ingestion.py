import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #Doesnt require constructor
class DataIngestionConfig:#Data class with 3 attributes
    train_data_path: str=os.path.join('artifact',"train.csv")
    test_data_path: str=os.path.join('artifact',"test.csv")
    raw_data_path: str=os.path.join('artifact',"raw.csv")

class DataIngestion:
    def __init__(self): #Constructor
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') #Reading Dataset(Can be done via mongoDB as well)

            logging.info('Read the dataset')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test split")

            train_set,test_set = train_test_split(df,test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion Completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj=DataIngestion()#object
    obj.initiate_data_ingestion()#function


# import os
# import sys
# from src.exception import CustomException
# from src.logger import logging
# import pandas as pd

# from sklearn.model_selection import train_test_split

# class DataIngestionConfig:
#     def __init__(self):
#         self.train_data_path = os.path.join('artifact', 'train.csv')
#         self.test_data_path = os.path.join('artifact', 'test.csv')
#         self.raw_data_path = os.path.join('artifact', 'raw.csv')

# class DataIngestion:
#     def __init__(self):  # Constructor
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         logging.info("Entered Ingestion method or component")
#         try:
#             df = pd.read_csv('notebook\data\stud.csv')  # Reading Dataset (Can be done via mongoDB as well)

#             logging.info('Read the dataset')

#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

#             logging.info("Train Test split")

#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

#             logging.info("Data Ingestion Completed")

#             return (
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             )
#         except Exception as e:
#             raise CustomException(e, sys)

# if __name__ == "__main__":
#     obj = DataIngestion()  # object
#     obj.initiate_data_ingestion()  # function
