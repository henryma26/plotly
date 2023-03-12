# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:45:50 2023

@author: user
"""

import pandas as pd
import plotly.io as pio
# import plotly.graph_objects as go
import plotly.graph_objs as go
from plotly.subplots import make_subplots
pio.renderers.default = "browser"


# df1 = pd.read_pickle('HK.800000_1min.pkl')
# df2 = pd.read_pickle('HK.00700_1min.pkl')

# df1 = df1[0:500]
# df2 = df2[0:500]

# fig = go.Figure(data=[go.Candlestick(x=df1['time_key'],
#                                       open=df1['open'],
#                                       high=df1['high'],
#                                       low=df1['low'],
#                                       close=df1['close'])])

# fig.update_layout(
#     title='1',
#     yaxis_title='2',
#     xaxis_rangeslider_visible=False
# )

# fig.show()

import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

# read in data
df1 = pd.read_pickle('HK.800000_1min.pkl')
df2 = pd.read_pickle('HK.00700_1min.pkl')

df1 = df1[0:500]
df2 = df2[0:500]

# create subplots with shared x-axis
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.5)

# add trace for first chart
fig.add_trace(go.Candlestick(x=df1['time_key'],
                open=df1['open'], high=df1['high'],
                low=df1['low'], close=df1['close'], name='HK.800000'), row=1, col=1)

# add trace for second chart
fig.add_trace(go.Candlestick(x=df2['time_key'],
                open=df2['open'], high=df2['high'],
                low=df2['low'], close=df2['close'], name='HK.00700'), row=2, col=1)

# update layout
fig.update_layout(height=800, width=1000, title='OHLC Candlestick Comparison')

# show plot
fig.show()