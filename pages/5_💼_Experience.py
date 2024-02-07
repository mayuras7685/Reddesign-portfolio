import streamlit as st

st.set_page_config(page_title='Experience', page_icon='💼' )

st.title('Experience')
st.write("Nothing ever becomes real 'til it is experienced.― John Keats")


with st.container():
    col1, col2 =st.columns((1, 2))
    with col1:
        st.image('https://www.pct.org.in/assets/img/favicon.png')
    with col2:
        st.subheader('Prayatna Charitable Trust')
        st.write('Python Developer Trainee')
        st.markdown('''
        - Taught the basics of Python and AI-ML to the students of 9th to 12th standard in Rural Area.
        - Made some AI and ML projects related real life problems with students.
        ''')