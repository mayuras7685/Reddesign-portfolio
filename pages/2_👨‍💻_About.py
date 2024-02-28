import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title='About', page_icon='👨‍💻' )

#resume 
pdfFileObj = open('./assets/Mayur_Asodara_Resume.pdf', 'rb')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_vfpu2rpp.json"

with st.container():
   col1, col2 = st.columns([5, 1])
   with col1:
      st.title('About 👨‍💻')
   with col2:
      st.download_button('Resume',pdfFileObj,file_name='mayur_resume.pdf',mime='pdf')
      



with st.container():
      st.write('My name Mayur Asodara, and I am ***Electronics and Communication Engineering*** Undergraduate from VishwaKarma Government College - Ahmedabad.')

      st.write('As an ambitious and hardworking individual, I am constantly seeking opportunities to enhance my knowledge and skills. My passion for Artificial Intelligence and Machine Learning has led me to gain expertise in this field.')
        

   


st.title('Education 📖')

# st.write('-----------')

# with st.container():
#     col3, col4 =st.columns((2,1))
#     with col3:
#         st.write('Vishwakarma Government Engineering College, Ahmedabad')
#         st.text('Bachelors in Engineering: Electronics and Communication ')

#     with col4:
#         st.write('June-2024 ***(expected)***')

# st.write('-----------')

# with st.container():
#     col3, col4 =st.columns((2,1))
#     with col3:
#         st.write('Axay HighSchool, Ahmedabad')
#         st.text('GSHEB (Class XII)')

#     with col4:
#         st.write('March-2020')

# st.write('-----------')

# with st.container():
#     col3, col4 =st.columns((2,1))
#     with col3:
#         st.write('Shriji Vidhyalay, Ahmedabad')
#         st.text('GSHEB (Class X)')

#     with col4:
#         st.write('March-2018')
# st.write('-----------')



txt('**Bachelors in Engineering** (Electronics and Communication), *Vishwakarma Government Engineering College*, Ahmedabad',
'2020-2024')
st.markdown('''
- CGPA: `6.89`

''')

st.write('-----')

txt('**HSC (Class XII)**, *Axay Highschool*, Ahmedabad',
'2020')
st.markdown('''
- Percentage: `69.23`

''')

st.write('-----')

txt('**SSC (Class X)**, *R.J Patel Shriji Vidhyalaya*, Ahmedabad',
'2018')
st.markdown('''
- Percentage: `75.16`

''')


    
# with st.spinner(text="Building line"):
#     with open('timeline.json', "r") as f:
#         data = f.read()
#         timeline(data, height=400)

with st.container():
   col5, col6 = st.columns((2,2))
   with col5:
      st.write('')
   with col6:
      st.write('')

with st.container():
   col7, col8 = st.columns((2,2))
   with col7:
      st.write('')
   with col8:
      st.write('')

st.title('Skills & Tools ⚒️')


# with st.container():
#     col5, col6, col7, col8= st.columns((1, 1, 1, 1))

#     with col5:
#         st.button('Python')
#         st.button('Computer Vision')
#         st.button('NLP')
    
#     with col6:
#         st.button('Flask')
#         st.button('YOLO')
#         st.button('TesorFlow')

#     with col7:
#         st.button('Mongodb')
#         st.button('MySQL')
#         st.button('Tableau')

#     with col8:
#         st.button('Colab')
#         st.button('Streamlit')
#         st.button('FastAPI')
# st.write('-----')


txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Database', '`Mysql`, `Mongodb`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`, `opencv`, `SciPy`')
txt3('Deep Learning', '`TensorFlow`, `Keras`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Tools', '`Power Bi`, `Tableau`, `Colab`, `Roboflow`')
txt3('Model deployment', '`streamlit`, `gradio`, `Heroku`, `Digital Ocean`')




# col11, col12, col13 , col14, col15 = st.columns(5)

# with col11:
#     pass
# with col12:
#     pass
# with col14:
#     pass
# with col15:
#     pass
# with col13 :
#     center_button = st.download_button('Resume',pdfFileObj,file_name='mayur_resume.pdf',mime='pdf')


#resume 
# pdfFileObj = open('mayur_resume.pdf', 'rb')
# st.download_button('Resume',pdfFileObj,file_name='mayur_resume.pdf',mime='pdf')