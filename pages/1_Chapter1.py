from email.policy import default
import os
from decouple import config
import openai
import streamlit as st
from streamlit_chat import message

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
starting_line = "Let’s roleplay. You are an online JavaScript course. Your task is to quickly assess the student’s current JavaScript skill level and present concepts and challenges that will keep the students learning at the edge of their current capabilities, keeping them interested, while also keeping their motivation and enthusiasm for the learning high. Present questions and help them think through questions and learn interactively. If they ask a question, rather than answer directly, try to ask questions that will lead the student to correct answers. Begin by welcoming the student and presenting a syllabus of topics. The topics are: 1. Variables and Data Types. 2. Control Flow and Loops. 3. Functions and Scope. 4. Arrays and Objects.5. DOM Manipulation and Event Handling. After that, presenting a coding exericse for each topic that students can complete in 10-20 minutes for each. Stay on task, and keep track of the lessons that the student has completed. Don’t ask the student to rate themselves. For each question, present the student with tests that their functions must pass to move on to the next challenge."

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

st.title("🏢 Javascript Tutor")

with st.sidebar:
    st.write("Lecture 9 and 10 - Introduction to Javascript")
    st.write("Learning Objectives")
    st.markdown(""" + History of JavaScript   
                    + Variables, data types, operators, and expressions  
                    + Define and call functions in JavaScript  
                    + Control structures: If statements, loops, and switch statements  
                    + Arrays: Creation, manipulation, and iteration of arrays  
                    + Objects: object properties, and methods  
                    + Document Object Model (DOM): Accessing and manipulating HTML elements  
                    + jQuery: easier for DOM manipulation and event handling
                    + Events: Responding to user actions with event listeners  
    """)    
#    if st.button("Heading, paragraphs, newline and lists"):
#            cathy_line = get_response("You are an online JavaScript course. Can you explain details the concepts and give code examples for each of them. The concepts are Heading, paragraphs, newline and lists in HTML")
            
st.write ("Use the topics in the sidebar to form a prompt. Ask for example. Example of a prompt: 'Tell me variables, datatypes, operators and expression in Javascript. Give code example to illusrate as detailed as possible'.")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

with st.form("my_form"):
   jim_line = st.text_area("Write you command here","", height=10, key='option')
   # Every form must have a submit button.
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
    
#def get_text():
#    input_text = st.text_area("","", height=10, key='option')
#    return input_text
#jim_line = get_text()

#if jim_line:
#    cathy_line = get_response(jim_line)
#    st.session_state.past.append(jim_line)
#    st.session_state.generated.append(cathy_line)

if st.session_state['generated']:  
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.markdown(""" :mailbox: Tutor: """ + st.session_state["generated"][i])
        st.markdown(""" :mailbox: You: """ + st.session_state['past'][i])
           
#with st.expander("Not sure what to say to Hannah?"):
#    st.markdown(""" 
#Try some of these:
#```
#1. What do you think are the most important qualities for a successful entrepreneur?
#2. What are the biggest challenges that entrepreneurs face in the early stages of building a business, and how can they overcome them?
#```
#    """)
