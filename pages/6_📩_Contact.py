import streamlit as st

st.set_page_config(page_title='Contact', page_icon='📩' )

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

st.header("Get In Touch With Me! :mailbox:")


contact_form = """
<form action="https://formsubmit.co/ff6747cbb4a74572c6abb8eeb4b26785" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


with st.container():
   col7, col8 = st.columns((2,2))
   with col7:
      st.write('')
   with col8:
      st.write('')

st.header('Social Media 🌐')
txt2('LinkedIn', 'https://www.linkedin.com/in/mayur-asodara-366067206/')
txt2('Twitter', 'https://twitter.com/MayurAsodara')
txt2('GitHub', 'https://github.com/mayuras7685/')
txt2('Instagram', 'https://instagram.com/mayur_7685/')

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")