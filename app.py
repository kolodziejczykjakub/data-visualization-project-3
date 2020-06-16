import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np

from tab_3d_issues import tab_3d_issues_layout
from issues_with_3d import low_numbers_15_06_query_values



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True


app.layout = html.Div(children=[
    html.H1(children='Title'),

    html.Div(children='''
        Lorem impsum...
    '''),

    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1'),
        dcc.Tab(label='Tab 2', value='tab-2'),
        dcc.Tab(label='Tab 3', value='tab-3'),
        dcc.Tab(label='Tab 4', value='tab-4'),
        dcc.Tab(label='Tab 5', value='tab-5'),
        dcc.Tab(label='Tab 6', value='tab-6'),
    ]),

    html.Div(id='tabs-content')

])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H4('Description'),
            html.P('Opis aplikacji...'),
            html.H4('Autorzy'),
            html.Li('Michał Bortkiewicz'),
            html.Li('Michał Dyczko'),
            html.Li('Jakub Kala'),
            html.Li('Damian Kryński'),
            html.Li('Franciszek Grymuła'),
            html.Li('Kamil Ruta'),
            html.A('Repozytorium', href='https://github.com/jakubkala/data-visualization-project-3')
        ])

    elif tab == 'tab-2':
        return tab_3d_issues_layout

    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])

    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])

    elif tab == 'tab-5':
        return html.Div([
            html.H3('Tab content 5')
        ])

    elif tab == 'tab-6':
        return html.Div([
            html.H3('Tab content 6')
        ])


# tab with 3d issues callbacks:
@app.callback(Output('output_bar1', 'children'),
              [Input('submit_button_bar1', 'n_clicks')],
              [State('input_bar11', 'value'),
               State('input_bar12', 'value'),
               State('input_bar13', 'value')],
              )
def update_output(n_clicks, input1, input2, input3):
    input_values = np.asarray([input1, input2, input3]).astype(float)
    MAE = low_numbers_15_06_query_values - input_values
    if n_clicks > 0:
        return u'''
            Errors for Bahamas deaths: {}, Brunei confirmed cases: {}, Burma recovered: {}
        '''.format(MAE[0], MAE[1], MAE[2])

@app.callback(Output('output_bar2', 'children'),
              [Input('submit_button_bar2', 'n_clicks')],
              [State('input_bar21', 'value'),
               State('input_bar22', 'value'),
               State('input_bar23', 'value')],
              )
def update_output(n_clicks, input1, input2, input3):
    input_values = np.asarray([input1, input2, input3]).astype(float)
    MAE = low_numbers_15_06_query_values - input_values
    if n_clicks > 0:
        return u'''
            Errors for Bahamas deaths: {}, Brunei confirmed cases: {}, Burma recovered: {}
        '''.format(MAE[0], MAE[1], MAE[2])


if __name__ == '__main__':
    app.run_server(debug=True)