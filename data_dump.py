import pymongo
import pandas as pd
import json
from predictive_maintenance.config import mongo_client

DATABASE_NAME = "Predictive"
COLLECTION_NAME = "maintenance"
DATA_FILE_PATH = "C:\\Users\\apurv\\OneDrive\\Desktop\\Internship\\Predictive_Maintenance\\predictive_maintenance\\jetengine1.csv"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #Convert dataframe into JSON so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values()) 
    print(json_record[0])

    #insert converted json to mongo db  
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

