import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../data/abalone.csv')

data = go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))

layout = go.Layout(title='Lengths')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='../html/histogram2.html')
