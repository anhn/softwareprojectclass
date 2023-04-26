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
starting_line = "Let’s roleplay. You are a User Experience teacher"
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
    st.write("Lecture 10 - UX Design principles and evaluation")
    st.write("Learning Objectives")
    st.markdown(""" 
                    + User Experience and User Interface
                    + Product Design and Service Design 
                    + Visual Communication  
                    + Design laws  
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
        Ask for explanation and examples by input a prompt. Example of a prompt: 'Explain to me Gestalt law'.  
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
    image = Image.open('law1.jpg')
    st.image(image, caption='Which Design law this image illustrate?')
    
with tab3:
    st.title("🏢 Exercise space")
    st.markdown ("""
        Implement the following exercise with <a href="https://codepen.io/pen/"> Codepen</a>. You will be asked to share your code later.  
        If you find it difficult, come back to the Theory space and ask the tutor for answer to the exercise with explanation.
    """, unsafe_allow_html=True)
    st.markdown("""
        1. Open the website vnexpress.net. Evaluate the website and identify as many design laws as possible.  

    """)



  

    
    
           
#with st.expander("Not sure what to say to Hannah?"):
#    st.markdown(""" 
#Try some of these:
#```
#1. What do you think are the most important qualities for a successful entrepreneur?
#2. What are the biggest challenges that entrepreneurs face in the early stages of building a business, and how can they overcome them?
#```
#    """)
