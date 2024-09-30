from fastapi import FastAPI
import pandas as pd 
import requests
import asyncio
from contextlib import asynccontextmanager
import json
import os 
import uvicorn

app = FastAPI()

@app.get('/dataset/{dataset_id}')
def extract_dataset(dataset_id: int):
     # URL to fetch the dataset description
    description_url = f"https://www.openml.org/api/v1/json/data/{dataset_id}"
    description_response = requests.get(description_url)
    description_data = description_response.json()

    # Extract the URL of the actual dataset
    dataset_url = description_data['data_set_description']['url']

    # Fetch the actual dataset
    dataset_response = requests.get(dataset_url)
    dataset_content = dataset_response.content

    # Create 'data' directory if it does not exist
    os.makedirs('data', exist_ok=True)

    # Save the dataset to a local file
    dataset_file_path = f'data/{dataset_id}.csv'
    with open(dataset_file_path, 'wb') as dataset_file:
        dataset_file.write(dataset_content)

    return {"message": 'Dataset saved'}

def clean_data(df):
    column_names = ['gender','age','occupation','city_category','stay_in_current_city_year','marital_status','product_category_1','product_category_2','product_category_3','purchase_amount']
    df = pd.read_csv('data/41540.csv',skiprows = 14,names = column_names)
    df.to_csv('data/marketing.csv')
    return df
if __name__ == '__main__':
    #Extract dataset from API
    extract_dataset(41540)
    #Transform Dataset
    df = clean_data('dataset_41540.csv')
    #Remove the extra files 
    os.remove('data/41540.csv')
    print('Extraction process is completed ')
    
    