from re import T
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit.elements.image import image_to_url

st.title('My dashboard')
st.write('note')
st.sidebar.title('selector')
#image = Image.open("Picture.jpg")
#st.image(image, use_column_width=True)
st.markdown('<style>body{background-color: lightblue;}</style>',unsafe_allow_html=True)


# loading the data
@st.cache
def load_data():
    df = pd.read_csv("C:/Users/DESMOND/Twitter-Data-Analysis/data/clean_tweet.csv")

    return df

data = load_data()

st.write(data)

# comment ot test git 