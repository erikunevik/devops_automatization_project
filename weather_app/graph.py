import plotly.express as px

def graph(data):
    df = data
    fig = px.line(df, x="time", y="degree", title="Vädret för de kommande 24 timmarna ")
    fig.update_layout(
        title={
        "text": "Vädret för de kommande 24 timmarna",
        "x": 0.5,          
        "xanchor": "center"
    },
    xaxis_title="Tid (hh:mm)",
    yaxis_title="Temperatur (°C)"
 
)
    
    
    return fig