
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon

x_terrace = np.arange(410,3375.8724463, 10)
x_terrace = np.flip(x_terrace)
y_terrace = np.ones_like(x_terrace)
y_terrace = y_terrace *188


df = pd.read_csv("site 3.csv")
fig, ax = plt.subplots(1,1)

polygon_points = [] #creates a empty list where we will append the points to create the polygon

for i in range(len(df.iloc[:, 0])):
    polygon_points.append([df.iloc[i, 0],df.iloc[i, 1]])
for i in range(len(x_terrace)):
    polygon_points.append([x_terrace[i], y_terrace[i]])
polygon_points.append([df.iloc[1, 0],df.iloc[1, 1]])
polygon = Polygon(polygon_points)
area = polygon.area
area = round(area, 2)
print(area)

ax.fill(*polygon.exterior.xy)
plt.xlabel("distance (m)")
plt.ylabel("elevation (m)")
plt.suptitle("Site 3 channel area polygon")
plt.text(1400,183,  "Area: " + str(area) + " m^2")
plt.show()