import matplotlib.pyplot as plt
import numpy as np
import math

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

#POINT DATASET
x = [1555,1203,568,1098,397,564,1445,337,1658,1517,948]
y = [860,206,1097,425,594,614,553,917,693,469,306]

x=[20,28,15,20,18,25,15,18,18,20,25,30,25,22,30,22,38,40,38,30,22,20,35,33]
y=[20,14,15,20,15,20,32,33,45,50,20,20,20,25,30,38,20,28,33,50,48,40,30,35]

# x = [0.9, 0.6, 0.1, 0.5, 0.04, 0.1, 0.82, 0.0, 1.0, 0.89, 0.46]
# y = [0.73, 0.0, 1.0, 0.24, 0.43, 0.45, 0.38, 0.7, 0.54, 0.29, 0.11]

#DEFINE GRID SIZE AND RADIUS(h)
grid_size=1
h=10

#GETTING X,Y MIN AND MAX
x_min=0
x_max=2500
y_min=0
y_max=2500
x_min=min(x)
x_max=max(x)
y_min=min(y)
y_max=max(y)


#CONSTRUCT GRID
x_grid=np.arange(x_min-h,x_max+h,grid_size)
y_grid=np.arange(y_min-h,y_max+h,grid_size)
x_mesh,y_mesh=np.meshgrid(x_grid,y_grid)

#GRID CENTER POINT
xc=x_mesh+(grid_size/2)
yc=y_mesh+(grid_size/2)

#FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL
def kde_quartic(d,h):
    dn=d/h
    P=(7/8)*(1-dn**2)**2
    return P

#PROCESSING
intensity_list=[]
for j in range(len(xc)):
    intensity_row=[]
    for k in range(len(xc[0])):
        kde_value_list=[]
        for i in range(len(x)):
            #CALCULATE DISTANCE
            d=math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
            if d<=h:
                p=kde_quartic(d,h)
            else:
                p=0
            kde_value_list.append(p)
        #SUM ALL INTENSITY VALUE
        p_total=sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)

print(intensity_list)

#HEATMAP OUTPUT
intensity=np.array(intensity_list)
plt.pcolormesh(x_mesh,y_mesh,intensity)
plt.plot(x,y,'ro')
plt.colorbar()
plt.show()

print('exeted')