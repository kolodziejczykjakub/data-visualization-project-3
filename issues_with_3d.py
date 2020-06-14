import plotly.express as px
import plotly.graph_objs as go
import base64

df = px.data.iris()
iris_group = df.groupby(by="species", ).mean()

def encode_img(image_filename):
    return base64.b64encode(open(image_filename, 'rb').read())


def get_encoded_imgs():
    encoded_image1 = encode_img(r'figures\3d_bar_chart.PNG')
    encoded_image2 = encode_img(r'figures\iris_3d_plot2.PNG')
    return encoded_image1, encoded_image2

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
