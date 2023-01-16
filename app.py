import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Henry Mugai Portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()
    

#---load assets---
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_qam8tww4.json")

#----header section---
st.subheader("Hi, I am Henry Mugai :wave:")
st.title("A junior data analyst from Kenya")
st.write("A junior data scientist with a strong background in statistics and programming. Skilled in data analysis, visualization, and machine learning. Experienced in using tools such as tableau and Python for data analysis and modeling. Strong problem-solving and communication skills, able to effectively present insights and findings to both technical and non-technical audiences. Always eager to learn and stay up-to-date with the latest developments in the field.")
st.write("[learn more >](https://www.linkedin.com/in/henry-mugai/)")


#----skills---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("SKILLS")
        st.write("##")
        st.write(
            """
            
            1.Research. 

            2.Analytical skills.

            3.Machine learning.

            4.Data visualisation.

            5.Strong communication skills.

            6.Problem-solving.
            """
        )

#----what i do----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WHAT I DO")
        st.write("##")
        st.write(
            """
            As a data scientist in the agri-tech industry, my role is to

            1.Harness the power of data to drive innovation and improve crop yields.

            2.Work closely with farmers, agronomists, and other stakeholders to gather and analyze large sets of data, using advanced statistical and machine learning techniques to identify patterns and trends.

            3.Develop predictive models that help farmers make more informed decisions,

            4.Use data visualization and communication techniques to present findings and insights to stakeholders in a clear and actionable way.

            Overall, 
            my goal is to use data to help farmers produce more food, with fewer resources and a lower environmental impact.
            """
        )
        st.write("[Mkulima Farms >]()")
    with right_column:
        st.image('images\henry mugai.JPG')

# ---- PROJECTS ----

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image('images\photo.jpg')
    with text_column:
        st.subheader("Dashboard to output the KCPE results for a primary school since its founding")
        st.write(
            """
            The dashboard shows visualisations for the kcpe results of a primary school
             by year and also by subject perfomance
            """
        )
        st.markdown("[View Dashboard...](https://henrymugai-silverstream-app-70r2tu.streamlitapp.com/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('images\mkulima farm.jpg')
    with text_column:
        st.subheader("An intergrated platform for agri-trends")
        st.write(
            """
            A work in progress where farmers, investors and any agri-interested participants
            can view the latest agri-trends and news  on all sectors of agriculture from 
            crop production to livestock keping.
        
            """
        )
        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('images\inv.jpg')
    with text_column:
        st.subheader(" Top investment ideas ")
        st.write(
            """
          a written atticle based on data that shows the types of top investment ideas. 
        
            """
        )
        st.markdown("[View article...](https://henrymugai-investment-ideas-app-lh73wz.streamlit.app/)") 
#--contact---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

contact_form = """
    <form action="https://formsubmit.co/henrymugai36@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()  
