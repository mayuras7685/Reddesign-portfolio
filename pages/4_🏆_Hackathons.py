import streamlit as st
from PIL import Image
st.set_page_config(page_title='Hackathons', page_icon='🏆' )
 

def txt(a, b, c, d, name, hed, img):
   st.header(hed) #Header
   st.image(img) #Imgage 
   st.write(f'{a}') #Description
   st.markdown(f'##### Project: `{name}`')
   st.markdown(f'##### {b}: {c}') #Skills explored during hackthon
   st.markdown(f'##### Project: {d}') #github link

h1 = Image.open('./assets/img/hacksvit.jpg')
h2 = Image.open('./assets/img/hackout.png')
h3 = Image.open('./assets/img/hackthisfall.png')
h4 = Image.open('./assets/img/dotslash.png')
h5 = Image.open('./assets/img/hackvengers.png')
h6 = Image.open('./assets/img/wittyhacks.png')
h7 = Image.open('./assets/img/hack4nu.png')
h8 = Image.open('./assets/img/hack4in.png')


st.title('Hackathons')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["HackSVIT", "Hackout'22", "Hackthisfall 3.0", "DotSlash 6.0", "HackVengers", "WittyHacks 3.0", "HackNUthon 4.0", "Hack for India"])

with tab1:   
   txt('I participated HackSVIT By SVIT, Vasad. it was my first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`React` , `Node.js`, `Mysql`, `Tailwind CSS`',
      'https://github.com/mayuras7685/SVIT-project-api',
      'Happiness Index for Schools',
      'HackSVIT',
      h1)

  

with tab2:
   txt("""I participated in hackathon, Hackout'22 by Synapse at Dhirubhai Ambani Institute of Information and Communication Technology with friends as my teammates. Our project idea was a Happiness index for school with self assessment facilities. (in simple words mood tracking of students and show that in numbers and visuals).
   winning over the hearts and minds of judges, and secured 4th spot on the leaderboard(Special mention award).
""",
      'Skills', 
      '`HTML`, `CSS`, `Flask`, `Mongodb`, `Figma`',
      'https://github.com/mayuras7685/Geek-Unkils_Submission_H22',
      'Happiness Index for Schools',
      "Hackot'22",
      h2)

with tab3:
   txt("""I participated in HackThisFall hackathon, a 36-hour long event     organised by MLH (Major League Hacking), a renowned international hackathon community. It was an incredible experience where I learned about several new technologies which are currently being used in industries. 

   During the event I had the opportunity to explore the postmanapi platform which provides API services and learned about a similar platform Apyhub, also learned Head less CMS (Content Management System) By StoryBlock. 
   Additionally, I gained some valuable insights into  git / github. """,
      'Skills', 
      '`React`, `Tailwind CSS`, `Flask`, `OCR`, `TensorFlow`, `Vercel`',
      'https://github.com/mayuras7685/KU-hackathon',
      'Document Classifier',
      'HackThisFall 3.0',
      h3)

with tab4:
   txt("""DotSlash 6.0 By SVNIT, Surat. Out of 1200+ Registeration we select    for offline round. Our Project idea for this hackathon was Document Classifiacion system, I know you have a question why you recreacting same project? 
       
   Answer was Adding new Feature like KYC Document Classification
        """,
      'Skills', 
      '`React`, `Tailwind CSS`, `Flask`, `OCR`, `TensorFlow`, `Vercel`',
      'https://github.com/mayuras7685/Unkils-DotSlash6.0-Submission',
      'Document Classifier',
      'DotSlash 6.0',
      h4)

with tab5:
   txt("""participated in the Hack-Vengers Hackathon held at Parul University. It was a fantastic experience where we collaborated and created a Wild Animal detection project that we are proud of.

We worked tirelessly to create a custom detection model that detects 6 classes (Lion, Tiger, Hyena, Fox, Wolf, Cheetah) and we are thrilled with the results (71% Accu.).

*I know 71% is less but in 17 hours with no accurate dataset also to improve accuracy we try to train the model with different no. of epochs with different hyper-parameters but internet and colab not worked as well we wanted every time. (Colab's Runtime out or internet disconnects)""",
      'Skills', 
      '`Computer Vision`, `Yolov5`, `Roboflow`, `Colab`',
      'https://github.com/mayuras7685/Unkils_HackVengers',
      'Wild Animal Detection',
      'Hackvengers',
      h5)

with tab6:
   txt("""attended a 36-hour hackathon called Wittyhacks organized by Datacode.in at NMIMS Indore. It was an incredible experience to be a part of this hackathon and showcase our skills and knowledge.

During the hackathon, we worked hard and created a content recommendation system using neural collaborative filtering. We put in a lot of effort, worked late hours, and applied our expertise to develop a unique solution that could help tourists in selecting the right places to visit based on their interests.""",
      'Skills', 
      '`TensorFlow`, `React` , `Node.js`, `Mongodb`',
      'https://github.com/WittyhacksCR003/WH012_Unkils',
      'Tourist Place Recommandtion System',
      'Wittyhacks 3.0',
      h6)

with tab7:
   txt("""attended a 24-hour hackathon called HackNUthon organized by Nirma University. It was an incredible experience to be a part of this hackathon and showcase our skills and knowledge.

During the hackathon, we worked on problem statment provide by Sponsers - Rapidops, automate or Create new feature for CRM, we create dashboard application that capable of sells forecasting, customer churn prediction, chustomer classification etc.. sort of AutoML concept
       
       """,
      'Skills', 
      '`TensorFlow`, `Streamlit` , `Data Manuplation`, `EDA`, `Keras`',
      'https://github.com/mayuras7685/HackNUthon-Unkils',
      'ML for CRM',
      'HackNUthon 4.0',
      h7)

with tab8:
   txt("""attended a 24-hour hackathon called Hack For India organized by Indian Oil and Silver Ock University. It was an incredible experience to be a part of this hackathon and showcase our skills and knowledge.

During the hackathon, we created smart camera for MSMEs, that solves problems like product count, defect detection, Anamoly detection, Risk detection etc. above features in one device Raspberry and atteched Webcam 
       
       """,
      'Skills', 
      '`TensorFlow`, `YOLO` , `Object Detection`, `IOT`, `Instance Detection`',
      'https://github.com/mayuras7685/HackNUthon-Unkils',
      'Smart Imaging Device',
      'Hack For India',
      h8)