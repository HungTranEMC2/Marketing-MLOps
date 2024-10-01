import pandas as pd
import numpy as np 
import os
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error as mea
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


import warnings 
#Ignore all warnings
warnings.filterwarnings('ignore')

def get_data():
    # Import the dataset
    os.chdir('..')
    data = pd.read_csv('./Data_Engineer/data/marketing.csv')
    data.drop(columns = ['Unnamed: 0'], inplace= True)
    return data

      
class ModelRandomForest:
    def __init__(self, data):
        self.data = data

    
    def run(self):
        df = get_data()
        
        #Apply label encoding the categorical columns
        cols = ['gender','age','city_category','stay_in_current_city_years']
        label = LabelEncoder()
        
        for col in cols:
            df[col] = label.fit_transform(df[col])
            
        #Assign y = purchase_amount, because y is a targetd variable, the rest of the columns assign in X
        X = df.drop(columns =['purchase_amount'])
        y = df['purchase_amount']
        
        #Split the dataset into training and testing set 
        X_train, X_test, y_train, y_test = train_test_split(X,y ,random_state= 42, test_size= 0.2)
        
        random_forest_model = RandomForestRegressor(n_jobs = 1)
        random_forest_model.fit(X_train,y_train)
        
        #Save the model to a pickle file
        with open('./Data_Science/model_random_forest.pkl','wb') as file:
            pickle.dump(random_forest_model,file)
            
        random_forest_output = random_forest_model.predict(X_test)
        random_forest_output = pd.DataFrame(random_forest_output)
        random_forest_output.to_csv('random_forest_output.csv')    
        print('The model run successfully and has been saved to model_random_forest.pkl file')       
        return random_forest_output

if __name__ == '__main__':
    df = get_data
    model = ModelRandomForest(df)
    output = model.run()
    print('The Pipeline is completed')
        