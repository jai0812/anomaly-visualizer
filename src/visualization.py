import plotly.express as px

def visualize_anomalies(df, x, y):
    fig = px.scatter(
        df, x=x, y=y, color='Anomaly',
        color_discrete_map={'Normal':'blue','Outlier':'red'},
        title=f"Anomaly Detection: {x} vs {y}",
        template="plotly_white"
    )
    return fig

