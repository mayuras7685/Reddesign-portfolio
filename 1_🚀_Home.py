import streamlit as st
import numpy as np
import time
import requests

st.set_page_config(page_title='Home', page_icon='🚀' )


 

with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Hi 👋, I'm Mayur")
        st.subheader(
            """
            I'm Machine Learning Enthusiast. 
            Continuously learning and exploring new ways to apply AI/ML to solve real-world problems. Dedicated to staying up-to-date with the latest developments and advancements.
            """
        )

    with col2:
        st.image('./assets/img/profile-pic.png')



