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
starting_line = "Let’s roleplay. You are a Javascript teacher"
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
    st.write("Lecture 9 and 10 - Introduction to Javascript")
    st.write("Learning Objectives")
    st.markdown(""" 
                    + History of JavaScript  
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
        Ask for explanation and examples by input a prompt. Example of a prompt: 'Explain to me variables, datatypes, operators and expression in Javascript. Give code example to illusrate as detailed as possible'.  
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
    st.markdown("""
    Preparing for a JavaScript interview involves researching less familiar topics with a solution-oriented approach. But before that, you need to know very well the fundamentals.  
    Below is the list of questions extracted from job interviews about Javascript programming knowledge:  
        :violet[1. List all primitive data types in Javascript  
        2. What is the difference between let, const, and var in JavaScript?  
        3. How do you declare a function in JavaScript?  
        4. What are different between arrays in javascript and array in java?  
        5. What is an object in JavaScript?  
        6. How do you create an object in JavaScript?  
        7. What are the difference between While... and Do... While loop?  
        8. What is DOM manipulation in JavaScript?  
        9. How do you select an element from the DOM using JavaScript?  
        10. How do you select an element from the DOM using JavaScript jQuery?  
        11. How do you add or remove an event listener in Javascript?  
        12. How do you dispatch an event in JavaScript?  
        13. How do you use event delegation in JavaScript to handle events for multiple elements?  
        14. In JavaScript what is an argument object?  
        15. Which company developed JavaScript?  
        16. What are undeclared and undefined variables?  
        17. Which symbol is used for comments in Javascript?  
        18. What is === operator?  
        19. How can the style/class of an element be changed?  
        20. How to read and write a file using JavaScript?  
        21. What would be the result of 3+2+”7″?  
        22. What do you mean by NULL in Javascript?  
        23. What are JavaScript Cookies?  
        24. What are the different types of errors in JavaScript?  
        25. What is the difference between JavaScript and Jscript?  
        26. What is the ‘Strict Mode in JavaScript, and how can it be enabled?  
        27. How to create an anonymous function in JavaScript?  
        28. Is JavaScript case sensitive?  
        29. What are some important JavaScript Unit Testing Frameworks?  
        30. What is OOPS Concept in JavaScript?]

    """)


with tab3:
    st.title("🏢 Exercise space")
    st.markdown ("""
        Implement the following exercise with <a href="https://codepen.io/pen/"> Codepen</a>. You will be asked to share your code later.  
        If you find it difficult, come back to the Theory space and ask the tutor for answer to the exercise with explanation.
    """, unsafe_allow_html=True)
    st.markdown("""
        1. Create a function that takes two numbers as parameters and returns their sum.  
        2. Write a program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user (e.g. 'Too high' or 'Too low') until the correct number is guessed.
        3. Write a function that takes an array of numbers as input and returns the sum of all the numbers in the array.  
        4. Write a program that asks the user to enter a number and then checks if the number is even or odd. The program should print "even" or "odd" to the console.  
        5. Write a function that takes a string as input and returns true if the string is a palindrome (i.e. reads the same backward as forward), false otherwise.  
        6. Create a program that takes a temperature in Celsius as input and converts it to Fahrenheit.  
        7. Write a program that changes the background color of the <body> element when a button is clicked.  
        8. Write a program that creates a form with two input fields (one for the name and one for the email address) and a submit button. When the user submits the form, create a new <div> element with the user's name and email address and append it to the <body> element.  
        9. Create a program that hides a <div> element when a button is clicked using jQuery.  
        10. Write a program that changes the color of a <div> element when the mouse hovers over it.  

    """)



  

    
    
           
#with st.expander("Not sure what to say to Hannah?"):
#    st.markdown(""" 
#Try some of these:
#```
#1. What do you think are the most important qualities for a successful entrepreneur?
#2. What are the biggest challenges that entrepreneurs face in the early stages of building a business, and how can they overcome them?
#```
#    """)
