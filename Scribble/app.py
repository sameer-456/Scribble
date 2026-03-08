import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils.ocr_processor import enhance_image, extract_text
from utils.ai_processor import process_with_ai
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configure Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# UI Title
st.title("📝 Scribble to Digital")
st.write("Convert messy handwritten notes into clean text & to-do lists")

# Upload Image
uploaded_file = st.file_uploader("Upload notes image", type=["jpg", "png", "jpeg"])

if uploaded_file:

    # Show Uploaded Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to array
    img_array = np.array(image)

    # Enhance image
    enhanced = enhance_image(img_array)
    st.image(enhanced, caption="Enhanced Image", use_column_width=True)

    # OCR Extraction
    with st.spinner("🔍 Extracting text with OCR..."):
        raw_text = extract_text(enhanced)

    st.subheader("📄 Raw OCR Text")
    st.text(raw_text)

    # AI Processing
    if st.button("✨ Convert to Digital"):
        with st.spinner("🤖 Processing with AI..."):

            result = process_with_ai(raw_text)

            st.subheader("✅ Digital Output")
            st.text(result.replace("\n", " ").strip())