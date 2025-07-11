import streamlit as st
import numpy as np
from PIL import Image
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import requests
from bs4 import BeautifulSoup

# --- CONFIG ---
MODEL_PATH = "medicinal_model.keras"
TRAIN_DIR = Path("combined_dataset/train")
IMG_SIZE = (224, 224)

# Load class labels
class_names = sorted([d.name for d in TRAIN_DIR.iterdir() if d.is_dir()])

# Load model
@st.cache_resource
def load_trained_model():
    return load_model(MODEL_PATH, compile=False)

model = load_trained_model()

st.title("🌿 Medicinal Plant Identifier")
st.write("Upload a **plant or leaf** image. I'll predict the type and fetch a summarized description.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img_arr = image.img_to_array(img.resize(IMG_SIZE))
    img_arr = np.expand_dims(img_arr, axis=0) / 255.0

    # Predict
    preds = model.predict(img_arr)
    predicted_index = np.argmax(preds)
    predicted_class = class_names[predicted_index]

    # Format prediction
    kind, name = predicted_class.split("_") if "_" in predicted_class else ("", predicted_class)
    label = f"{name.capitalize()} {'Leaf' if kind == 'leaf' else 'Plant'}"
    st.success(f"✅ Predicted: **{label}**")

    # Print actual and predicted values
    st.markdown("### 🔍 Prediction Details")
    st.write(f"**Actual Class:** `{predicted_class}`")

    # Fetch dynamic summary
    st.markdown("### 📘 Summary from the Web")
    try:
        wiki_url = f"https://en.wikipedia.org/wiki/{name.capitalize()}"
        res = requests.get(wiki_url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        p = soup.find("p")
        if p:
            summary = p.get_text().strip().split("\n")[0]
            st.markdown(f"[🌐 Learn more on Wikipedia »]({wiki_url})")
        else:
            raise ValueError("No paragraph found")
    except Exception:
        # Fallback to Healthline
        search_url = f"https://www.healthline.com/search?q={name}"
        st.info("⚠️ Couldn't fetch Wikipedia summary.")
        st.markdown(f"🔎 Try searching for more info here: [Healthline Search for {name}]({search_url})")
