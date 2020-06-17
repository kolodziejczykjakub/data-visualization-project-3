import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('./data/covid_cases.csv')
limits = [df.shape[0]//4, df.shape[0]*2//4, df.shape[0]*3//4, df.shape[0]]
cases = df[["confirmed", "deaths", "recovered"]]

first_all = cases.iloc[:limits[0]].values.sum()
first_confirmed, first_deaths, first_recovered = cases.iloc[:limits[0]].sum()
second_all = cases.iloc[limits[0]:limits[1]].values.sum()
second_confirmed, second_deaths, second_recovered = cases.iloc[limits[0]:limits[1]].sum()
third_all = cases.iloc[limits[1]:limits[2]].values.sum()
third_confirmed, third_deaths, third_recovered = cases.iloc[limits[1]:limits[2]].sum()
fourth_all = cases.iloc[limits[2]:limits[3]].values.sum()
fourth_confirmed, fourth_deaths, fourth_recovered = cases.iloc[limits[2]:limits[3]].sum()
cases_first_df = pd.DataFrame.from_dict({'cases': ['confirmed', 'deaths', 'recovered'], 'count': [first_confirmed, first_deaths, first_recovered]})
cases_second_df = pd.DataFrame.from_dict({'cases': ['confirmed', 'deaths', 'recovered'], 'count': [second_confirmed, second_deaths, second_recovered]})
cases_third_df = pd.DataFrame.from_dict({'cases': ['confirmed', 'deaths', 'recovered'], 'count': [third_confirmed, third_deaths, third_recovered]})
cases_fourth_df = pd.DataFrame.from_dict({'cases': ['confirmed', 'deaths', 'recovered'], 'count': [fourth_confirmed, fourth_deaths, fourth_recovered]})

def get_piechart_1():
    fig = px.pie(cases_first_df, values='count', names='cases')
    fig.update_traces(textinfo='none')
    return fig

def get_piechart_2():
    fig = px.pie(cases_second_df, values='count', names='cases')
    fig.update_traces(textinfo='none')
    return fig

def get_piechart_3():
    fig = px.pie(cases_third_df, values='count', names='cases')
    fig.update_traces(textinfo='none')
    return fig

def get_piechart_4():
    fig = px.pie(cases_fourth_df, values='count', names='cases')
    fig.update_traces(textinfo='none')
    return fig

def get_correct_chart():
    x = ['1 ćwiartka','2 ćwiartka','3 ćwiartka','4 ćwiartka']
    confirmed = (pd.Series([first_confirmed/first_all, second_confirmed/second_all, third_confirmed/third_all, fourth_confirmed/fourth_all]) * 100).round(2)
    recovered = (pd.Series([first_recovered/first_all, second_recovered/second_all, third_recovered/third_all, fourth_recovered/fourth_all]) * 100).round(2)
    deaths = (pd.Series([first_deaths/first_all, second_deaths/second_all, third_deaths/third_all, fourth_deaths/fourth_all]) * 100).round(2)
    fig = go.Figure(data=[
        go.Bar(name='confirmed', x=x, y=confirmed, text=confirmed, textposition='auto'),
        go.Bar(name='recovered', x=x, y=recovered, text=recovered, textposition='auto'),
        go.Bar(name='deaths', x=x, y=deaths, text=deaths, textposition='auto'),
    ])
    fig.update_layout(barmode='stack', height=500, width=800, margin=dict(l=50, r=50, t=10, pad=20), autosize=False, paper_bgcolor='rgba(0,0,0,0)')
    return fig

def get_piechart_tab():
    return html.Div([
        html.Div([
            html.Div([
                html.H2('Niepoprawne użycie piechartów i nie wyświetlenie wartości procentowych', style={'text-align': 'center', "margin": '2em'}),
            ]),
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    html.Div('Udział osób zakażonych, wyleczonych i zmarłych z powodu COVID-19 w pierwszej ćwiartce od początku pandemii do teraz.'),
                    dcc.Graph(figure=get_piechart_1()),
                ], className="three columns"),
                html.Div([
                    html.Div('Udział osób zakażonych, wyleczonych i zmarłych z powodu COVID-19 w drugiej ćwiartce od początku pandemii do teraz.'),
                    dcc.Graph(figure=get_piechart_2()),
                ], className="three columns"),
                html.Div([
                    html.Div('Udział osób zakażonych, wyleczonych i zmarłych z powodu COVID-19 w trzeciej ćwiartce od początku pandemii do teraz.'),
                    dcc.Graph(figure=get_piechart_3()),
                ], className="three columns"),
                html.Div([
                    html.Div('Udział osób zakażonych, wyleczonych i zmarłych z powodu COVID-19 w czwartej ćwiartce od początku pandemii do teraz.'),
                    dcc.Graph(figure=get_piechart_4()),
                ], className="three columns"),
            ], className='row', style={'width': '80%', 'margin': 'auto'}
            ),
            html.Div([
                html.H4('Podaj szacunkową wartość'),
                dcc.Markdown("O ile punktów procentowych zmienił się procentowy udział zgonów z drugiej ćwiartki na czwartą?"),
                dcc.Input(id='piecharts-input', type='number', value='0', size='10'),
                html.H4('Odpowiedz'),
                dcc.Markdown("Czy % wyleczeń z drugiej ćwiartki na trzecią wzrósł czy zmalał?"),
                dcc.Dropdown(id='piecharts-dropdown', options=[
                    {'label': "Wzrósł", "value": "up"},
                    {'label': "Zmalał", "value": "down"},
                ], style={"width": "300px", "text-align": 'center', 'display': 'inline-block'}),
                html.Br(),
                html.Button(id='piecharts-submit', n_clicks=0, children='Sprawdź'),
            ], className="row"),
            html.Div([
                html.Hr(),
                html.H6(
                    """
                    Bardziej czytelny jest wykres poniżej. Bez problemu możemy porównać wartości z odpowiednich grup (confirmed, recovered, deaths), a także zbadać tendencje wzrostowe lub malejące.
                    """, style={"margin": '1em'}
                ),
                html.Div('Udział osób zakażonych, wyleczonych i zmarłych z powodu COVID-19 w podziale na cztery ćwiartki pod względem czasu wystąpienia.', style={'margin': '2em'}),
                dcc.Graph(figure=get_correct_chart(), style={'display': 'inline-block'}),
                html.H6("Sprawdzenie odpowiedzi", style={"margin": '1em'}),
                html.Div(id="piecharts-your-answer", style={'width': '80%', 'margin': 'auto'}),
            ], className="row", id="good-piecharts", style={'display': 'none'})
        ], className="row", style={'text-align': 'center', "margin-bottom": '4em'})
    ])


def register_callbacks(app):
    @app.callback(
        [
            Output('good-piecharts', 'style'),
            Output('piecharts-your-answer', 'children'),
        ],
        [
            Input('piecharts-submit', 'n_clicks')
        ],
        [
            State('piecharts-input', 'value'),
            State('piecharts-dropdown', 'value')
        ],
    )
    def update_output(n_clicks, input, dropdown):
        if n_clicks > 0:
            style = {'display': 'block'}
            if dropdown == "up":
                dropdown = "wzrósł"
            elif dropdown == "down":
                dropdown = "zmalał"
            else:
                dropdown = '-'
            your_answer = f"""Odpowiedziałeś, że udział zgonów z drugiej ćwiartki na czwartą zmienił się o {float(input):.2f} punktów procentowych. W rzeczywistości jest to {(third_deaths/third_all-second_deaths/second_all)*100:.2f}.
            Wskazałeś też, że % wyleczeń z drugiej ćwiartki na trzecią {dropdown}. Prawidłową odpowiedzią jest, że wzrósł o zaledwie 0.04%. Trudno odczytać to z wykresów kołowych, wykres typu stacked-bar z podanymi wartościami liczbowymi znacznie to ułatwia."""
        else:
            style = {'display': 'none'}
            your_answer = ""
        return [style, your_answer]
