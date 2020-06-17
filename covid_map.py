import dash_core_components as dcc
import dash_html_components as html

levels_description_dictionary = {
    1: "1. Źle dobrane - cykliczne - mapowanie wartości na kolorów może sugerować, że ilość zachorowań w Polsce i Rosji jest taka sama...",
    2: "2. Legenda dodana do kolorów umożliwia zrozumienie wizualizacji, ale nie umożliwia wyciągania poprawnych wniosków",
    3: "3. Zmiana mapowania wartości na kolory na mapowanie sekwencyjne pozwala zobaczyć relację między ilościami zachorowań w poszczególnych krajach \n" +
       "Jednak przełamanie standardu - pokazanie najmniejszych wartości najciemniejszym kolorem - zdecydowania pogarsza zrozumienie wizualizacji.",
    4: "4. Dodanie legendy umożliwia pełne zrozumienie wizualizacji, jednak nie jest ona wygodna i intuicyjna ze względu na przełamanie pewnego schematu...",
    5: "5. Sekwencyjne mapowanie wartości na kolory w taki sposób, by największe wartości były najciemniejsze jest pewnym standardem, " +
       "który pozwala zrozumieć przekaz wizualizacji nawet bez dodawania legendy.",
    6: "6. Dodana legenda pozwala zrozumieć i odczytać dość dokładnie wszystkie zależności między zachorowaniami w poszczególnych państwach. \n" +
       "Ciągle jednak można poprawić czytelność wykresu, zmieniając liczbę zachorowań na inną miarę - np. liczbę zachorowań na mln mieszkańców lub na jednostkę obszaru taką jak km2"
}

center_style = style = {"display": " block",
                        "margin-left": "auto",
                        "margin-right": "auto",
                        "width": "80%"}

center_style_2 = {"width": "50%", "margin-left": "auto", "margin-right": "auto"}

covid_map = html.Div([
    html.Div([
        html.H3('Wybierz poziom czytelności mapy i spróbuj wywnioskować, który kraj ma najwięcej zachorowań.',
                style={"text-align": "center"}),
        html.Div(id='slider',
                 children=[
                     dcc.Slider(
                         id='correctness_level_slider',
                         min=1,
                         max=6,
                         marks={
                             1: {'label': '1', 'style': {'color': '#ff0000', "font-size": "25px"}},
                             2: {'label': '2', 'style': {'color': '#ff5900', "font-size": "25px"}},
                             3: {'label': '3', 'style': {'color': '#ff9d00', "font-size": "25px"}},
                             4: {'label': '4', 'style': {'color': '#ffff00', "font-size": "25px"}},
                             5: {'label': '5', 'style': {'color': '#55ff00', "font-size": "25px"}},
                             6: {'label': '6', 'style': {'color': '#00ff00', "font-size": "25px"}},
                         },
                         value=1,
                         dots=True,
                     )],
                 style=center_style_2
                 ),
        html.Div(id="image", style={'text-align':'center'}),
        html.Div(id="image_description", style={"text-align": "center", "font-size": "25px"})
    ], style=center_style)
])
