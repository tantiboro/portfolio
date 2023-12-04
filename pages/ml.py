import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import pickle


# a function to load the saved model
def load_model():
    with open('pipeline2.pkl', 'rb') as f_in:
        model = pickle.load(f_in)
    return  model
model = load_model()
# Create the user input data
customer = {
    
    'age': "age",
    'job': 'job',
    'marital': 'marital',
    'education': "education",
    'default': 'default',
    'balance': 'balance',
    'housing': "housing",
    'loan': 'loan',
    'contact': 'contant',
    'day': "day",
    'month': 'month',
    'duration': 'duration',
    'campaign': "campaign",
    'pdays': "pdays",
    'previous': "previous",
    'poutcome': "poutcome"
}
def predict_single(X):
    # cat = customer[categorical + numerical].to_dict(orient='rows')
    # dv = DictVectorizer(sparse=False)
    # dv.fit(cat)
    X = pd.DataFrame([customer])
    y_pred = model.predict(X)
    print(y_pred)
    return y_pred

# def show_model_page():
st.markdown("<h1 style='text-align: center; color: red;'>Bank Marketing Campaign Project</h1>", unsafe_allow_html=True)

    # html_temp = """
    # <div style="background-color:tomato;padding:10px">
    
    # """

    # st.markdown(html_temp, unsafe_allow_html=True) 
st.markdown("<h4 style='text-align: center; color: green;'>This application is not associated with the Kiva organization and does not guarantee any funding. Our goal is to help you process your application</h4>", unsafe_allow_html=True)
    #st.title("Funding application Process") 

    #st.markdown(html_temp, unsafe_allow_html=True)

    #st.subheader(""" We need some information to predict outcome of your loan""")
st.markdown("<h3 style='text-align: center; color: blue;'>Thank you for using our application. Please select your sector name, your currency policy from the dropdown menu on the left. Do not forget to add the loan amount needed in US dollars and click on the submit button </h3>", unsafe_allow_html=True)
    
age = st.number_input('Insert the applicant age', value=0.00)
customer['age'] = age
job = st.selectbox('What is the applicant occupation?:', ('unemployed', 'services', 'management', 'technician', 'admin.', 'unknown', 'housemaid', 'entrepreneur', 'student', 'blue_collar', 'self-employed', 'retired'))
marital = st.selectbox('What is the applicnt marital status?:', ('married', 'divorced', 'single'))
education = st.selectbox('Insert the applicant education level:', ('primary', 'secondary', 'tertiary', 'unknown'))
default = st.selectbox('Has the applicant defaulted on previous loan?:', ('yes', 'no'))
balance = st.number_input('What is the applicant balance?:')
customer['balance'] = balance
housing = st.selectbox('Does the applicant leave alone or with family?', ('yes', 'no'))
loan = st.selectbox('Does the applicant have a personal loan?', ('yes', 'no'))
contact = st.selectbox('What is the applicant communication contact type?:', ('cellular', 'unknown', 'telephone'))
day = st.number_input('What is the last contact day of the month?:')
customer['day'] = day
month = st.selectbox('Insert the last month of the year:', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
duration = st.number_input('What is the duration of the last contact in seconds?:')
customer['duration'] = duration
campaign = st.number_input('How many times this person has been contacted during this campaign including this one?:')
customer['campaign'] = campaign
pdays = st.number_input('How many days have passed since this person has been contacted?:')
customer['pdays'] = pdays
previous = st.number_input('How many times this person has been contacted in previous compaigns?:')
customer['previous'] = previous
poutcome = st.selectbox('What is the outcome of the previous marketing campaign for this client?:', ('unknown', 'other', 'failure', 'success'))
customer['poutcome'] = poutcome
    
    

ok = st.button("Submit your Application ")
if ok:
    X = pd.DataFrame([customer])
    result = predict_single(X)
    st.write('The current number is ', result)    
    if result >= 0.5:
        st.balloons()
        st.markdown("<h2 style='text-align: center; color: black;'>Good luck to the next step of the process</h2>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: black;'>CONGRATULATIONS</h1>", unsafe_allow_html=True)
    else:
            #st.write("Do not be discouraged. Please redefine your application")
        st.markdown("<h2 style='text-align: center; color: red;'>Don't be discourage, Please redefine your application</h2>", unsafe_allow_html=True)
        #st.header( prediction)
    st.markdown("<h1 style='text-align: center; color: green;'>Results</h1>", unsafe_allow_html=True)
X = pd.DataFrame([customer])
# result = predict_single(X)
# st.write('The current number is ', result)

from PIL import Image
image = Image.open('data/figure_1.png')
col1, col2, col3, col4 = st.columns([12,20,20,12])

with col1:
    st.markdown("<h1 style='text-align: center; color: blue;'>MORE THAN 70 % OF THE CALL WERE DONE FROM MAY TO AUGUST</h1>", unsafe_allow_html=True)
        #st.subheader("How Do I my goals?")

with col2:
    st.image(image, width=600)
with col3:
    st.write("")
with col4:
    st.markdown("<h2 style='text-align: center; color: green;'> May IS THE BUSIER MONTH, AVERAGING MORE CALLS THAN THE PERIOD FROM SEPTEMBER TO APRIL</h2>", unsafe_allow_html=True)
        #st.subheader("Machine learning or Artificial Intelligence may be your best Toolkit")
    #st.image(image, width=400, caption='Road To Unknown')
    