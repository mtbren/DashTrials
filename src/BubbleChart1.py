import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
from future.backports.datetime import date

df = pd.read_csv('../data/mpg.csv')
print(df.head(3))
print(df.columns)
df = df[df['horsepower'].apply(lambda x:x.isnumeric())]
df['horsepower'] = df['horsepower'].astype('int64')

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

layout = go.Layout(title='Bubble Chart', hovermode='y')

fig = go.Figure(data=data, layout=layout);

pyo.plot(fig, filename="../html/bubblechart1.html")