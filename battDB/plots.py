import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots


def get_html_plot(df, x_col: str, y_cols: list):
    """
    Given a pandas.DataFrame object, returns a plotly figure which is a scatter plot
    of each column in y_cols vs x_col. If len(y_cols) == 1, this is a simple x-y scatter
    plot, if len(y_cols) == 2, one y_col is on the left of the plot and the other is on
    the right, if len(y_cols) > 2, an exception is raised.
    Args: df (pandas.DataFrame): the dataframe to plot
          x_col (str): the column to plot on the x-axis
          y_cols (list): the columns to plot on the y-axis
    Returns: plotly figure
    """
    if not 0 < len(y_cols) < 3:
        raise ValueError("y_cols must have length 1 or 2")
    # Create a figure
    fig = fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add first scatter plot
    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[y_cols[0]],
            mode="lines",
            name=y_cols[0],
            text=y_cols[0],
            opacity=0.8,
        )
    )

    # If there's a second column
    if len(y_cols) == 2:
        # Add second scatter plot
        fig.add_trace(
            go.Scatter(
                x=df[x_col],
                y=df[y_cols[1]],
                mode="lines",
                name=y_cols[1],
                text=y_cols[1],
                opacity=0.8,
            ),
            secondary_y=True,
        )
        fig.update_layout(title=" vs ".join(y_cols))

    else:
        fig.update_layout(title=y_cols[0])

    fig.update_layout(xaxis_title=x_col)

    # Return the figure
    return plot(fig, output_type="div", include_plotlyjs=False)
