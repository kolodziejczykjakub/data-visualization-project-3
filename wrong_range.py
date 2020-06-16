import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np


def to_week(x):
    y = -np.flip(x // 7, 0)
    y = y + np.abs(np.min(y))
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
    html.Div([
        html.Label('Wybierz początek osi Y'),
        dcc.Slider(
            id='wrong_range_start_date',
            min=numdate[0],
            max=numdate[-1],
            step=1,
            value=numdate[-5],
            ),
        html.Label('Wybierz koniec osi Y'),
        dcc.Slider(
            id='wrong_range_end_date',
            min=numdate[0],
            max=numdate[-1],
            step=1,
            value=numdate[-1],
            )
        ]),
    html.Div(
        dcc.Graph(id='wrong_range_chart'))
    ], style={'width': '49%'})

