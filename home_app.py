import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# CS301 - Web Development and HCI 👋")

st.sidebar.success("Select a lecture above.")

st.markdown(
    """
    This is the experimental setting for a AI-assited active learning in IT study. The hypothesis was that with a proper use of AI tools, in this case, a GPT-based chatbot, the motivation and learning outcome is improved for students in online setting.
    We applied this novel concept in teaching our course Web Development and Human Computer Interaction course.  
    Each student in the class is equipped with a chatbot as their private tutor.  
    You can use your tutor for:  
        + Personalized support by answering questions, explanations, and feedback on work  
        + Give solutions to your difficult work  
        + Explain and debug your code  
        + Answering your questions regarding the connection of the study and future career  
        + Improved learning outcomes  
        + Facilitation of peer-to-peer learning  
        + Diagnosis of misunderstandings, targeted instruction  
        + Support for self-directed learning, resources, and study tips  
        + Increased your autonomy and ownership of learning  
    Start by selecting the lecture in the sidebar.
"""
)
