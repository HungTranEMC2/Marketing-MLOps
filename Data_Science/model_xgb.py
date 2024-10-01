import pandas as pd
import numpy as np 
import os
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error as mea
from sklearn.linear_model import LinearRegression

from xgboost import XGBRegressor as XGBR

import warnings 
#Ignore all warnings
warnings.filterwarnings('ignore')

def get_data():
    # Import the dataset
    os.chdir('..')
    data = pd.read_csv('./Data_Engineer/data/marketing.csv')
    data.drop(columns = ['Unnamed: 0'], inplace= True)
    return data

      
class ModelXGB:
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
        
        XGB_model = XGBR(n_estimator = 1000, learning_rate= 0.05)
        XGB_model.fit(X_train,y_train, eval_set = [(X_test,y_test)], verbose = False)
        
        #Save the model to a pickle file
        with open('./Data_Science/model_xgb.pkl','wb') as file:
            pickle.dump(XGB_model,file)
            
        XGB_output = XGB_model.predict(X_test)
        XGB_output = pd.DataFrame(XGB_output)
        XGB_output.to_csv('XGB_output.csv')    
        print('The model run successfully and has been saved to model_xgb.pkl')       
        return XGB_output

if __name__ == '__main__':
    df = get_data
    model = ModelXGB(df)
    output = model.run()
    print('The Pipeline is completed')
        