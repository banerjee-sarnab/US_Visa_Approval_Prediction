import os
from datetime import date
from urllib.parse import quote_plus

DATABASE_NAME = "US_Visa"
COLLECTION_NAME = "Visa_Data"
username = "sarnab17"
password = quote_plus("Sarnab@2002") 
MONGODB_URL_KEY = f"mongodb+srv://{username}:{password}@cluster0.f0rnzlp.mongodb.net/?appName=Cluster0"
PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
FILE_NAME: str = "usvisa.csv"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Visa_Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

