# Marketing-MLOps
![image](https://github.com/user-attachments/assets/349e5367-2e88-499a-9025-37c0338f522b)

## Brief Summary
This project demonstrate the complete lifecycle of a data science initiative. It begins with Extracting data from an API, followed by transformation,
and loading it into a database. The next phase involves exploring and analyzing the dataset to understand its distribution and statistical properties.
During this stage, various visualization techniques are employed to gain clearer insights into the data, Subsequently, machine learning algorithms are 
applied to make predictions, and the models are thoroughly evaluated. Finally, the project is deployed the model into a web application 

# Data_Engineer:
This project show case the process of extracting,transforming, and loadking data from an API into a local MySQL database.

## Folder Structure
- `extract_and_transform.py`:

  
  - **Description**: Script to download the `marketing.csv` dataset from the API.

  - **Execution**: Run `python extract_and_transform.py` to execute the script.


- `Load.py`:

  
  - **Description**: Script to load the dataset into the `customer_purchase` database, specifically into the `customer_purchase` table.

  
  - **Executuin**: Run `Load.py` to execute the sript.

## Database Configuration:
- **Local MySQL Database**: the database is hosted locally on your computer. Ensure that the connection detail in the scripts are correctly
configured to connect to your local MySQL instance.


# Data_Analysis:
This folder contain the Exploration and Analysis part of the project

## Content:
- `EDA.ipynb`:
 
  - **Description**: This is the jupyter notebook that contain the statistical and visualization of the dataset. It include the statistical summary and visualization to understand data better
 
    
  - **Execution**:  Open the notebook in Jupyter and run the cells sequentially to perform the analysis.

# Data_Science
This folder contains the machine learning part of the project.

## Contents
- `models.ipynb`:


  - **Description**: This Jupyter notebook compares three machine learning models: Linear Regression (base model), XGBoost, and Random Forest.


  - **Sections**:
    
    - **Model Training**: Steps to train each of the three models.
      
    - **Evaluation Metrics**: Comparison of models based on evaluation metrics such as RMSE (Root Mean Squared Error).
      
    - **Results**: Analysis showing that XGBoost is the best fit model with the lowest RMSE score.
      
  - **Execution**: Open the notebook in Jupyter and run the cells sequentially to train the models and compare their performance.
  
- `model_xgb.py`: This script contains the implementation of the XGBoost model for generating predictions. To create the necessary pickle files for use in the Data App, run the following command:

  
        `py model_xgb.py'

- `model_random_forest.py`: This script contains the implementation of the Random Forest model for generating predictions. To create the necessary pickle files for use in the Data App, run the following command:


      `py model_random_forest.py`

  
# Data_Application
This folder contains the deployment part of the project.



