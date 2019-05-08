# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:34:10 2019

@author: Callaway
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import pandas as pd
import datetime as dt 

start = dt.datetime(2011,1,1)
end = dt.datetime.now()

df = web.DataReader('CERN', 'yahoo', start, end)

df.index = pd.to_datetime(df.index)
df['moving_average'] = df.Open.rolling(window = 50).mean()

df2 = web.DataReader('TRPLX', 'yahoo', start,end)
df2.index = pd.to_datetime(df2.index)
df3 = pd.merge(df,df2, left_index = True, right_index = True, how = 'left')


app = dash.Dash()

# html of entire project 
app.layout = html.Div(children = [
        html.H1('Dash Tutorials'),
        dcc.Graph(id = 'example',
                  figure = {
                          'data' : [{'x': df3.index, 'y': df3.Open_x, 'type': 'line', 'name': 'Cerner'},
                                    {'x' : df3.index, 'y': df3.moving_average, 'type': 'dash', 'name': 'Cerner 50 Day SMA'},
                                    {'x': df3.index, 'y': df3.Open_y, 'type': 'line', 'name': 'TRPLX'},
                                    ],
                          'layout' : {'title': 'Cerner Stock Price'}
                          
                          }
                  )
        ])
        

# run app 
if __name__ == '__main__':
    app.run_server(debug= False)
