import streamlit as st
from streamlit_option_menu import option_menu
from load_image import load_image
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.models import load_model

def streamlit_menu():
    selected = option_menu(
        menu_title=None, 
        options=["Home", "Project","Team","Contact","Demo"],  
        icons=["house", "book","people", "envelope","search"], 
        menu_icon="cast",  
        default_index=0,  
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {
                   "font-size": "20px",
                   "color": "black",
                   "text-align": "left",
                   "margin": "0px",
                   "--hover-color": "#eee",
                   },
                   "nav-link-selected": {"background-color": "green"},
                   },
                   )
    return selected


selected = streamlit_menu()

if selected == "Home":
    st.title(f"Banana leaves diseases detection using CNN")
    st.image("https://p1.pxfuel.com/preview/176/296/904/dji-uav-plant-protection-drone-farmland-agriculture-plant-protection.jpg",use_column_width='always')


    
if selected == "Project":
    st.title(f"About this project")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Introduction")
        st.write('Agriculture playing a big role', ' in sustainable development goals', 'especially in no poverty, zero hunger and  good health and well-being')
        
        
    with col2:
        st.subheader("Problem")
        
    with col3:
        st.subheader("Solution")
        #st.image("")




if selected == "Team":
    st.title(f"Person behind this project")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Marie-Ritha")
        st.image("https://avatars.githubusercontent.com/u/71000965?v=4",use_column_width='always')
    with col2:
        st.header("Savanna")
        st.image("https://mail.google.com/mail/u/0?ui=2&ik=937fe5ec2c&attid=0.1&permmsgid=msg-a:r-7038484383381289472&th=180861147d2657b8&view=att&disp=safe&realattid=f_l2p2eoxn0",use_column_width='always')
    with col3:
        st.header("Florentine")
        #st.image("")
     
if selected == "Contact":
    st.title(f"Contact us")


if selected == "Demo":
    st.header("Test our model here")
    img_file=st.file_uploader('upload your image here', accept_multiple_files=False, type=['.jpg','.png'])
    
    if img_file is not None:
        show_img = st.image(load_image(img_file),use_column_width='always')
        img = np.array(Image.open(img_file))
        img = img/255
       
        submit=st.button('Classify')
        if submit:
            model = load_model('model.h5')
            model.predict(img)            

