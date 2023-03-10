# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:35:34 2023

@author: 27823
"""
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="MASInsight", page_icon=":bar_chart:",layout="centered")
st.title("MASInsight")
#---HORIZONTAL MENU

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#90adcd"},
        "icon": {"color": "#ffffff", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#90adcd",
            },
        "nav-link-selected": {"background-color": "#90adcd"},
    },
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

#---LOAD ASSETS---
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_rznvYX6xOF.json")
img_dash_1 =Image.open("C:/Users/27823/MASINSIGHT/masapp/Images/salesdashscreenshot.PNG")        

if selected == "Home":

    #---HEADER SECTION ---
    with st.container():
        #st.title("MASInsight")
        st.title("Visually dynamic, interactive web app, from your Excel data")
        st.write("""
                 Statistical Modeling to solve Finance and Marketing business Problems in Python
                 
                 """)
        st.write("[Contact Us >] (https://http://localhost:8501/#get-in-touch)")
        st.button("Contact Us")
        
        
    #--- ABOUT ---
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("The affordable industry standard")
            st.write("##")
            st.write(
                """
                WebApp platform is flexible. It evolves to suit your situation, whether you're an individual, startup or business
                MASINSIGHT is helping individuals and startups manage their data and grow their business. No joining fees, no hassle. Perfect for the visual-thinker
                """
            )
        with right_column:
            st_lottie(lottie_coding, 
                      height=500, 
                      key="coding"
                      )    
    
elif selected == "Projects":

    with st.container():
        st.write("---")
        st.header("Are you a visual thinker?")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_dash_1)
        
        with text_column:
            st.subheader("Dashboard 1")
            st.write(
                """
                This dashboard looks at sales data
                
                """
                )
            st.markdown("[View Here](https://app)")    
    
elif selected == "Contact":
        
    #---CONTACT FORM---
    with st.container():
        st.write("---")
        st.header("Get In Touch!")
        st.write("Find out how to get your own web app")
        st.write("##")
        
        contact_form = """
        <form action="https://formsubmit.co/masinsight360@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false"
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email"  placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
       </form>
       """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
                    
                    