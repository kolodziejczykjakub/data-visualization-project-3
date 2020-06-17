import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from bubbles import get_bubbles


def get_bubbles_tab():
    return html.Div([
        html.Div([
            html.Div([
                html.H3('Nieprawidłowe skalowanie wykresu bąbelkowego'),
            ]),
        ], className="row"),

        html.Div([
            html.Div([
                dcc.Graph(figure=get_bubbles(correct=False)),
                html.H4('Podaj szacunkową wartość'),
                dcc.Markdown("Ile razy więcej zgonów jest w Indiach niż w Chile?"),
                dcc.Input(id='bubbles-input', type='number', value='0', size='10'),
                html.Button(id='bubbles-submit', n_clicks=0, children='Sprawdź'),
            ], className="six columns"),

            html.Div([
                dcc.Graph(id="good-bubbles-chart"),
                dcc.Markdown(id="bubbles-answer"),
                dcc.Markdown(
                    """
                    Tak wygląda prawidłowy wykres. W rzeczywistości odpowiedź na postawione pytanie wynosi około 2.86.
                    Błąd, jaki został popełniony po lewej stronie, to ustalenie promienia bąbelka jako wprost
                    proporcjonalnego do prezentowanej wielkości. Tymczasem w sytuacji, gdy przyglądamy się różnym
                    bąbelkom, większe znaczenie ma powierchnia, jaką zajmuje każdy z nich.
                    """,
                    style={'text-align': 'justify'}
                ),
            ], className="six columns", id="good-bubbles", style={'display': 'none'})
        ], className="row", style={'text-align': 'center'})
    ])


def register_callbacks(app):
    @app.callback([Output('good-bubbles', 'style'),
                  Output('bubbles-answer', 'children'),
                   Output('good-bubbles-chart', 'figure')],
                  [Input('bubbles-submit', 'n_clicks')],
                  [State('bubbles-input', 'value')],
                  )
    def update_output(n_clicks, input):
        btn_clicked = dash.callback_context.triggered[0]['prop_id'] == 'bubbles-submit.n_clicks'
        if btn_clicked:
            style = {'display': 'block'}
            figure = get_bubbles(correct=True)
        else:
            style = {'display': 'none'}
            figure = {}
        text = f'Nieprawidłowy wykres skłonił do odpowiedzi, że w Indiach zmarło {input} razy wiecej osób niż w Chile'
        return style, text, figure
