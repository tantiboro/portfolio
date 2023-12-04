import pandas as pd
import streamlit as st
import plotly.express as px

import requests
import streamlit as st
 
# add streamlit lottie
from pandas_profiling import ProfileReport
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events
 
df = pd.read_csv("data/bank.csv", sep=';')
fig = px.scatter(df, x="day", y="balance", color="marital")
selected_point = plotly_events(fig, click_event=True)
 
st.subheader("Pandas Profiling of Bank Marketing Dataset")
penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)