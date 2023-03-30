import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to my learning space! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This is the homepage of Web Development and Human Computer Interaction course.  
    After completing the course, the student must have the following:  
        Knowledge:   
         + structure and functioning of the Internet and the World Wide Web  
         + fundamental knowledge about HTML and CSS style sheets  
         + fundamental knowledge about Javascript as a programming language  
         + introduction to a Javascript framework for UI - React  
         + elements in the web development process  
        Skill:  
         + plan, design and develop a responsive website using HTML and CSS  
         + carry out a usability assessment of websites, based on the guidelines for user-friendly design and universal design  
         + do basic image processing for the web  
         + use static analysis to analyze the code quality of a web page  
         + take into account differences between browsers when developing web pages  
         + carry out user testing of websites  
         General:  
         + have insight into central professional issues related to web development and HCI  
         + communicate key issues and solution options for websites  
         + plan and implement projects together with others  
         + reflect on own professional practice and adjust this under guidance  
         Learning activities
         + Watching Lecture videos  
         + AI-assited self-learning  
         + Project work: students develop their own websites in a form of project.

"""
)
