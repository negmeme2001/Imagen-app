import os
from io import BytesIO
from PIL import Image
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


load_dotenv()

HF_TOKEN=os.getenv("HUGGINGFACE_API_KEY")
GEN_MODEL=os.getenv("MODEL_TO_GENERATE")
EDIT_MODEL=os.getenv("MODEL_TO_EDIT")


if HF_TOKEN is None:
    raise ValueError("HUGGINGFACE_TOKEN is not set in .env")

if GEN_MODEL is None:
    raise ValueError("MODEL_TO_GENERATE is not set in .env")

if EDIT_MODEL is None:
    raise ValueError("MODEL_TO_EDIT is not set in .env")

def pil_to_bytes(img: Image.Image, fmt="PNG"):
    """Convert a PIL image to raw bytes"""
    buffer = BytesIO()
    img.save(buffer, format=fmt)
    buffer.seek(0)
    return buffer.read()

def bytes_to_pil(data: bytes):
    """Convert raw image bytes to a PIL image"""
    return Image.open(BytesIO(data)).convert("RGB")

def generate_image(prompt: str) -> Image.Image:
    """Generate an image using Text-prompt 
    using Model from Huggingface 
    """
    client = InferenceClient(GEN_MODEL, token=HF_TOKEN)

    #New HF client supports direct PIL images
    response = client.text_to_image(prompt)

    return response  # Return the first generated image

def edit_image(prompt: str , base_image: Image.Image) -> Image.Image:
    """Edit an existing image using prompt and use different model from huggingface"""
    client = InferenceClient(EDIT_MODEL, token=HF_TOKEN)
    # Send img+prompt to img2img pipeline
    response = client.image_to_image(image=base_image, prompt=prompt)

    return response

