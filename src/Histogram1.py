import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0,end=50, size=0.5))]

layout = go.Layout(title='Mpg distribution')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='../html/histogram1.html')
