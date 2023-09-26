
import streamlit as st
import pandas as pd
import numpy as np

HairEye = pd.read_csv('HairEyeColor.csv')

st.title("Hair Eye Color Database")


InputHair = st.sidebar.selectbox("Select Hair Color", ("Brown", "Black", "Blond", "Red"))


HairEyeselect = HairEye[HairEye["Hair"] == InputHair]


st.dataframe(HairEyeselect)




