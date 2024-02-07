import streamlit as st
import numpy as np
import time
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

st.set_page_config(page_title='Home', page_icon='🚀' )


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_vfpu2rpp.json"


 

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
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vfpu2rpp.json"),
        )



