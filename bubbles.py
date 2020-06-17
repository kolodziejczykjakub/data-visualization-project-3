import math
import plotly.graph_objects as go
import pandas as pd


def _bubbles(x, y, values, sizes, labels):
    return go.Figure(
        data=[
            go.Scatter(
                x=x, y=y,
                text=labels,
                hovertext=[f'Kraj: {labels[i]}<br>Ilość zgonów: {value}' for i, value in enumerate(values)],
                mode='markers+text',
                marker_size=sizes)
        ], layout=go.Layout(
            title="Liczba zgonów na COVID-19",
            xaxis_title="Procent obywateli jaki stanowią osoby po 70 r.ż.",
            yaxis_title="Wykonane testy",
            height=550
        )
    )


def get_bubbles(correct=True):
    df = pd.read_csv('data/covid_bubbles.csv')
    values = df['total_deaths']
    if correct:
        sizes = [math.sqrt(value) * 2 for value in values]
    else:
        sizes = [value * 0.03 for value in values]
    return _bubbles(df['aged_70_older'], df['total_tests'], values=values, sizes=sizes, labels=df['location'])


def _gen_data():
    locations = {
        'Nigeria': 'Nigeria',
        'Pakistan': 'Pakistan',
        'India': 'Indie',
        'Chile': 'Chile',
        'Russia': 'Rosja',
        'Canada': 'Kanada',
        'Austria': 'Austria'
    }
    df = pd.read_csv('data/owid-covid-data.csv')
    df = df[(df['date'] == '2020-06-15') & (df['total_tests'].notnull()) & (df['location'].isin(locations.keys()))]
    df['total_deaths'] = df['total_deaths'].apply(lambda x: int(x))
    df['location'] = df['location'].apply(lambda x: locations[x])
    df = df[['location', 'total_deaths', 'total_tests', 'aged_70_older']]
    df.to_csv('data/covid_bubbles.csv')


# _gen_data()
