import streamlit as st
from utils import generate_image, edit_image

st.set_page_config(layout="wide", page_title="Imagen App")

# Session state for conversation history and gallery

if "last_image" not in st.session_state:
    st.session_state.last_image = None


if "gallery" not in st.session_state:
    st.session_state.gallery = []


st.title("Imagen App - Text-to-Image and Image Editing with Google Gemini")

prompt = st.text_input("Enter your Prompt:", "")


col1, col2 = st.columns([2, 1])


with col1:
    if st.button("Send"):
        with st.spinner("Generating... Please wait"):
            if st.session_state.last_image is None:
                img = generate_image(prompt)

            else:
                img = edit_image(prompt, st.session_state.last_image)

            st.session_state.last_image = img
            st.session_state.gallery.append(img)

    if st.session_state.last_image is not None:
        st.image(st.session_state.last_image, width=700)


with col2:
    st.subheader("Gallery")
    for idx, image in enumerate(st.session_state.gallery[::-1]):
        st.image(image, width=150)
