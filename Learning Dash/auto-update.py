# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:43:01 2019

@author: callaway
"""

import dash
from dash.dependencies import Input, Event # he said event would be here
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import random
from collections import deque



# deque is a list with a max len basically
X = deque(maxlen = 20)
Y = deque(maxlen = 20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div([
        dcc.Graph(id = 'live-graph',animate = True),
        dcc.Interval(id = 'graph-update', interval = 1000) #update every 1000 ms
        ]
                )

@app.callback(Output('live-graph','figure'),
              event = [Event('graph-update')])


def update_graph():
    ''' this is where the data is going to come from, could be something else
    '''
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
    
    data = go.Scatter(
            x = list(X),
            Y = list(Y),
            name = 'Scatter',
            mode = 'lines+markers'
            )
    return {'data':[data], 'layout':go.Layout(xaxis = dict(range = [min(X),max(X)]),
            yaxis = dict(range = [min(Y), max(Y)]))}

    
if __name__ == "__main__":
    app.run_server(debug = False)
    
    
    
    
    
