import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Virtual assistant for PRO1000 👋")

st.sidebar.success("Select an option above.")

st.markdown(
    """
    This is a virtual setting for a AI-assited personalized learning in a software project management course. 
    You can use this virtual assistant for:  
        + Ask for details, explanation and clarification of information of the projects
        
        + Support your ideation with ideas generations  
        
        + Helping you with generation and refinement of user stories
        
        + Helping you with code generations
        + Helping you with developing test plan and test cases
        + Explain and illustrate for project management concepts you learn, i.e. Agile development, Work Breakdown Structure, Gantt Chart
        + Assist troubleshooting during the planing and execution of your projects
        + Improved the structure and quality of your report
        + Motivate you with the working in the project        
    :red[When working with ChatGPT, be aware of following things. 
First, ChatGPT 3.5 bases on data until 2021 so it not be up to date for some of your questions. 
Second, halluciation can happen when generated text does not make sense as they are not a result of sensory experiences or perceptions. 
Third, be aware of legal compliance and constraints when using generated content within USN context. You can not use text 100% generated in your project report. 
Last but not least, ensure that your personal sensitive information, and or proprietary content is not shared or processed by Chatgpt, 
as it may pose privacy and security risks.  ]
"""
)
