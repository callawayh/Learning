# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:54:17 2019

@author: Callaway 

Introduction to using dash

https://pythonprogramming.net/data-visualization-application-dash-python-tutorial-introduction/
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


# html of entire project 
app.layout = html.Div(children = [
        html.H1('Dash Tutorials'),
        dcc.Graph(id = 'example',
                  figure = {
                          'data' : [{'x': [1,2,3,4,5], 'y': [5,6,7,2,1], 'type': 'line', 'name': 'boats'},
                                    {'x': [1,2,3,4,5], 'y': [8,6,10,9,2], 'type': 'bar', 'name': 'cars'},
                                    ],
                        'layout' : {'title': 'Basic Dash Example'}
                        
                          })
        ])

# run app 
if __name__ == '__main__':
    app.run_server(debug= False)
