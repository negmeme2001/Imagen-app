# ImageGen App — Summary

This is a small prototype app for generating and editing images using AI models.  
The app is built with **Streamlit** as the UI and **HuggingFace Inference API** as the backend.

## What the App Does
- I send a prompt → the app generates an image.  
- I send another prompt → the app edits the previous image.  
- Simple conversational flow (no extra generate/edit buttons).  
- The app knows when to generate or when to edit based on whether an image already exists.

## Tech Used
- **Python**
- **Streamlit**
- **HuggingFace Hub**
- **uv** (dependency manager)
- **Pillow**
- `.env` for secret keys and model configs

## Models Used
Two different models are used (because most models don’t do both tasks):

- **Text → Image:**  
  `stabilityai/stable-diffusion-xl-base-1.0`

- **Image → Image (edit):**  
  `Qwen/Qwen-Image-Edit`  
  (or any compatible img2img model)

## Project Structure
```
imagegen-app/
├── main.py          # Streamlit app
├── utils.py         # Backend functions (generate/edit)
├── .env             # API keys + model names  
├── README.md
└── pyproject.toml
```


## ✅ How It Works (Simple Flow)
1. User writes a prompt.  
2. If no image exists → generate a new one.  
3. If an image already exists → edit it using the new prompt.  
4. Images and conversation history are kept in session state.