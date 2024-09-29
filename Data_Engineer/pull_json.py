from fastapi import FastAPI
import requests
import json
import os 


app = FastAPI()

@app.get('/dataset/{dataset_id}')
def get_dataset(dataset_id: int):
    url = f"https://www.openml.org/api/v1/json/data/{dataset_id}"
    response = requests.get(url)
    data = response.json()

    #Create 'data' director if it does not exist
    os.makedirs('data', exist_ok = True)

    #Save JSON to local file 
    json_file_path = f'data/dataset_{dataset_id}.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)
    
    return {"message": 'Dataset saved'}