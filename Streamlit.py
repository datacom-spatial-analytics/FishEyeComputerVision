from tkinter import font
import webbrowser
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.image as img
from datetime import time

from scipy.interpolate import Rbf  # radial basis functions
import matplotlib.pyplot as plt
import numpy as np

st.write("**Datacom Spatial Analytics**")

hmap = Image.open('images/Heatmap.png')

blueprint = Image.open('images/Datacom_3F.png')
blueprint_T = Image.open('images/Datacom_3F_T.png')

blueprint_T.paste(hmap, (140,250), mask = hmap)
#st.image(blueprint, caption="This is the map of Datacom Level 3")
#st.image(blueprint_T, caption="This is the Heatmapping of Datacom Level 3")

st.sidebar.header("**Visualisation of Spatial Analytics**")
st.sidebar.subheader("**User Input Parameters**")
st.sidebar.subheader("**Tidal Effects Plot**")

if st.sidebar.button('Number of clients per day'):
    st.write('Show plot of number of clients per day')
if st.sidebar.button('Number of clients per hour'):
    st.write('Show plot of number of clients per hour')
if st.sidebar.button('Granular time analysis in 15 mins interval'):
    st.write('Show plot of number of clients in granular time in 15 mins interval')
if st.sidebar.button('Granular time analysis in 30 mins interval'):
    st.write('Show plot of number of clients in granular time in 30 mins interval')

st.sidebar.subheader("**Heatmap Plot**")
if st.sidebar.button('Datacom Level 3 Floor map'):
    st.image(blueprint, caption="This is the map of Datacom Level 3")
if st.sidebar.button('Datacom Level 3 Floor Heatmap'):
    st.image(blueprint_T, caption="This is the Heatmapping of Datacom Level 3")
heatmap_change = st.slider("Choose the time to see the heatmap: ",value=(time(0, 00), time(23, 50)))
st.write("Heatmap at: ", heatmap_change)
#st.experimental_rerun()

if st.sidebar.button('Interactive Plotting'):
    webbrowser.open_new_tab('https://app.powerbi.com/reportEmbed?reportId=b9216604-11dc-43e6-a820-abd017c950f0&autoAuth=true&ctid=866c7a4c-8a59-4bd3-ad9f-8512a581efc0')



