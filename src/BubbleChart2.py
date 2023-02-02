import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv("../data/mpg.csv")
df = df[df['horsepower'].apply(lambda x:x.isnumeric())]
#df['horsepower'] = df['horsepower'].astype('int64')
data = [go.Scatter(x=df['horsepower'].astype('int64'),
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

layout = go.Layout(title="Bubble Chart", hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename="../html/bubbleChart2.html")
