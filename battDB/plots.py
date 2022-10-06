import plotly.graph_objs as go
from plotly.offline import plot


def get_html_plot(df):
    """
    Given a pandas.DataFrame object, returns a list of plotly figures
    each of which is a scatter plot of time vs each other column.
    """
    # Get the columns
    cols = df.columns
    # Get the time column
    time_col = [col for col in cols if "time" in col.lower()][0]
    # Get the other columns
    other_cols = [col for col in cols if col != time_col]

    # Create a list of figures
    figures = []
    # For each other column
    for col in other_cols:
        # Create a figure
        fig = go.Figure()
        # Add a scatter plot
        fig.add_trace(
            go.Scatter(
                x=df[time_col],
                y=df[col],
                mode="lines",
                name=col,
                text=col,
                opacity=0.8,
            )
        )
        fig.update_layout(
            title=col,
            xaxis_title=time_col,
            yaxis_title=col,
        )

        # Add the figure to the list
        figures.append(plot(fig, output_type="div", include_plotlyjs=False))
    # Return the list of figures
    return figures
