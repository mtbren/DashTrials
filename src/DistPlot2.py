import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("../data/iris.csv")

x1 = df[df['class'] == 'Iris-setosa']['petal_length']
x2 = df[df['class'] == 'Iris-versicolor']['petal_length']
x3 = df[df['class'] == 'Iris-virginica']['petal_length']

hist_data = [x1, x2, x3]

group_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)

pyo.plot(fig, filename='../html/distplot2.html')
