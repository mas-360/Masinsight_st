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

st.set_page_config(page_title="MASInsight", page_icon=":bar_chart:",layout="wide")

#---logo
img_logo = Image.open("C:/Users/27823/MASINSIGHT/masapp/Images/logo.PNG") 

with st.container():
    image_col, txt_col = st.columns((0.2,1.5))
    with image_col:
        st.image(img_logo)
    with txt_col:
        st.title("MASINSIGHT")

#---HORIZONTAL MENU

selected = option_menu(
    menu_title=None,
    options=["Home", "Data Apps", "Contact"],
    icons=["house", "bar-chart", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#83c5be"},
        "icon": {"color": "#ffffff", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#006d77",
            },
        "nav-link-selected": {"background-color": "#006d77"},
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
    
local_css("C:/Users/27823/MASINSIGHT/masapp/style/style.CSS")

#---LOAD ASSETS---
lottie_coding1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_q5qeoo3q.json")
lottie_coding2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
lottie_coding3 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tCCSYl.json")
img_dash_1 =Image.open("C:/Users/27823/MASINSIGHT/masapp/Images/salesdashscreenshot.PNG") 

if selected == "Home":

    #---HEADER SECTION ---
    with st.container():
        #st.title("MASInsight")
        st.header("Turn your Excel files into an interactive, dynamic data app.")
        st.write("""
                 Visualize your Excel data & become data-driven.
                 
                 """)
        #st.write("[Contact Us >] (https://http://localhost:8501/#get-in-touch)")
        st.button("Contact Us")
        
        
    #--- ABOUT ---
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1,1))
        with left_column:
            st.header("Become data-driven & produce business value.")
            st.write("##")
            st.write(
                """
                Barriers to producing business value indicate lack of necessary technology to improve use of data.
                Whether you're an individual, start-up or business it's now easy & affordable to understand your data and reach your strategic goals.
                """)
        with right_column:
            st_lottie(lottie_coding1, 
                      height=500, 
                      key="coding"
                      ) 
                      
        with st.container():
            st.write("---")
            lft_col, rght_col = st.columns((1,1))
            with lft_col:
                st_lottie(lottie_coding2, 
                          height=500, 
                          key="coding2"
                          ) 
        
            with rght_col:
               st.header("How your data is transformed.")
               st.write("##")
               st.write(
                   """
                   MASINSIGHT transforms your raw data into an interactive data app all using Python.
                   From cleansing, modeling and visualizing into a data app. Turning your information into insights.
                   """)
                           
    with st.container():
        st.write("---")
        left_col, right_col = st.columns((1,1))
        with left_col:
            st.header("Your data is secure.")
            st.write("##")
            st.write(
                """
                All data apps are served entirely over HTTPS ensuring all data is encrypted. 
                You are in control as to who has access & permissions to your data apps in your business. 
                """
            )
        with right_col:
            st_lottie(lottie_coding3, 
                      height=500, 
                      key="coding3"
                      ) 
            
        
    
elif selected == "Data Apps":

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
        st.write("Find out how to get your own data app by filling out the form below.")
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
                    
                    
