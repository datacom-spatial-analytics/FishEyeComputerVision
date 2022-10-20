from tkinter import font
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.image as img

from scipy.interpolate import Rbf  # radial basis functions
import matplotlib.pyplot as plt
import numpy as np

x = [1555,1203,568,1098,397,564,1445,337,1658,1517,948]
y = [860,206,1097,425,594,614,553,917,693,469,306]
x = [0.9, 0.6, 0.1, 0.5, 0.04, 0.1, 0.82, 0.0, 1.0, 0.89, 0.46]
y = [0.73, 0.0, 1.0, 0.24, 0.43, 0.45, 0.38, 0.7, 0.54, 0.29, 0.11]
z = [1]*len(x)

rbf_adj = Rbf(x, y, z, function='gaussian')

x_fine = np.linspace(0, 1, 81)
y_fine = np.linspace(0, 1, 82)

x_grid, y_grid = np.meshgrid(x_fine, y_fine)

z_grid = rbf_adj(x_grid.ravel(), y_grid.ravel()).reshape(x_grid.shape)

#im = img.imread('images/Datacom_3F.png')
#plt.plot('blueprint')
#plt.imshow(im)
#plt.savefig('images/Datacom_T.png', dpi=500, transparent=True)

plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()
plt.pcolor(x_fine, y_fine, z_grid);
plt.plot(x, y, 'ok');
plt.xlabel('x'); plt.ylabel('y'); #plt.colorbar();
plt.title('Heat Intensity Map');

plt.savefig('images/Heatmap.png', dpi=18, transparent=True)
#st.experimental_rerun()
