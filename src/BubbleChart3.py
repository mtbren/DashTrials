import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv("../data/mpg.csv")

data = go.Scatter(x=df['displacement'],
                  y=df['acceleration'],
                  mode='markers',
                  text=df['name'],
                  marker=dict(
                      size=df['weight']/100,
                      color=df['weight'],
                      showscale=True
                  ))

layout = go.Layout(title='Bubble Chart 3')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='../html/bubblechart3.html')
