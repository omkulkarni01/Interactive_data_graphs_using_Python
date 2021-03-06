# -*- coding: utf-8 -*-
"""Interactive_graphs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DTP1Jd0gzs0y7P2TV_mHrtm-UVOIwcoq
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd                     # download & import all required libraries
import numpy as np
import chart_studio.plotly as py
import plotly.offline as po             #to use plotly library offline
import plotly.express as px
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk

# %matplotlib inline
po.init_notebook_mode(connected=True)
df = pd.read_csv("covid data.csv")      #loading file (location of file & IDE must be same)

print(f'Size of data is {df.shape}')       #data shape
df                                         #to show data

df = df[['iso_code','date', 'location', 'total_cases','new_cases']]  #data preprocessing
df.head()

print(f"First and Last dates of data are {df.date.min()} & {df.date.max()} respevtively.")

print("Available options of plot are :")

for i in ['natural earth','mercator','hammer','equirectangular','orthographic','kavrayskiy7','miller','robinson','eckert4',
'azimuthal equal area','conic equal area','conic equidistant','stereographic','mollweide','transverse mercator',
'winkel tripel','aitoff','sinusoidal']:
    print(i+',')
from tkinter import *
from PIL import ImageTk

a=input("enter type of plot:")               # asking for user input

canvas = Canvas(width = 600, height = 800, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "t.png")
canvas.create_image(10, 10, image = image, anchor = NW)
m = px.choropleth(df, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                    animation_frame="date",
                    title = "Daily new COVID cases",
                    projection=a,
                   color_continuous_scale=px.colors.sequential.PuRd)
text = Text(m)
text.place(x=30, y=50)
mainloop()
m.show()



agri=pd.read_csv('agri.csv')              #loading file (location of file & IDE must be same)
print(f"Shape of data is {agri.shape}")    #data shape
agri.head()                               #to show data

data=dict(type='choropleth',
          locations=agri['code'],
          locationmode='USA-states',
          z=agri['total exports'],
          text=agri['text'],
          colorscale='Greens',
         colorbar={'title':'colorbar'})
layout=dict(title='Agri Plot',geo=dict(scope='usa',showlakes=True,lakecolor="blue"))
y=pg.Figure(data=[data],layout=layout)        #specifing plot details
po.iplot(y)



gdp=pd.read_csv('gdp.csv')                #loading file (location of file & IDE must be same)
print(f"Shape of data is {gdp.shape}")    #data shape
gdp                                       #showing data

data=dict(type='choropleth',
          colorscale='peach',
          locations=gdp['CODE'],
          z=gdp['GDP (BILLIONS)'],
          text=gdp['COUNTRY'])
layout=dict(title='GDP geo-plot',geo=dict(projection={'type':'natural earth'}))
z=pg.Figure(data=[data],layout=layout)          #specifing plot details
po.iplot(z)                                     #output

