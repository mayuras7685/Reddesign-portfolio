import streamlit as st
from PIL import Image

st.set_page_config(page_title='Projects', page_icon='🗂️' )


st.title('Projects')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assets/img/p2.png'))
  with col2:
    st.subheader("Wild Animal Detection")
    st.write("""
   Custom object detection model that detects 6 classes (Tiger, Lion, Hyena, Cheetah, Wolf, Fox) and And came up with an Interface that detects Wild animals from webcam feed, images, and URLs of images
             """)

    st.markdown('`Computer Vision`, `openncv-python`, `RCNN`, `Yolo`, `Roboflow`, `colab` ')

    g1 = '[GitHub](https://github.com/mayuras7685/Deadly_animal_detection)'
    st.markdown(g1)

st.write('---')

with st.container():
  col3,col4 = st.columns((1, 2))
  with col3:
    st.image(Image.open('./assets/img/p5.png'))
  with col4:
    st.subheader("Underwater Trash Detection")
    st.write("""Developed an underwater trash plastic detection project using YOLOv5 and YOLOv8 by training custom datasets. This project includes two models: one based on YOLOv5 for object detection and another using YOLOv8 for instance segmentation.""")

    st.markdown('`Computer Vision`, `openncv-python`, `Yolo`, `Roboflow`, `colab` ')

    g2 = '[GitHub](https://github.com/mayuras7685/Under_water_trash_plastic_detection)'
    st.markdown(g2)

st.write('---')

with st.container():
  col5,col6 = st.columns((1, 2))
  with col5:
    st.image(Image.open('./assets/img/p1.png'))
  with col6:
    st.subheader("Olympic Data Analysis Web Application")
    st.write("""
    This analysis will provide detailed and accurate information regarding various factors which leads to the evolution of Olympic Games and improvement of Countries/Players over the time in visual format.
    """)

    st.markdown('`EDA`, `Streamlit`, `pandas`, `matplotlib`, `plotly`, `seaborn`')

    g3 = '[GitHub](https://github.com/mayuras7685/Olympics-data-analysis)'
    st.markdown(g3)

st.write('---')

with st.container():
  col7,col8 = st.columns((1, 2))
  with col7:
    st.image(Image.open('./assets/img/p4.png'))
  with col8:
    st.subheader("US Road Accidents Data Analysis")
    st.write("""This project focuses on analyzing and visualizing the US road accidents dataset to gain insights into various aspects of accidents, such as their frequency, severity, time distribution, and geographic distribution. 7 million data points, more than 13500 cities & 49 states coverd in this Analysis """)

    st.markdown('`EDA`, `Streamlit`, `pandas`, `matplotlib`, `plotly`, `seaborn`')

    g4 = '[GitHub](https://github.com/mayuras7685/US_Accident_Analysis)'
    st.markdown(g4)

st.write('---')

with st.container():
  col9,col10 = st.columns((1, 2))
  with col9:
    st.image(Image.open('./assets/img/p3.png'))
  with col10:
    st.subheader("Portfolio Website Using Streamlit")
    st.write("""Portfolio Website using Streamlit library, multi page stremlit webapp to showcase my work and skills """)

    st.markdown('`Python`, `Streamlit`')

    g5 = '[GitHub](https://github.com/mayuras7685/portfolio)'
    st.markdown(g5)

