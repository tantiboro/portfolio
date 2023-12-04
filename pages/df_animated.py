import pandas as pd
import streamlit as st

import plotly.express as px


import requests
import streamlit as st
 
# add streamlit lottie
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events
 
 
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
 
 
# lottie_penguin = load_lottieurl(
#     "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
# )
 
# st_lottie(lottie_penguin, height=600)
 
# st.title("Streamlit Plotly Events + Lottie Example: Bank")
#https://lottiefiles.com/animations/ux-ui-design-section-lottie-json-animation-58vX3xSuad
# import streamlit as st
# from streamlit_lottie import st_lottie

# with st.echo():
#     st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello")

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()