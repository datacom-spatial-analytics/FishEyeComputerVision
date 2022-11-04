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

################ View  ################
def view(model):
   st.set_page_config(layout = 'wide')
   # Header
   st.header(model.header)
   
   commentaryCol, spaceCol, chartCol=st.columns((2,1,6))
   # Description
   with commentaryCol:
      st.write(model.description)
   # Year Slider  
   year=st.slider(model.sliderCaption,
      model.yearStart, model.yearEnd,
      model.yearStart, model.yearStep)
   #Chart
   with chartCol:
      st.plotly_chart(model.chart(year), 
         use_container_width = True)



################ Model ################
class Model:
   def __init__(self):
      self.df = pd.DataFrame(px.data.gapminder())
      self.ylist = [int(i) for i in self.df['year'].unique()]
      self.yearStart = self.ylist[0]
      self.yearEnd = self.ylist[-1]
      self.yearStep = self.ylist[1]-self.ylist[0]
   def chart(self,year):
      return px.scatter(self.df[self.df['year'] == year],
         x = 'lifeExp', y = 'gdpPercap', 
         title = f'Year: {year}',
         color='continent',size='pop')
   header = 'Global Statistics from Gapminder'
   description ='''
      See how life expectancy changes over time 
      and in relation to GDP.
      Move the slider to change the year to display.
   '''
   sliderCaption='Select the year for the chart'

   ################ Start  ################
view(Model())