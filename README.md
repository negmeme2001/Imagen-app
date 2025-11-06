# Imagen App — Text-to-Image and Image Editing with Google Gemini

This is a simple prototype app that generates images from text prompts and edits previously generated images using follow-up prompts.  
The UI is built with **Streamlit**, and image generation/editing is done using **Google Gemini**.

---

## What It Does
- Write a prompt → the app generates an image.
- Write another prompt → the app edits the **last generated image**.
- A small gallery keeps all generated versions.

---

## Tech Stack
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Pillow (image handling)
- `uv` for environment & dependency management
- `.env` for API keys and model names

---

## Models Used
| Task | Model |
|------|-------|
| Text → Image | `gemini-2.5-flash-image` |
| Image → Image (edit) | `gemini-2.5-flash-image` |

## Project Structure
```
imagegen-app/
├── main.py          # Streamlit app
├── utils.py         # Backend functions (generate/edit)
├── .env             # API keys + model names  
├── README.md
└── pyproject.toml
```

---

## Run the App Locally

```bash
# Clone the project
git clone https://github.com/negmeme2001/Imagen-app.git
cd Imagen-app

# Install dependencies
uv sync

# Add your environment variables
touch .env

# Run the app
streamlit run main.py
```
## Video demonstration:
[Video](https://github.com/negmeme2001/Imagen-app/issues/1)


Made by Mohamed Ahmed (Negm)
