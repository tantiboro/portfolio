import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit as st
from streamlit_plotly_events import plotly_events

 
st.title("Streamlit Plotly Events Example: Bank")
df = pd.read_csv("data/bank.csv", sep=';')
 
fig = px.scatter(df, x='day', y="balance", color='job')
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
    st.stop()

selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
 
df_selected = df[
    (df["day"] == selected_x_value)
    & (df["balance"] == selected_y_value)
]
st.write("Data for selected point:")
st.write(df_selected)