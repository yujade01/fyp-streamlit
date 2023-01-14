import streamlit as st
import numpy as np
import pandas as pd

df_location = pd.read_csv("location.csv")

customer_location = df_location[['latitude', 'longitude']]
st.map(customer_location)