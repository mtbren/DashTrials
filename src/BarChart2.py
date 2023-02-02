import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo


df = pd.read_csv('../data/mocksurvey.csv', index_col=0)

print(df[df.columns[0]])

data = [go.Bar(y=df.index, x=df[response], name=response, orientation='h')
            for response in df.columns]

layout = go.Layout(title='Survey', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='../html/barchart2.html')
