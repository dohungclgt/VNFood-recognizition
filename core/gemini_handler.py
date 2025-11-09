import streamlit as st
from google import genai
from google.genai import types
import json, re

def analyze_food(image_bytes: bytes, region: str, language: str):
    """
    Gọi Google AI Studio (Gemini API) để nhận diện món ăn và bounding box.
    """

    api_key = st.secrets["general"]["GOOGLE_API_KEY"]
    client = genai.Client(api_key=api_key)

    mime_type = "image/png" if image_bytes[:8].startswith(b"\x89PNG") else "image/jpeg"

    if language == "English":
        prompt = (
            f"This image shows a Vietnamese dish, usually from {region}. "
            "Please analyze it and return JSON with fields: "
            "food_name, confidence (0-100), region, description, how_to_cook, how_to_eat, "
            "and bounding_box (x,y,width,height) of the main dish in the image."
        )
    else:
        prompt = (
            f"Đây là ảnh món ăn Việt Nam, phổ biến ở vùng {region}. "
            "Hãy trả về dữ liệu JSON gồm: "
            "food_name, confidence (0-100), region, description, how_to_cook, how_to_eat, "
            "và bounding_box (x,y,width,height) là tọa độ vùng chứa món ăn chính trong ảnh."
        )

    try:
        response = client.models.generate_content(
            model="models/gemini-2.0-flash-lite",
            contents=[
                types.Part.from_text(text=prompt),
                types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
            ]
        )

        text = response.text.strip()
        cleaned = text.replace("```json", "").replace("```", "").strip()

        match = re.search(r"\{[\s\S]*\}", cleaned)
        if match:
            result = json.loads(match.group(0))
        else:
            result = {"raw_output": cleaned}

        return result

    except Exception as e:
        return {"error": str(e)}
