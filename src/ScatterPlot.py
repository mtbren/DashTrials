import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=30,
                       color='rgb(124,124,124)',
                       symbol='pentagon',
                       line={'width': 2}
                   ))]

layout = go.Layout(title="My Scatter Plot",
                   xaxis=dict(title="My X Axis"),
                   yaxis={'title': 'My Y Axis'},
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='../html/scatter.html')