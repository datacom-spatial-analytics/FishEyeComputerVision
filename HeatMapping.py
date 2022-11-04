# CAN DELETE THE FILE AND MERGE TO STREAMLIT.PY AFTER STREAMLIT WORKING

from tkinter import font
import pandas as pd
from PIL import Image
import matplotlib.image as img

from scipy.interpolate import Rbf  # radial basis functions
import matplotlib.pyplot as plt
import numpy as np
import json

datafile = 'Dataset.json'
with open(datafile) as f:
    data = json.load(f)

df = pd.DataFrame()
for n in range(len(data)):
    id =[]
    bbox = []
    score = []
    for i, key in enumerate(data[n].keys()):
        print()
        if i == 0:
            id.append(data[n][key])
        if i == 1:
            bbox.append(data[n][key])
        if i == 2:
            score.append(data[n][key])
    temp = pd.DataFrame({'id': id, 'x_box': bbox[0][0], 'y_box': bbox[0][1], 'w_box': bbox[0][2], 'h_box': bbox[0][3], 'a_box': bbox[0][4], 'score': score})
    #     # concat dataframes
    df = pd.concat([df, temp], ignore_index=True)

# get the first column of df
x = df[df.columns[1]]
y = df[df.columns[2]]
# normalize the data attributes
x = (x-x.min())/ (x.max() - x.min())
y = (y-y.min())/ (y.max() - y.min())

z = [1]*len(x) 

rbf_adj = Rbf(x, y, z, function='gaussian')

x_fine = np.linspace(-1, 2, 82)
y_fine = np.linspace(-1, 2, 82)

x_grid, y_grid = np.meshgrid(x_fine, y_fine)

z_grid = rbf_adj(x_grid.ravel(), y_grid.ravel()).reshape(x_grid.shape)

plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()
plt.pcolor(x_fine, y_fine, z_grid)
plt.plot(x, y, 'ok')
plt.xlabel('x'), plt.ylabel('y'), plt.colorbar()
plt.title('Heat Intensity Map')
plt.show()