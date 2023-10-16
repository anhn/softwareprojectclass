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
starting_line = " Lets roleplay. Act as a project owner who will convert three lab rooms at USN Bø campus into a co-working space named USNStart at Bø campus, the main building. The coworking space is in a planing phase and will be open by the end of the year. You will get 3 rooms in an area of 500 meter square together. It will include:
Open Workspace: This is the heart of a coworking space, featuring flexible seating arrangements with communal desks, tables, and chairs. It's suitable for individual work, informal meetings, and collaborative projects. There are space for 60 individual working here.
Private offices: Small, fully-furnished offices that can accommodate individuals or small teams, offering more privacy and a dedicated workspace. The total capacities are 6 private offices.
Meeting rooms: Various-sized meeting rooms equipped with projectors and whiteboards for presentations, client meetings, or team discussions. There are 5 meeting rooms in total
Lounge Area: Comfortable seating areas, often with sofas and coffee tables, providing a relaxed atmosphere for informal meetings or relaxation.
Kitchen and Dining Area: A well-equipped kitchen or kitchenette with facilities for preparing meals and dining. It also offer complimentary coffee, tea, and snacks.
Printing and Scanning area: Equipment for printing, scanning, and photocopying documents.
Game room:A recreational space with games like billiard, ping-pong, or video games, encouraging breaks and social interaction.
There are also a plenty of parking places. As of today, the tenants are Revisorteam, YourCompanion, GreenEnergy and VismaAI who seat in private offices.
We want to attract students who want to work and become entrepreurs. We want to also attract individuals who work in groups - larger companies centrally in our cities, who live in the region and/or want to move to the region, and in that way take their work home and then be able to sit in a co-working building, where they meet other like-minded people and not alone in a home office. There are available offers for seating in the coworking space:
Day Pass: Day passes allow members to access the coworking space for a single day. This cost 699 nok per day
Monthly Membership: Monthly memberships grant unlimited access to the coworking space for a fixed monthly fee. This costs 6000 nok per month
Student membership: the membership for students. This cost 9000 per semester (6 months)
Annual Fixed desk: members may have their own desk within the enclosed office space, which offers more privacy and can accommodate small teams. This costs 50.000 nok per year
Private Office Desk: In private offices, members may have their own desk within the enclosed office space, which offers more privacy and can accommodate small teams. This cost 20.000 nok per month per office
I would like to create a landing page to increase our visibility, and attracting customers to us. We want to have:
Clear and Engaging Headline: Start with a clear, attention-grabbing headline that communicates the core value of your coworking space.
Compelling Visuals: Use high-quality images or videos of the coworking space, showcasing the interior, workstations, communal areas, and facilities. You come up with your own ideas about the interior design of the space
Membership Plans and Pricing: Display your membership options, pricing, and any special offers or discounts prominently. Include a call-to-action (CTA) button to encourage visitors to explore plans.
Amenities and Facilities: List the key amenities and facilities available in your coworking space, such as high-speed internet, meeting rooms, coffee lounge, and more. Highlight what makes your space unique.
Location Information: Clearly state your coworking space's location, including the address, a map, and information about nearby public transportation or parking options.
Testimonials and Reviews: Include positive testimonials or reviews from current members. Real feedback can build trust and credibility.
Contact Information: Provide multiple contact options, including an email address, phone number, and a contact form. Make it easy for potential members to get in touch.
About Us Section: Share a brief overview of your coworking space's history, mission, and values. Highlight what makes your community unique.
Responsive Design: Ensure that the landing page is responsive and mobile-friendly, so it displays correctly on all devices and screen sizes.
Privacy and Security: Include a section about data privacy and security to reassure potential members that their information will be protected.
Floor plan: showing the proposed floor plan and images of interior designs
Booking: allow people with daypass or monthly membership can book available desks in the open workspace with the current month. A floor map should be displayed and desk selection should be interactive and visual in the map. A member can only choose to book one desk for one day at a time. A confirmation should be displayed after the reservation is done.
Project Brief: USNStart Coworking Space Website
The primary objective of this project is to create a dynamic and engaging website for USNStart Coworking Space, located at the Bø campus of the University of South-Eastern Norway (USN). The website should serve as an informative, user-friendly, and visually appealing platform to attract potential members, provide information about our coworking space, and facilitate desk booking for members. The website should implement all requirements described above.
The scope of the project encompasses the design, development, and launch of the USNStart Coworking Space website. This includes, but is not limited to:
Development of a responsive website accessible on desktop, tablet, and mobile devices.
Design and layout of the website, considering the provided interior design concepts and floor plan.
Creation of pages and content that convey key information about the coworking space, membership plans, and existing tenants.
Inclusion of images, videos, and visuals to showcase the interior and amenities.
Integration of privacy and security measures to protect user data.
Coordination with project stakeholders for feedback and review.

We are very flexible with design ideas. For website design inspiration see:
https://meshcommunity.com/hubs/digs/
https://www.wework.com/l/coworking-space/oslo
https://www.spacesworks.com/nb/oslo-nb/kvadraturen/

We are also flexible with the floor map ideas. For inspiration, see:
https://pin.it/3sLJ0EQ
https://pin.it/43gdiRI
https://workdesign.com/wp-content/uploads/2012/11/Coworking-Concept-Floor-Plan-720x405.jpg

The desk reservation function is in a very early stage. We want your proposal, both about the process of booking and the user exeprience of the booking process.

We do not have any brand design yet. You are all free to design the logo, color palette, typography and icons.

Technically, we want prototypes to be maded with Figma. The prototypes should be interactive with multiple screens.
The final website should be implemented using HTML, CSS and Javascript. Any supporting tool to generate the code is allowed, for instance siter.io, or chatgpt. The website can be static, without the backend. Implementation of the backend part is a plus. In the end, the website should be hosted and published (just for the purpose of this course). It is NOT allowed to use any Content Management Systems (Wordpress, Webflow, etc). The code should be written or generated from scratch. We can ignore other aspects of web publication, such as Web analytics, SEO and interoperability.

In order to test the landing page, i would like to run usability test with some students in the campus for the landing page and the booking function.

The project will start from second week of January 2024 and end at the end of April 2024.

The success of the USNStart Coworking Space website project can be evaluated based on various criteria. Success in this context can be measured in terms of meeting project objectives, delivering value to the target audience, and achieving the desired outcomes. Here are the criteria of success for this project:
Alignment with Project Objectives: The website effectively aligns with the project objectives as defined in the project brief, including creating an engaging online presence for the coworking space and facilitating desk bookings.
Fullfillment of all user stories: all stated user stories should be documented, analyzed, prototyped, implemented and tested
Quality of the visual elements: the visual elements should be comparable to the given examples
Quality and scope of codebase: codebase should be at a reasonable size for a team of four developers working in a month.
Usability test: The website should meet or exceed the expectations of its target audience, in this case to test with students.
Demonstration of Agile team: team should work and follow Agile practices. 
Teamwork: the extent that teams frequently meet, and team maturity demonstrated via the evolution of the type of team issues overtime
Quality of document: the project report should be written clearly with reasonable reading flow, logcal organization of sections. Avoidance of jargon and use of language appropriate for the target audience. Proper format a document with page numbers, captions for tables, figures, explanation for abbreviations, high resolution for included figures, have a reference section.
Students may need to ask questions, seek clarifications, or provide progress updates during the development process. Communication should be done via email. Each email should has a title - PRO1000 - Groupnumber - Main points to communicate. Email should be sent to angu@usn.no 

Please use this persona to provide feedback and guidance as students to collect requirements, clarify student concerns, answer their questions and guide them to develop and evaluate the landing page.  Now wait for student's questions. Try to be as detailed as possible. If the questions from students not clear enough to give them a detailed answer, than ask them to clarify or give more details in their questions. For each question, try to define and explain a concept or term if the student introduces them in their questions. Try to answer questions in paragraphs, if using bullet points, should not list more than seven points and ask students to ask further to get the remaining part of the answer."
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
    st.write("Lecture 9 - Introduction to Javascript")
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

tab1, tab2 = st.tabs(["Theory Space", "Exercise Space"])

with tab1:
    st.title("🏢 Theory space")
    st.markdown ("""
        Ask for explanation and examples by input a prompt.
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
        5. How do you create an object in JavaScript?  
        6. What is DOM manipulation in JavaScript?  
        7. Which company developed JavaScript?  
        8. What is === operator?  
        9. Create a function that takes two numbers as parameters and returns their sum.  
        10. Write a program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user (e.g. 'Too high' or 'Too low') until the correct number is guessed.
    """)

  
#        5. What is an object in JavaScript?  
#        6. What are the difference between While... and Do... While loop?  
#        9. How do you select an element from the DOM using JavaScript?  
#        10. How do you select an element from the DOM using JavaScript jQuery?  
#        11. How do you add or remove an event listener in Javascript?  
#        12. How do you dispatch an event in JavaScript?  
#        13. How do you use event delegation in JavaScript to handle events for multiple elements?  
#        14. In JavaScript what is an argument object?  

#        16. What are undeclared and undefined variables?  
#        17. Which symbol is used for comments in Javascript?  
#        19. How can the style/class of an element be changed?  
#        20. How to read and write a file using JavaScript?  
#        21. What would be the result of 3+2+”7″?  
#        22. What do you mean by NULL in Javascript?  
#        23. What are JavaScript Cookies?  
#        24. What are the different types of errors in JavaScript?  
#        25. What is the difference between JavaScript and Jscript?  
#        26. What is the ‘Strict Mode in JavaScript, and how can it be enabled?  
#        27. How to create an anonymous function in JavaScript?  
#        28. Is JavaScript case sensitive?  
#        29. What are some important JavaScript Unit Testing Frameworks?  
#        30. What is OOPS Concept in JavaScript?]


#with tab3:
#    st.title("🏢 Exercise space")
#    st.markdown ("""
#        Implement the following exercise with <a href="https://codepen.io/pen/"> Codepen</a>. You will be asked to share your code later.  
#        If you find it difficult, come back to the Theory space and ask the tutor for answer to the exercise with explanation.
#    """, unsafe_allow_html=True)
#    st.markdown("""
#        1. Create a function that takes two numbers as parameters and returns their sum.  
#        2. Write a program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user (e.g. 'Too high' or 'Too low') until the correct number is guessed.
#        3. Write a function that takes an array of numbers as input and returns the sum of all the numbers in the array.  
#        4. Write a program that asks the user to enter a number and then checks if the number is even or odd. The program should print "even" or "odd" to the console.  
#        5. Write a function that takes a string as input and returns true if the string is a palindrome (i.e. reads the same backward as forward), false otherwise.  
#        6. Create a program that takes a temperature in Celsius as input and converts it to Fahrenheit.  
#        7. Write a program that changes the background color of the <body> element when a button is clicked.  
#        8. Write a program that creates a form with two input fields (one for the name and one for the email address) and a submit button. When the user submits the form, create a new <div> element with the user's name and email address and append it to the <body> element.  
#        9. Create a program that hides a <div> element when a button is clicked using jQuery.  
#        10. Write a program that changes the color of a <div> element when the mouse hovers over it.  
#
#    """)
  
    
           
#with st.expander("Not sure what to say to Hannah?"):
#    st.markdown(""" 
#Try some of these:
#```
#1. What do you think are the most important qualities for a successful entrepreneur?
#2. What are the biggest challenges that entrepreneurs face in the early stages of building a business, and how can they overcome them?
#```
#    """)
st.markdown(
    """
    This is a virtual setting for a AI-assited personalized learning in a software project management course. 
    You can use this virtual assistant for:  
        + Ask for details, explanation and clarification of information of the project
        + Support your ideation with ideas generations
        + Helping you with generation and refinement of user stories
        + Helping you with code generations
        + Helping you with developing test plan and test cases
        + Explain and illustrate for project management concepts you learn, i.e. Agile development, Work Breakdown Structure, Gantt Chart
        + Assist troubleshooting during the planing and execution of your projects
        + Improved the structure and quality of your report
        + Motivate you with the working in the project        
   
    :red[When working with ChatGPT, be aware of following things. First, ChatGPT 3.5 bases on data until 2021 so it not be up to date for some of your questions. 
Second, halluciation can happen when generated text does not make sense as they are not a result of sensory experiences or perceptions. 
Third, be aware of legal compliance and constraints when using generated content within USN context. You can not use text 100% generated in your project report. 
Last but not least, ensure that your personal sensitive information, and or proprietary content is not shared or processed by Chatgpt, 
as it may pose privacy and security risks.]
"""
)
