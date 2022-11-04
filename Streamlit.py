from tkinter import font
import webbrowser
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.image as img
from datetime import datetime, time
from scipy.interpolate import Rbf  # radial basis functions
import matplotlib.pyplot as plt
import numpy as np
import json
import plotly.figure_factory as ff
import plotly.express as px
import datetime as dt
import requests
import base64
import plotly.graph_objects as go
from dateutil.relativedelta import relativedelta # to add days or years
import os
from scipy.stats import gaussian_kde

st.write("**Datacom Spatial Analytics**")

#hmap = Image.open('images/Heatmap.png')

blueprint = Image.open('images/Datacom_3F.png')
blueprint_T = Image.open('images/Datacom_3F_T.png')

#blueprint_T.paste(hmap, (140,250), mask = hmap)
#st.image(blueprint, caption="This is the map of Datacom Level 3")
#st.image(blueprint_T, caption="This is the Heatmapping of Datacom Level 3")

st.sidebar.header("**Visualisation of Spatial Analytics**")
st.sidebar.subheader("**User Input Parameters**")
st.sidebar.subheader("**Tidal Effects Plot**")
if st.sidebar.button('Interactive Plotting'):
    webbrowser.open_new_tab('https://app.powerbi.com/reportEmbed?reportId=b9216604-11dc-43e6-a820-abd017c950f0&autoAuth=true&ctid=866c7a4c-8a59-4bd3-ad9f-8512a581efc0')
st.sidebar.subheader("**Heatmap Plot**")
if st.sidebar.button('Datacom Level 3 Floor map'):
    st.image(blueprint, caption="This is the map of Datacom Level 3")
#if st.sidebar.button('Datacom Level 3 Floor Heatmap'):
#    st.image(blueprint_T, caption="This is the Heatmapping of Datacom Level 3")
#heatmap_change = st.slider("Choose the time to see the heatmap: ",value=(time(0, 00), time(23, 50)))
#st.write("Heatmap at: ", heatmap_change)
heatmap_change = st.slider("Choose the time to see the heatmap: ", format="hh:mm:Ss", value=(time(0, 00, 00), time(23, 59, 59)))
st.write("Heatmap at: ", heatmap_change[0])
#st.experimental_rerun()

date = '2022-10-27'
startTime = heatmap_change[0]
endTime = heatmap_change[1]

#start = date + 'T' + startTime.strftime('%H:%M:%S')
#end = date + 'T' + endTime.strftime('%H:%M:%S')

get_all_url = 'https://raspeberryimagedata.azurewebsites.net/api/data/merged/all'
# post data
r = requests.get(get_all_url)

start = date + 'T' + str(startTime)
end = date + 'T' + str(endTime)

# change r.text to json object
data = json.loads(r.text)

bounding_boxes = []
for i in data:
    for key, value in i.items():
        if key == 'Date/Time':
            if(i[key] >= start and i[key] <= end):     
                bounding_boxes.append(i['bbox'])

# get the first element of each list
x = [i[0] for i in bounding_boxes]
y = [i[1] for i in bounding_boxes]
# normalize the data attributes
x = (x - np.min(x)) / (np.max(x) - np.min(x))
y = (y - np.min(y)) / (np.max(y) - np.min(y))
# scatter plot of x and y


# create a mesh to plot in
z = [1]*len(x) 

kde = gaussian_kde([x,y])
xi, yi = np.mgrid[0:1:100j, 0:1:100j]
zi = kde(np.vstack([xi.flatten(), yi.flatten()]))
# plot a density
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud')
plt.scatter(x, y)
plt.show()


plt.title('Heat Map of Meeting Room')
#plt.show()
st.pyplot(plt)

st.write(data)




