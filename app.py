import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px


st.header('US Vehicle Sales Stats')

data = pd.read_csv('../vehicles_us.csv',parse_dates=['date_posted'])

fig = px.histogram(data, x='price', color='condition', barmode='overlay')



