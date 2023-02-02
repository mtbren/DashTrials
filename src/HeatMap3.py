import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo

df = pd.read_csv('../data/flights.csv')

data = go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'])
layout = go.Layout(title='Passengers by Year-Month')

fig = go.Figure(layout=layout, data=data)
pyo.plot(fig, filename='../html/heatmap3.html')
