# Marketing-MLOps
## Brief Summary
	This project showcase the full cycle development of a datascience project, from getting data from API, Transform, and Load it to database. 
	Then I provide Exploration and Analysis steps to understand the distribution, or statistical nature of the dataset, in this stage, I performed 
	multiple visualization technique to have more clear insight and picture about the data. 
	Next, I will apply machine learning Algorithms to get the prediction , and evaluate the models. 
	Last, I will deploy the model into the web app application 

### Data_Engineer:
	This folder show case the process I extract and Transform data from API
	- 'extract_and_transform.py' : this is the python file that can download the dataset marketing.csv from API whenever we run the code.
					'py extract_and_transform.py'
	- 'Load.py': This is the python file that I push the dataset into the customer_purchase database under customer_purchase table.
			. I host the local MYSQL database in my computer, so all the connection in the code that is linked to the MySQL in my laptop

### Data_Analysis:
	This folder contain the Exploration and Analysis part of the project
 	- 'EDA.ipynb': This is the jupyter notebook that contain the statistical and visualization of the dataset. 

### Data_Science: 
	This folder contain the Machine Learning part of the project
	- 'models.ipynb': this jupyter notebook contain the comparison between 3 models which are Linear_Regression (base model), XGBoost, and Random Forest 
	After comparing evaluation metrics, XGBoost shows as the best fit model compare to other 2 with the lowest RMSE score
	

    