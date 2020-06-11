import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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
        return html.Div([
            html.H3('Tab content 2')
        ])

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


if __name__ == '__main__':
    app.run_server(debug=True)