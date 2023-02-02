import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../data/abalone.csv')

set1 = np.random.choice(df['rings'], 40, replace=False)
set2 = np.random.choice(df['rings'], 100, replace=False)

data = [go.Box(y=set1,name='A'),
        go.Box(y=set2, name='B')]

layout = go.Layout(title='Check if sample from same dataset')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='../html/boxplot2.html')
