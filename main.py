import streamlit as st
from utils import generate_image, edit_image


prompt = st.text_input("Your Prompt:")

if st.button("Send"):
    if st.session_state.get("last_image") is None:
        img = generate_image(prompt)

    else:
        img = edit_image(prompt, st.session_state.last_image)

    st.session_state.last_image = img
    st.image(img)