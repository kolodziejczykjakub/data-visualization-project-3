import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from issues_with_3d import *


encoded_image1, encoded_image2 = get_encoded_imgs()
fig = get_3d_scatter_iris()
fig1 = get_barplot_iris()


tab_3d_issues_layout = html.Div([
            html.H3('Issues with third dimension on plots'),

            html.Div([
                html.Div([
                    html.H4('Redundant third dimension on bar plot'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),
                             style={'height':'115%', 'width':'115%'}),
                ], className="four columns"),

                html.Div([
                    html.H4('Better stick to two dimensions'),
                    dcc.Graph(figure=fig1)
                ], className="four columns"),

                html.Div([
                    html.H4('Write your estimated values for both plots'),
                    dcc.Markdown("Values for mean petal lengths in order - setosa, versicolor, virginica:"),
                    dcc.Input(id='input-pl-set', type='number', value='0', size='5'),
                    dcc.Input(id='input-pl-ver', type='number', value='0', size='10'),
                    dcc.Input(id='input-pl-vir', type='number', value='0', size='10'),
                    html.Button(id='submit-button-pl', n_clicks=0, children='Submit'),
                    html.Div(id='output-pl-mae')
                ], className="four columns"),
            ], className="row"),

            html.Div([
                html.Div([
                    html.H4('Column 1'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode())),
                ], className="six columns"),

                html.Div([
                    html.H4('Column 2'),
                    dcc.Graph(figure=fig)
                ], className="six columns"),
            ], className="row")
        ])