import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
from tab_3d_issues import tab_3d_issues_layout
from issues_with_3d import low_numbers_15_06_query_values
import wrong_range
import plotly.graph_objects as go
import covid_map
import tab_bubbles
import tab_md

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True


app.layout = html.Div(children=[
    html.H1(children='Błędy wizualizacyjne zaciemniające Pandemię', style={"text-align":'center'}),

    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='O aplikacji', value='tab-1'),
        dcc.Tab(label='Wykresy słupkowe', value='tab-2'),
        dcc.Tab(label='Zakres osi', value='tab-3'),
        dcc.Tab(label='Mapy', value='tab-4'),
        dcc.Tab(label='Wykresy bąbelkowe', value='tab-5'),
        dcc.Tab(label='Wykresy kołowe', value='tab-6'),
    ]),

    html.Div(id='tabs-content')

])




@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Opis aplikacji'),
            html.P('Aplikacja ma za zadanie prezentować typowe błędy wizualizacyjne popełniane przy pokazywaniu stanu epidemiologicznego w Polsce i na świecie.'
                   +' Błędy takie mogą powodować niezrozumienie zbieranych statystyk, a także mogą być stosowane do zwiększania paniki wśród ludzi.'
                    +' Warto zatem znać je i wykrywać, aby nie ulec manipulacji osób tworzących takie wizualizacje.'),
            html.H4('Autorzy'),
            html.Li('Michał Bortkiewicz'),
            html.Li('Michał Dyczko'),
            html.Li('Jakub Kala'),
            html.Li('Damian Kryński'),
            html.Li('Franciszek Grymuła'),
            html.Li('Kamil Ruta'),
            html.P("\n"),
            html.A('Repozytorium', href='https://github.com/jakubkala/data-visualization-project-3')
        ],
            style={'marginLeft': 400, 'marginRight': 400, 'marginTop': 100, 'marginBottom': 10})

    elif tab == 'tab-2':
        return tab_3d_issues_layout

    elif tab == 'tab-3':
        return wrong_range.wrong_range

    elif tab == 'tab-4':
        return covid_map.covid_map

    elif tab == 'tab-5':
        return tab_bubbles.get_bubbles_tab()

    elif tab == 'tab-6':
        return tab_md.get_piechart_tab()


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
            Błąd dla liczby zgonów na Bahama: {}, liczby potwierdzonych przypadków w Brunei: {}, liczby wyleczonych w Burmie: {}
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
            Błąd dla liczby zgonów na Bahama: {}, liczby potwierdzonych przypadków w Brunei: {}, liczby wyleczonych w Burmie: {}
        '''.format(MAE[0], MAE[1], MAE[2])


# wrong range tab callback
@app.callback(
    Output('wrong_range_chart', 'figure'),
    [Input('wrong_range_start_date', 'value'),
     Input('wrong_range_end_date', 'value')]
    )
def update_scale(start, end):
    col = 'deaths'
    df_ = wrong_range.df.loc[start:end, :]
    fig = go.Figure(go.Bar(
        x=df_['week'],
        y=df_[col]
        ))
    fig.update_yaxes(range=[0, wrong_range.df[col].max() + 100])
    fig.update_layout(
        height=500,
        width=700,
        title='Liczba zgonów na COVID w Polsce',
        xaxis_title='Tydzień pandemii',
        yaxis_title='Średnia liczba zgonów'
        )
    return fig


tab_bubbles.register_callbacks(app)
tab_md.register_callbacks(app)


# covid_map callbacks
@app.callback(Output("image", "children"),
              [Input('correctness_level_slider', 'value')])
def display_image(n):
    return html.Img(src=app.get_asset_url(f"map_{n}.png"),
                    style={'text-align':'center'})


@app.callback(Output('image_description', 'children'),
              [Input('correctness_level_slider', 'value')])
def display_description(n):
    return html.Label(covid_map.levels_description_dictionary[n], style={'text-align': "center"})







if __name__ == '__main__':
    app.run_server(debug=False)
