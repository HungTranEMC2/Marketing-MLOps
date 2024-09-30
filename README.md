# Marketing-MLOps
## Brief Summary
This project demonstrate the complete lifecycle of a data science initiative. It begins with Extracting data from an API, followed by transformation,
and loading it into a database. The next phase involves exploring and analyzing the dataset to understand its distribution and statistical properties.
During this stage, various visualization techniques are employed to gain clearer insights into the data, Subsequently, machine learning algorithms are 
applied to make predictions, and the models are thoroughly evaluated. Finally, the project is deployed the model into a web application 

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
	

    