import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np


def to_week(x):
    y = -np.flip(x // 7, 0)
    y = y + np.abs(y.min())
    return y



df = pd.read_csv('./data/covid.csv')
df = df.loc[df['Country/Region'] == 'Poland']

df.reset_index(drop=True, inplace=True)
df = df.assign(
    week=lambda df: to_week(df.index)
    )
df = df.groupby('week', as_index=False) \
    .agg({'deaths': np.mean, 'recovered': np.mean, 'confirmed': np.mean})

numdate = [ x for x in range(len(df['week'].unique())) ]



wrong_range = html.Div([
    html.H4("Zakres osi"),
    html.P("Manipulacja zakresem danych, zarówno na osi odciętych jak i rzędnych może prowadzić do błędnej interpretacji danej wizualizacji."),
    html.P("W tym przypadku, wykres pozwala obronić zarówno hipotezę o rozwoju pandemii jak i wypłaszczaniu krzywej zachorowań."),
    html.Div(
        dcc.Graph(id='wrong_range_chart')),
    html.Div([
        html.Label('Wybierz początek osi X'),
        dcc.Slider(
            id='wrong_range_start_date',
            min=numdate[0],
            max=numdate[-1],
            step=1,
            value=numdate[-5],
        ),
        html.Label('Wybierz koniec osi X'),
        dcc.Slider(
            id='wrong_range_end_date',
            min=numdate[0],
            max=numdate[-1],
            step=1,
            value=numdate[-1],
        )
    ])
    ], style={'marginLeft': 450, 'marginRight': 300, 'marginTop': 100, 'marginBottom': 10, 'width': '49%'})

