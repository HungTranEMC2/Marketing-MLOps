# Marketing-MLOps
## Brief Summary
This project demonstrate the complete lifecycle of a data science initiative. It begins with Extracting data from an API, followed by transformation,
and loading it into a database. The next phase involves exploring and analyzing the dataset to understand its distribution and statistical properties.
During this stage, various visualization techniques are employed to gain clearer insights into the data, Subsequently, machine learning algorithms are 
applied to make predictions, and the models are thoroughly evaluated. Finally, the project is deployed the model into a web application 

# Data_Engineer:
This project show case the process of extracting,transforming, and loadking data from an API into a local MySQL database.

## Folder Structure
- **extract_and_transform.py**: /n/
		. **Description**: Script to download the `marketing.csv` dataset from the API /n/
		. **Execution**: Run `python extract_and_transform.py` to execute the script.


- **Load.py**:
		. **Description**: Script to load the dataset into the `customer_purchase` database, specifically into the `customer_purchase` table.
	 	. **Executuin**: Run `Load.py` to execute the sript

## Database Configuration:
- **Local MySQL Database**: the database is hosted locally on your computer. Ensure that the connection detail in the scripts are correctly
configured to connect to your local MySQL instance


### Data_Analysis:
	This folder contain the Exploration and Analysis part of the project
 	- 'EDA.ipynb': This is the jupyter notebook that contain the statistical and visualization of the dataset. 

### Data_Science: 
	This folder contain the Machine Learning part of the project
	- 'models.ipynb': this jupyter notebook contain the comparison between 3 models which are Linear_Regression (base model), XGBoost, and Random Forest 
	After comparing evaluation metrics, XGBoost shows as the best fit model compare to other 2 with the lowest RMSE score
	

    
