import streamlit as st
import pandas as pd
from eda_app import run_eda
from ml_app import run_ml
import plotly
import streamlit_option_menu
from streamlit_option_menu import option_menu
import os


def get_data():
    # Import the dataset
    data = pd.read_csv('/workspaces/Marketing-MLOps/Data_Engineer/data/marketing.csv')
    data.drop(columns = ['Unnamed: 0'], inplace= True)
    return data


with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Data","Exploration and Analysis","Machine Learning"],
    icons = ["house",'database',"bar-chart","robot"],
    menu_icon = "cast",
    default_index = 0,
  )
  st.markdown('---')
  st.subheader('This is My Contact Information')
  st.markdown("""
   - **Name:** Hung Tran
   - **Email:** alexchan6788@gail.com
   - **Linkedin:** https://www.linkedin.com/in/alextran02
   - **GitHub:** https://github.com/HungTranEMC2
               """)
#Home Page
if selected == "Home":
   st.title('Welcome to My Marketing MLOps Project Home Page')
   st.header('Black Friday Sales Analysis and Prediction App')

   st.image('/workspaces/Marketing-MLOps/Data_Application/MLOps.png',caption = 'MLOps Project')

   st.markdown("""
   This project aims to analyze and predict Black Friday sales using advanced machine learning operations (MLOps). 
   The Exploration and Analysis will show the visualization of the dataset.
   The Machine Learning show the Result of using XGBoost Algorithms to generate prediction. 
               """)

if selected == "Data":
   df = get_data()
   st.dataframe(df)
   
#EDA Page
if selected == "Exploration and Analysis":
    st.title('Exploratory Data Analysis')
    run_eda()
# ML Page
if selected == "Machine Learning":
    st.title('Machine Learning Results')
    run_ml()