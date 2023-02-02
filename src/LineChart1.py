import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(56)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)
print(x_values)
trace1 = go.Scatter(x=x_values, y=y_values+5,
                   mode='markers', name='markers1')

trace2 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='lines2')

trace3 = go.Scatter(x=x_values, y=y_values-5,
                    mode='lines+markers', name='lines & markers')

data = [trace1, trace2, trace3]

layout = go.Layout(title='Line Chart')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='html/linechart1.html')
