"""About page shown when the user enters the application"""
import streamlit as st


#"""Used to write the about page in the app.py file"""
st.title("Page on construction:")
st.markdown(
            """## Who Am I?
"<h1 style='text-align: center; color: blue;'>I am a scientist with several years of pratical experiences. I am open to new ideas and technologies to make the world a better place"</h1>

A Data Scientist with 5 years of experience in solving Business Problems, 
a constant learner and a firm believer of experimentation over expertise. 
Always on the lookout for new technologies, I am passionate about designing Data driven solutions which are easy, economical and can be scaled.
 
**Tanti Ouattara**\n
**Data Science | Business Analytics | Project Management **

[**LinkedIn**](https://www.linkedin.com/in/tanti-ouattara/) | [**Email**](mailto:tantiboro@gmail.com)

## The Project
I came across **Streamlit** last week while looking for solution to host python apps on AWS EC2. 
The Framework  boasts of being the easiest and the fastest way of creating interactive apps, and after spending just a 
few hours creating this interactive resume, I can vouch for that. 

Check out my [**GitHub**](https://github.com/tantiboro) for the implementation. Reach out to me for any project or a simple discussion on Streamlit.
Also check out their [**page**](https://www.streamlit.io/) for more more information and updates.
Also check out this amazing implementation of Streamlit by [**Marc Skov Madsen**](http://awesome-streamlit.org/) for streamlit inspiration.


""",
            unsafe_allow_html=True,
        )

"""Skills page shown when the user enters the application"""



"""Used to write the page in the app.py file"""
st.title("Skills :shinto_shrine:")
st.markdown(
            """"<h1 style='text-align: center; color: black;'>
              Languages
- R
- Python
- SQL 
- VBA

<h1 style='text-align: center; color: black;'>
Platforms and Libraries\n
- **SAS** - JMP, Enterprise Miner and Enterprise Guide
- **MS Office** - Excel, Powerpoint, Project, Word
- **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Tensorflow, Keras, Streamlit, Dash, Plotly, Matplotlib, Seaborn, etc.
- **R** - Shiny, Dplyr
- **SQL** - MS SQL, PostgreSQL 
- Tableau
- chembl
- rdkit
- PowerBI
- JIRA, Confluence

<h1 style='text-align: center; color: black;'>
 Analytical Skills\n
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Web Scraping

<h1 style='text-align: center; color: black;'>
 AWS Stack\n
- EC2\n
- Lambda
- S3
- RDS - Redshift, Aurora, MS SQL
- Dynamo DB
- Sagemaker
- IAM
            





</h1>""",
            unsafe_allow_html=True,
        )
