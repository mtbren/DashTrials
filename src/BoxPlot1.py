import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

# y = [1,2,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,30,54,200]

# data = [go.Box(y=y, boxpoints='all', jitter=0.3, pointpos=2)]
# data = [go.Box(y=y, boxpoints='outliers', jitter=0.3, pointpos=2)]

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [go.Box(y=snodgrass, name='Snodgrass'),
        go.Box(y=twain, name='Twain'),]


pyo.plot(data, filename='../html/boxplot1.html')
