# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:01:07 2019

@author: CH057395
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output
import pandas as pd
import datetime as dt 


app = dash.Dash()

# html of entire project 
app.layout = html.Div(children = [
        
        html.H1(children = '''
                symbol to graph
                '''),
        
        dcc.Input(id = 'input', value = '', type = 'text'),
        
        html.Div(id = 'output-graph')

        ])
        
@app.callback(
        Output(component_id = 'output-graph', component_property = 'children'),
        [Input(component_id = 'input', component_property = 'value')]
        )

def update_graph(input_data):
    
    start = dt.datetime(2015,1,1)
    end = dt.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    df['50_day_sma'] = df.Open.rolling(window = 50).mean() # I could put an arima model here
    
    return dcc.Graph(id = 'example-graph',
                  figure = {
                          'data' : [
                                  {'x': df.index, 'y': df.Open, 'type': 'line', 'name': input_data},
                                  {'x': df.index, 'y': df['50_day_sma'], 'type': 'line',
                                   'name': '{}_50_day_sma'.format(input_data)},
                                    ],
                          'layout' : 
                              {'title': '{} Stock Price'.format(input_data)}
                          }
                  )
    

# run app 
if __name__ == '__main__':
    app.run_server(debug= False)
