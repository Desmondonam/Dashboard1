from os import stat
from re import T
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
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

df = load_data()
# use a selection of options

visualization = st.sidebar.selectbox('Select a Chart type' ,('Bar Chart', 'Pie Chart', 'Line Chart'))
state_select = st.sidebar.selectbox('Select a place', df['place'].unique())
status_select = st.sidebar.radio('Twitter Data status', ('Words in tweet', 'polarity', 'country', 'Created_on'))
selected_state = df[df['place']==state_select]
st.markdown("## **Tweet level Analysis **")


def get_total_dataframe(df):
    total_dataframe = pd.DataFrame({
    'Status':['retweet_count', 'favorite_count', 'followers_count', 'friends_count'],
    'Number of cases':(df.iloc[0]['retweet_count'],
    df.iloc[0]['favorite_count'],
    df.iloc[0]['favorite_count'],df.iloc[0]['followers_count'])})
    return total_dataframe



state_total = get_total_dataframe(selected_state)
if visualization=="Bar chart":
    state_total_graph = px.bar(state_total, x='Status', y='Number of cases',
    labels={'Number of cases':'Number of cases in %s' %(state_select)},color='Status')
    st.plotly_chart(state_total_graph)
elif visualization == 'Pie chart':
    if state_select=='retweet_count':
        st.title('Total retweet_count')
        fig = px.pie(df, values=df['retweet_count'], names=df['place'])
        st.plotly_chart(fig)

    elif state_select=='favorite_count':
        st.title('Total  favorite_count')
        fig = px.pie(df, values=df['favorite_count'], names=df['place'])
        st.plotly_chart(fig)

    elif state_select=='followers_count':
        st.title('Total favorite_count')
        fig = px.pie(df, values=df['followers_count'], names=df['place'])
        st.plotly_chart(fig)
    else:
        st.title('Total recoverd cases')
        fig = px.pie(df, values=df['revovered_cases'], names=df['place'])
        st.plotly_chart(fig)
elif visualization=='Line Chart':
    if state_select=='followers_count':
        st.title('Total followers_count Among places')