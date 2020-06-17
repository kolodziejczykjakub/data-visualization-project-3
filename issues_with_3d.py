import plotly.express as px
import plotly.graph_objs as go
import base64
import pandas as pd


df = px.data.iris()
iris_group = df.groupby(by="species", ).mean()


covid = pd.read_csv(r"data/covid_cases.csv")
low_numbers = covid[(covid['confirmed']>100) & (covid['confirmed']<500)]
low_numbers_15_06 = low_numbers[low_numbers['date'] == "2020-06-15"].iloc[:5, :]

low_numbers_15_06_query_values = [11, 141, 175]




def encode_img(image_filename):
    return base64.b64encode(open(image_filename, 'rb').read())


def get_encoded_imgs():
    encoded_image1 = encode_img(r'figures/3d_bar_chart_covid.PNG')
    encoded_image2 = encode_img(r'figures/iris_3d_plot2.PNG')
    encoded_image3 = encode_img(r'figures/bar_chart_covid.PNG')

    return encoded_image1, encoded_image2, encoded_image3

def get_3d_scatter_iris():
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                        color='species', size_max=5,  width=900, height=600)

    fig.add_trace(
        go.Scatter3d(
            mode='markers',
            x=iris_group.sepal_length,
            y=iris_group.sepal_width,
            z=iris_group.petal_width,
            marker=dict(
                color=iris_group.species_id,
                size=20,
            ),
            showlegend=False
        )
    )
    return fig


def get_barplot_iris():
    fig = go.Figure(data=[
        go.Bar(name='setosa', x=iris_group.columns[:4].values, y=iris_group.iloc[0, :4].values),
        go.Bar(name='versicolor', x=iris_group.columns[:4].values, y=iris_group.iloc[1, :4].values),
        go.Bar(name='virginica', x=iris_group.columns[:4].values, y=iris_group.iloc[2, :4].values)
    ])
    return fig


def get_barplot_low_numbers_15_06():
    fig = go.Figure(data=[
        go.Bar(name='deaths', x=low_numbers_15_06["Country/Region"].values,
               y=low_numbers_15_06.loc[:, 'deaths'].values, marker_color='red'),
        go.Bar(name='recovered', x=low_numbers_15_06["Country/Region"].values,
               y=low_numbers_15_06.loc[:, 'recovered'].values, marker_color='green'),
        go.Bar(name='confirmed', x=low_numbers_15_06["Country/Region"].values,
               y=low_numbers_15_06.loc[:, 'confirmed'].values, marker_color='goldenrod')
    ])
    fig.update_layout(
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=50
        )
    )
    return fig



def excel_plot():
    fig = go.Figure()

    img_width = 1600
    img_height = 900
    scale_factor = 0.5

    # Add invisible scatter trace.
    # This trace is added to help the autoresize logic work.
    fig.add_trace(
        go.Scatter(
            x=[0, img_width * scale_factor],
            y=[0, img_height * scale_factor],
            mode="markers",
            marker_opacity=0
        )
    )

    # Configure axes
    fig.update_xaxes(
        visible=False,
        range=[0, img_width * scale_factor]
    )

    fig.update_yaxes(
        visible=False,
        range=[0, img_height * scale_factor],
        # the scaleanchor attribute ensures that the aspect ratio stays constant
        scaleanchor="x"
    )

    # Add image
    fig.add_layout_image(
        dict(
            x=0,
            sizex=img_width * scale_factor,
            y=img_height * scale_factor,
            sizey=img_height * scale_factor,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch",
            source=r'figures\3d_bar_chart_covid.PNG')
    )

    # Configure other layout
    fig.update_layout(
        width=img_width * scale_factor,
        height=img_height * scale_factor,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )
    return fig