import plotly.express as px
import streamlit as st

color_scale = px.colors.qualitative.Vivid

class Plot:
    def __init__(self) -> None:
         pass
    
    def plot_bar_chart(self, dataframe, x, y, title=None):
        fig = px.bar(dataframe, x = x, y=y, title=title, color_discrete_sequence=color_scale)
        st.plotly_chart(fig, use_container_width=True)
    
    def plot_pie_chart(self, dataframe, names, values, title=None):
        fig = px.pie(dataframe, values = values, names=names, title=title)
        st.plotly_chart(fig, use_container_width=True)
    
    def plot_grouped_bar(self, dataframe, x, y, color, title=None):
        fig = px.bar(dataframe, x=x, y=y, color=color, barmode="group", title=title)
        st.plotly_chart(fig, use_container_width=True)