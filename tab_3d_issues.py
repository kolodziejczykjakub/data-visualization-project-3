import dash_core_components as dcc
import dash_html_components as html

from issues_with_3d import *


encoded_image1, encoded_image2, encoded_image3 = get_encoded_imgs()
fig = get_3d_scatter_iris()
fig1 = get_barplot_iris()

fig2 = get_barplot_low_numbers_15_06()

tab_3d_issues_layout = html.Div([
            html.H3('Issues with third dimension on bar plots'),

            html.Div([
                html.Div([
                    html.H4('Redundant third dimension on the bar plot'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),
                             style={'height':'90%', 'width':'90%'}),
                    # dcc.Graph(figure=fig3)
                ], className="six columns"),

                html.Div([
                    html.H4('It is better to stick to two dimensions'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),
                             style={'height': '130%', 'width': '100%'}),
                ], className="six columns"),

            ], className="row"),

            html.Div([
                html.Div([
                    html.H4('Write your estimated values for the first plot:'),
                    dcc.Markdown("Values for Bahamas deaths, Brunei confirmed Burma recovered :"),
                    dcc.Input(id='input_bar11', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar12', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar13', type='number', value='0', size='10'),
                    html.Button(id='submit_button_bar1', n_clicks=0, children='Submit'),
                    html.Div(id='output_bar1')
                ], className="six columns"),

                html.Div([
                    html.H4('Write your estimated values for the second plot:'),
                    dcc.Markdown("Values for Bahamas deaths, Brunei confirmed Burma recovered :"),
                    dcc.Input(id='input_bar21', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar22', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar23', type='number', value='0', size='10'),
                    html.Button(id='submit_button_bar2', n_clicks=0, children='Submit'),
                    html.Div(id='output_bar2')
                ], className="six columns")
            ], className="row"),


            html.Div([
                html.Div([
                    html.H4('Check real values on second plot:'),
                    dcc.Graph(figure=fig2),
                ], className="twelve columns"),

            ], className="row")
        ])