# import sys
# from US_Visa.logger import logging
# from US_Visa.exception import USvisaException


# logging.info("This is our custom log message.")

# try:
#     a = 1 / 0
# except Exception as e:
#     raise USvisaException(e, sys)

# from urllib.parse import quote_plus

# username = "sarnab17"
# password = quote_plus("Sarnab@2002") 
# MONGODB_URL_KEY = f"mongodb+srv://{username}:{password}@cluster0.f0rnzlp.mongodb.net/?appName=Cluster0"

# print(MONGODB_URL_KEY)


# import os

# mongo_db_url = os.getenv('MONGODB_URL_KEY')
# print(mongo_db_url)

from US_Visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

