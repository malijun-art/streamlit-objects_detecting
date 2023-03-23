import streamlit as st

st.set_page_config(page_title = "home",
                   layout = 'wide',
                   page_icon='./images/home.png')

st.title ("ChunHong Xiao's Image Coding Project")
st.caption('this web is demostrating the functions')

st.markdown("""
### this app detects objects from Images
- Automatically detects 20 objects from images
- [Click here for App](/YOLO_for_image/)


""")
