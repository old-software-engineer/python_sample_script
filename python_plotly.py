# -*- coding: utf-8 -*-
import datetime
import numpy as np
import pandas as pd
from matplotlib import pylab
from pylab import plt
import plotly.plotly as py
import plotly.tools as tls
from plotly import figure_factory as FF
tls.set_credentials_file(username='user_name', api_key='api_key')
import plotly.graph_objs as go
import quandl as q
q.ApiConfig.api_key = 'put_here_your_api_keys'
data=q.get("NS1/LRCX_US", authtoken="authentication_token")
print data
data=data['News Buzz']
tail = data.tail(30)



INCREASING_COLOR = '#1EA1BD'
DECREASING_COLOR = '#C6C6C6'
colors = []
last_val = 0
for i in tail:
    if (i != 0):
        if i > last_val:
        	colors.append(INCREASING_COLOR)
	elif (i == last_val):
		colors.append(INCREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)       
    else:
        colors.append(DECREASING_COLOR)
    last_val = i

trace = go.Bar(
                x=tail.index,
                y=tail,
                marker = dict(color = colors)
            ) 
layout = go.Layout(
title = 'Lam Research News Buzz',
titlefont = dict( color= '#000000', family = 'raleway', size=24 ),
font=dict(family = 'Raleway'),
xaxis=dict(
        showline=True,
        mirror=True,
        linecolor='#545454',
        linewidth=3,
        zeroline=False),
yaxis=dict(
        autorange=False,
        showline=True,
        mirror=True,
        range=[0,12],
        linecolor='#545454',
        linewidth=3,
        #title = 'Sentiment Score',
        zeroline=False),
plot_bgcolor='000000',
    annotations = list([
        dict(
            x = data.index[-29],
            y = 1,
            text = "<b>Low News Buzz Score</b>",
            showarrow = False,
            font=dict(
                color='c6c6c6',
                size = 14 
            ),
        ),
        dict(
            x = data.index[-29],
            y = 10,
            text = "<b>High News Buzz Score</b>",
            showarrow = False,
            font=dict(
                color='c6c6c6',
                size = 14
            ),
        )
    ])
)
traces = [trace]
fig = go.Figure(data=traces, layout=layout)
py.plot(fig, filename = "Lam Research News Buzz New Colors_SHUB")
