import streamlit as st 
import pandas as pd 
# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache_data
def get_data():
    # Import the dataset
    data = pd.read_csv('C:/Users/289380/OneDrive - Resideo/Documents/Marketing-MLOps/Data_Engineer/data/marketing.csv')
    data.drop(columns = ['Unnamed: 0'], inplace= True)
    return data


def count_plot(dataframe, column_name, title =None, hue = None):
    '''
    Function to plot seaborn count plot
    Input: Dataframe name that has to be plotted, column_name that has to be plotted, title for the graph
    Output: Plot the data as a count plot
    '''
    base_color = sns.color_palette()[0]
    sns.countplot(data = dataframe, x = column_name, hue=hue)
    plt.title(title)
    pass



def run_eda():
	st.subheader("EDA")
	submenu = st.sidebar.selectbox("Submenu",["EDA","Plots"])
	df = get_data()

	if submenu == "EDA":
		st.subheader("Exploratory Data")
		st.dataframe(df.head())

		c1,c2 = st.columns(2)

		with st.expander("Descriptive Summary"):
			st.dataframe(df.describe())

		with c1:
			with st.expander("Gender Distribution"):
				st.dataframe(df['gender'].value_counts())
		with c2:
			with st.expander("age Distribution"):
				st.dataframe(df['age'].value_counts())

	elif submenu == "Plots":
		st.subheader("Plotting")
		with st.expander("Gender"):
				fig, ax = plt.subplots()
				sns.countplot(data = df, x = 'gender',hue ='gender', ax = ax )
				ax.set_title("Gender Distribution")
				st.pyplot(fig)

		with st.expander("City"):
				fig, ax = plt.subplots()
				sns.countplot(data = df, x= 'city_category',hue ='city_category', ax = ax )
				ax.set_title("Population of each City Category")
				st.pyplot(fig)



		with st.expander("Stay Durations"):
				fig, ax = plt.subplots()
				sns.countplot(data = df, x= 'stay_in_current_city_years',hue ='stay_in_current_city_years', ax = ax )
				ax.set_title("Analyzing Customer Segments by Duration of City Residency")
				st.pyplot(fig)
		with st.expander("Occupation"):
				fig, ax = plt.subplots()
				sns.countplot(data = df, x= 'occupation numeric',hue ='occupation numeric', ax = ax )
				ax.set_title("Analyzing Customer Segments by Occupation")
				st.pyplot(fig)

		with st.expander("Age"):
				fig, ax = plt.subplots()
				sns.countplot(data = df, x= 'age',hue ='age', ax = ax )
				ax.set_title("Population of each Age Group")
				st.pyplot(fig)

			





