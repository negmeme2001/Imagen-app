import streamlit as st
from utils import generate_image, edit_image


prompt = st.text_input("Your Prompt:")

if st.button("Send"):
    if 'last_image' not in st.session_state:
        st.session_state.last_image = None
        img = generate_image(prompt)

    else:
        img = edit_image(prompt, st.session_state.last_image)

    st.session_state.last_image = img
    st.image(img)