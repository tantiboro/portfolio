import streamlit as st
import time
import pandas as pd
#import streamlit as st
#import plotly.express as px
#from streamlit_plotly_events import plotly_events


import requests
#import streamlit as st
 


st.set_page_config(
    page_title="Bank Marketing App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Bank Marketing Campaign: May 2008-November 2010")
st.markdown("<h1 style='text-align: center; color: red;'>This dataset is made publicly available for research by Moro et al. The details are described in [Moro et al., 2014]</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>Please Select a Page form the left side </h1>", unsafe_allow_html=True)


