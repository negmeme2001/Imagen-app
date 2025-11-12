import streamlit as st
from utils import generate_image, edit_image

st.set_page_config(layout="wide", page_title="Imagen App")

# Session state for conversation history and gallery

if "last_image" not in st.session_state:
    st.session_state.last_image = None


if "gallery" not in st.session_state:
    st.session_state.gallery = []


st.title("Imagen App - Text-to-Image and Image Editing with Google Gemini")

prompt = st.text_input("Enter your prompt:", "")

if st.button("Send", use_container_width=True):
    if prompt.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating... Please wait"):
            if st.session_state.last_image is None:
                img = generate_image(prompt)

            else:
                img = edit_image(prompt, st.session_state.last_image)

            st.session_state.last_image = img
            st.session_state.gallery.append((prompt, img))

# --- Chat-style Display ---
for p, img in reversed(st.session_state.gallery):
    st.markdown(f"**You:** {p}")
    st.image(img, width=700)
    st.markdown("---")