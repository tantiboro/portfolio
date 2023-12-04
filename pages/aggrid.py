import sys, os
sys.path.append('/home/tantiboro/anaconda3/envs/data_science/lib/python3.8/site-packages')
#sys.path.remove("/home/tantiboro/.local/lib/python3.10/site-packages")
import pandas as pd
import streamlit as st
import streamlit as st
import plotly.express as px


import seaborn as sns
import matplotlib.pyplot as plt
from st_aggrid import AgGrid, GridOptionsBuilder 
st.set_page_config(layout="wide")
#Show celebratory balloons
st.snow()

st.title("Streamlit AgGrid Example: Bank Marketing Project")

@st.cache_data
def load_data():
    #loading the data with pandas
    df = pd.read_csv("data/bank-full.csv", sep=';') 
    return df
df = load_data()
#AgGrid(df, height=400) 


shouldDisplayPivoted = st.checkbox('Pivot df on Month')

gb = GridOptionsBuilder()

#Makescolumns resizable, sortable and filterable by default

gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=True
)

# Configure balance to have a 80px initial width
gb.configure_column(field='age', header_name="Age", width=80)

#configure job column to have a tooltip and adjust to fill the grid container
gb.configure_column(
    field='job',
    header_name="Job Title",
    width = 200,
    #flex=3,
    tooltipField='job'
)
gb.configure_column(field='housing',header_name="Type of Housing", width=120, tooltipFiel='housing')
gb.configure_column(field='marital', header_name="Marital Status", width=200 )
gb.configure_column(field='duration', header_name='Level of Education', width=120)

gb.configure_column(
    field='month',
    header_name='Month of the Campagn',
    width=150,
    type=['numericColumn'],
    #valueFormatter='value.toLocalString()',
    pivot=True,
    hide=False
)
gb.configure_column(
    field='day',
    header_name='Day of the month',
    width=150,
    type=['numericColumn'],
    #valueFormatter='value.toLocalString()',
    pivot=True,
    #hide=True
)
gb.configure_column(
    field='balance',
    header_name='Balance[$]',
    #width=120,
    flex=1,
    type=['numericColumn'],
    #valueFormatter='value.toLocalString()',
    aggFunc="sum",
    valueFormatter="scientific"
)
gb.configure_grid_options(
    tooltipShowDelay=0,
    pivotMode=shouldDisplayPivoted
)

go = gb.build()
AgGrid(df, gridOptions=go, height=400)


st.subheader("Define a custom colorscale")
fig = px.histogram(
    df,
    y='balance',
    x='month',
    color='education',
    title='Monthly Balance per Education Level'
    #color_continuous_scale='reds'
)
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

g = df['month'].value_counts()
# Declaring exploding pie
#explode = [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0.4, 0.4, 0.4]
plt.figure(figsize=(8,8))
colors = sns.color_palette('pastel')[0:11]
keys= ['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'jan', 'feb','mar', 'apr', 'sep']
fig = px.pie(g, values=g.values, labels=keys, width=400, height=400, hole=.3, title="Number of Phone Calls Per Month")
# Set the title
#px.title("Number of Phone Calls Per Month")
#Save the plot
#px.savefig('figure_1.png')
#Show the plot
#fig.show()
st.plotly_chart(fig, use_container_width=True)
