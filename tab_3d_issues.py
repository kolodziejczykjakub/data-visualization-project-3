import dash_core_components as dcc
import dash_html_components as html

from issues_with_3d import *


encoded_image1, encoded_image2, encoded_image3 = get_encoded_imgs()
fig = get_3d_scatter_iris()
fig1 = get_barplot_iris()

fig2 = get_barplot_low_numbers_15_06()

tab_3d_issues_layout = html.Div([
            html.Div([
                html.Div([
                    # html.H3('Issues with third dimension on bar plots'),
                    html.H3('Problemy z trzecim wymiarem na wykresach słupkowych.'),
                ], className="six columns"),

                html.Div([
                    # html.H4('Most annoying issues:'),
                    # dcc.Markdown('''
                    # * It is difficult to find the exact values on the bar.
                    # * Bars in the back may be hidden.
                    # * Bars in the back appear smaller than they really are.
                    # '''),
                    html.H4('Najczęstsze problemy:'),
                    dcc.Markdown('''
                    * Cięzko odczytać dokładną wartość wysokości słupka.
                    * Słupki z tyłu są przysłonięte prze te na przedzie.
                    * Słupki z tyłu wydają się mniejsze niż faktycznie są.
                    '''),
                ], className="six columns"),

            ], className="row"),

            html.Div([
                html.Div([
                    # html.H4('arRedundant third dimension on the b plot'),
                    html.H4('Wykres ze zbędnym trzecim wymiarem.'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),
                             style={'height':'80%', 'width':'80%'}),
                    # dcc.Graph(figure=fig3)
                ], className="six columns"),

                html.Div([
                    # html.H4('It is better to stick to two dimensions'),
                    html.H4('Poprawny wykres dwuwymiarowy.'),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),
                             style={'height': '130%', 'width': '100%'}),
                ], className="six columns"),

            ], className="row"),

            html.Div([
                html.Div([
                    # html.H4('Write your estimated values for the first plot:'),
                    # dcc.Markdown("Enter values for Bahamas deaths, Brunei confirmed cases and Burma recovered :"),
                    html.H4('Oszacuj wysokości poniżej wymienionych słupków dla pierwszego wykresu:'),
                    dcc.Markdown("Wprowadź oszacowane wartości dla liczby zgonów na Bahama, liczby potwierdzonych przypadków w Brunei oraz liczby wyleczonych w Burmie:"),
                    dcc.Input(id='input_bar11', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar12', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar13', type='number', value='0', size='10'),
                    html.Button(id='submit_button_bar1', n_clicks=0, children='Submit'),
                    html.Div(id='output_bar1')
                ], className="six columns"),

                html.Div([
                    # html.H4('Write your estimated values for the second plot:'),
                    # dcc.Markdown("Enter values for Bahamas deaths, Brunei confirmed cases and Burma recovered :"),
                    html.H4('Oszacuj wysokości poniżej wymienionych słupków dla drugiego wykresu:'),
                    dcc.Markdown("Wprowadź oszacowane wartości dla liczby zgonów na Bahama, liczby potwierdzonych przypadków w Brunei oraz liczby wyleczonych w Burmie:"),
                    dcc.Input(id='input_bar21', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar22', type='number', value='0', size='10'),
                    dcc.Input(id='input_bar23', type='number', value='0', size='10'),
                    html.Button(id='submit_button_bar2', n_clicks=0, children='Submit'),
                    html.Div(id='output_bar2')
                ], className="six columns")
            ], className="row"),


            html.Div([
                html.Div([
                    # html.H4('Check real values on second plot:'),
                    html.H4('Sprawdź rzeczywiste wartości wysokości słupków:'),
                    dcc.Graph(figure=fig2),
                ], className="twelve columns"),

            ], className="row")
        ])