import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime as dt 

start = dt.datetime(2016,1,1)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)


app = dash.Dash()

# html of entire project 
app.layout = html.Div(children = [
        html.H1('Dash Tutorials'),
        dcc.Graph(id = 'example',
                  figure = {
                          'data' : [{'x': df.index, 'y': df.Open, 'type': 'line', 'name': 'Tesla'},],
                          'layout' : {'title': 'Tesla Stock'}
                          }
                  )
        ])
        

# run app 
if __name__ == '__main__':
    app.run_server(debug= False)
    
df.head()
