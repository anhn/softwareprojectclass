from email.policy import default
import os
from decouple import config
import openai
import streamlit as st
from streamlit_chat import message
from PIL import Image

openai.api_key = st.secrets["OPENAI_KEY"]

st.set_page_config(
    page_icon='🏢',
    page_title='Your Javascript tutor',
    menu_items={
        'Get Help': 'https://join.slack.com/t/officechatbot/shared_invite/zt-14rlr8chh-C~rwJN~~KUAX~DOkvcno1g',
        'Report a bug': "https://github.com/anhn/streamlit-example/issues/new",
        'About': "This chatbot is tailored by Anh Nguyen-Duc for trying a virtual project assistant "
    }
)
cathy_line =''
jim_line = ''
starting_line = "Let’s roleplay. You are a React JS teacher"
def get_response(jim_line):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": starting_line},
            {"role": "user", "content": jim_line},
        ],
        max_tokens = 1024,
        temperature = 0.5,
    )
    output = completions.choices[0]["message"]["content"].strip()
    return output 

with st.sidebar:
    st.write("Lecture 11 - Introduction to React JS")
    st.write("Learning Objectives")
    st.markdown(""" 
                    + ReactJS vs traditional Javascript
                    + Environment: Node.js and NPM 
                    + Understanding JSX
                    + Components and Props
                    + State
                    + Rendering HTML elements
                    + Hello world - React App
    """)    
#    if st.button("Heading, paragraphs, newline and lists"):
#            cathy_line = get_response("You are an online JavaScript course. Can you explain details the concepts and give code examples for each of them.")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

tab1, tab2, tab3 = st.tabs(["Theory Space", "Job Interview Questions", "Exercise Space"])

with tab1:
    st.title("🏢 Theory space")
    st.markdown ("""
        Explore each of the learning topics (in the sidebar) with your tutor.  
        Ask for explanation and examples by input a prompt. Example of a prompt: 'Guide me to create a hello world React JS app'.  
        If you have other questions, please type  <a href="https://www.menti.com/aljeqx5dziyr"> your question here</a>   
    """, unsafe_allow_html=True)
    with st.form("my_form"):
        jim_line = st.text_area("Write you command here","", height=10, key='option')
        historyIncluded = st.checkbox('Add the last chat to input')
        submitted = st.form_submit_button("Submit")
        if submitted:
            if jim_line:
                if historyIncluded:
                    jim_line_long = st.session_state["past"][len(st.session_state['past'])-1] + st.session_state["generated"][len(st.session_state['generated'])-1] + jim_line
                    cathy_line = get_response(jim_line_long)
                else:
                    cathy_line = get_response(jim_line)
                st.session_state.past.append(jim_line)
                st.session_state.generated.append(cathy_line)
    if st.session_state['generated']:  
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.markdown(""" :mailbox: :red[Tutor:] """ + st.session_state["generated"][i])
            st.markdown(""" :mailbox: :blue[You:] """ + st.session_state['past'][i])

with tab2:
    st.title("🏢 Check your knowledge")



with tab3:
    st.title("🏢 Exercise space")
    st.markdown ("""
        Implement the following exercise with <a href="https://codepen.io/mercuryworks/pen/EyQaBO"> Codepen</a>. You can enter React code in the JS (Babel) column
    """, unsafe_allow_html=True)
    st.markdown("""
        1. Create a React component (extend React.Component) that renders a form with two input fields: one for a username and one for a password. When the form is submitted, log the values of the inputs to the console.  
        2. Create a React component that renders an image. Pass the image source and alt text as props.
        3. Create a React component that renders a counter. The component should have two buttons: one to increment the count and one to decrement the count. Display the current count as text.
        4. Create a React component that renders a table of data. Pass the data as an array prop. Each row in the table should correspond to an element in the array, and each column should correspond to a property of the object in the array.

    """)



  

    
    
           
#with st.expander("Not sure what to say to Hannah?"):
#    st.markdown(""" 
#Try some of these:
#```
#1. What do you think are the most important qualities for a successful entrepreneur?
#2. What are the biggest challenges that entrepreneurs face in the early stages of building a business, and how can they overcome them?
#```
#    """)