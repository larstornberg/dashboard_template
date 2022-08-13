from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
import plotly.express as px
import plotly.graph_objects as go
import plotly
import seaborn as sns

import numpy as np
import sys
sys.path.append('..')

from io import BytesIO
import base64
from plotly.tools import mpl_to_plotly

from src.plotting import plot_matplotlib_figure_1, plot_matplotlib_figure_2

def fig_to_uri(in_fig, close_all=True, **save_args):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)


app = Dash(__name__)


app.layout = html.Div([
    
    html.Div([
        html.H1("The Money Maker"),
        html.P("This is a short description of the app and how to operate it"),
        # html.Img(src=app.get_asset_url("left_pane.png")),
        # html.Img(src="assets/left_pane.png"),
        html.Label("Stock Name", className='dropdown-labels'), 
        html.Br(),
        #dcc.Input(id='stockname', className='input', value='AZN.st', type='text', debounce=True),
        dcc.Dropdown(id='stockname', 
                     className='dropdown', 
                     options=[
                         {'label': 'Netflix', 'value': 'nflx'},
                         {'label': 'AztraZeneca', 'value': 'azn.st'},
                         {'label': 'Stockholm OMX index', 'value': '^OMX'},
                         {'label': 'H&M', 'value': 'HM-B.ST'}
                     ],
                     value='^OMX',
                     #options=['azn.st', 'nflx','^OMX'], 
                     #value='azn.st',
                     searchable=True),
        html.Br(),
        html.Br(),
        html.Label('Choose analysis method', 
                   className='dropdown-labels'),
        dcc.Dropdown(id='method', 
                     className='dropdown', 
                     options=['sma-crossing', 'extrema', 'bollinger-band'], 
                     value='sma-crossing',
                     searchable=False),
        html.Br(),
        html.Br(),
        html.Label('SMA windows', 
                   className='dropdown-labels'),
        html.Br(),
        dcc.Input(id='sma_a_value', 
                  className='input', 
                  value=20, 
                  type='number', 
                  debounce=True),
        html.Br(),
        dcc.Input(id='sma_b_value', 
                  className='input', 
                  value=50, 
                  type='number', 
                  debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Number of standard devs', 
                   className='dropdown-labels'),
        html.Br(),
        dcc.Input(id='param', 
                  className='input', 
                  value=2, 
                  type='number', 
                  debounce=True)
        ], id='left-container'),
    
    html.Div([
        html.Div([
            html.Img(id="upper-left-figure"),
        ], id='upper-left-container'),
        html.Div([
            html.Img(id='upper-right-figure'),
        ], id='upper-right-container'),
        html.Div([
            html.Img(id='lower-left-figure'),
        ], id='lower-left-container'),
        html.Div([
            html.Img(id='lower-right-figure'),
        ], id='lower-right-container')
    ], id='right-container')

], id='container')


@app.callback(
    Output("upper-left-figure", 'src'), 
    Output("upper-right-figure", 'src'), 
    Input("param", "value")  
)
def update_graph(param):
    #fig, ax1 = plt.subplots(1,1)
    #np.random.seed(param)
    #ax1.matshow(np.random.uniform(-1,1, size = (3,3)))
    #ax1.set_title(param)
    fig_1 = plot_matplotlib_figure_1(param)
    out_url_1 = fig_to_uri(fig_1)
    
    fig_2 = plot_matplotlib_figure_2(param)
    out_url_2 = fig_to_uri(fig_2)
    
    return out_url_1, out_url_2

if __name__ == "__main__":
    #app.run_server(debug=False, host='0.0.0.0')
    app.run_server(debug=True)
