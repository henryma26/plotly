# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:39:30 2023

@author: henryma
"""

import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

pio.renderers.default = "browser"
# Load Bitcoin data
df = pd.read_pickle('testing.pkl')
# df = df[:500]

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['start_time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

# Add buy markers
fig.add_trace(go.Scatter(x=df[df['buy'] == 1]['start_time'],
                          y=df[df['buy'] == 1]['close'],
                          mode='markers',
                          marker=dict(color='blue', symbol='triangle-up', size=10),
                          name='Buy'))

# Add sell markers
fig.add_trace(go.Scatter(x=df[df['sell'] == 1]['start_time'],
                          y=df[df['sell'] == 1]['close'],
                          mode='markers',
                          marker=dict(color='black', symbol='triangle-down', size=10),
                          name='Sell'))


# Customize chart layout
fig.update_layout(
    title='Bitcoin Candlestick Chart',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False
)

# Display chart
fig.show()