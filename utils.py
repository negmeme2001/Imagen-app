import os 
from io import BytesIO
from PIL import Image
from google import genai
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL")


if API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not set in .env")

if MODEL is None:
    raise ValueError("GEMINI_MODEL is not set in .env")


_client = genai.Client(api_key=API_KEY)


def extract_image(response) -> Image.Image:
    for cand in getattr(response, "candidates", []):
        content = getattr(cand, "content", None)
        if not content:
            continue
        for part in content.parts:
            if hasattr(part, "inline_data") and part.inline_data and part.inline_data.data:
                img_bytes = part.inline_data.data
                return Image.open(BytesIO(img_bytes)).convert("RGBA")
    raise ValueError("No image found in response.")

def generate_image(prompt: str) -> Image.Image:
    """Generate an image using Text-prompt 
    Text ---> Image using Gemini 2.5 Flash
    """
    try:
        if not prompt or prompt.strip() == "":
            raise ValueError("Prompt cannot be empty")

        # New HF client supports direct PIL images
        response = _client.models.generate_content(
            model=MODEL, 
            contents=[prompt],
            )

        return extract_image(response)  # Return the first generated image
    except Exception as e:
        print(f"Error generating image: {e}")
        raise

def edit_image(prompt: str , base_image: Image.Image) -> Image.Image:
    """Edit an existing image using prompt
    Image + Text ---> Image using Gemini 2.5 Flash
    """
    try:
        if not prompt or prompt.strip() == "":
            raise ValueError("Prompt cannot be empty")

        response = _client.models.generate_content(
            model=MODEL,
            contents=[prompt, base_image]
        )

        return extract_image(response)
    except Exception as e:
        print(f"Error editing image: {e}")
        raise

