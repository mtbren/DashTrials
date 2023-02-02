import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY']==day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
                       
    data.append(trace)
    

layout = go.Layout(title='Temp Chart')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='../html/YumaAZ.html')

