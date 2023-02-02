import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df1 = pd.read_csv('../data/nst-est2017-alldata.csv')

df1 = df1[df1['DIVISION'].isin(['1','2','3','4','5'])]
df1.set_index('NAME', inplace=True)

list_of_population_columns = [col for col in df1.columns if col.startswith('POP')]
df1 = df1[list_of_population_columns]

print(df1)
data = [go.Scatter(x=df1.columns,y=df1.loc[name],mode='lines',name=name) for name in df1.index]


pyo.plot(data, filename='../html/linechart2.html')