import streamlit as st
from extract_data import create_dict
from graph import graph

st.set_page_config(layout="wide")

def layout():
    st.title("Väder applikation")
    
    city = st.selectbox("Välj stad:", options=["stockholm", "göteborg", "malmö"])
    st.plotly_chart(graph(create_dict(city)))
        
if __name__ == "__main__":
    layout()