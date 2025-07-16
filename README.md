# 🧠 Medicinal Plant Classifier & Identifier

This project uses **deep learning (VGG16)** to classify medicinal plants based on uploaded **leaf or full plant** images. It includes a web app built with **Streamlit** that instantly predicts the plant class and fetches live summaries from **Wikipedia** or **Healthline**.

---

## 🌿 Project Motivation

Identifying medicinal plants accurately is essential for:
- Traditional medicine
- Agriculture
- Biodiversity conservation

Since users may provide either **leaf** or **full-plant** images, a **VGG16 CNN** model was fine-tuned using both views to increase robustness and prediction reliability in real-world conditions.

---

## 📁 Dataset Structure

To support dual image types (leaf and plant), the dataset is structured as follows:








### ✅ Why `*_leaf` and `*_plant` folders?
- Helps the model learn both macro (plant) and micro (leaf) level features.
- Increases classification accuracy when input type varies.
- Supports flexibility for field or lab-based image input.

---

## 🧠 Model Architecture

| Component | Details |
|----------|---------|
| **Base Model** | VGG16 (ImageNet pre-trained) |
| **Input Size** | 224 × 224 × 3 |
| **Final Layers** | Flatten → Dense → Dropout → Softmax |
| **Output Classes** | Based on total folders in `combined_dataset/train/` |
| **Loss Function** | Categorical Crossentropy |
| **Optimizer** | Adam |

---

## 🚀 Key Features

- 🌱 Upload plant or leaf image
- 🧠 Real-time prediction with high accuracy
- 📄 Dynamically fetched plant summary
- 🔗 Wikipedia or Healthline links for reference
- ✅ Shows both **actual class** and **predicted class**
- 📷 Displays uploaded image with label

---

## 🖥️ Streamlit App (`app.py`)

Functionality:
- Load `.keras` model from disk
- Accept uploaded image (JPG, PNG)
- Resize to `(224, 224)`, normalize
- Predict class (e.g., `neem_leaf`, `neem_plant`)
- Convert label to readable format
- Fetch description from:
  - ✅ Wikipedia (first attempt)
  - 🔁 Healthline or search fallback
- Display:
  - Image
  - Actual and predicted label
  - Link and dynamic summary

---

## 📦 Installation & Usage

### 🔧 Install dependencies
```bash
pip install -r requirements.txt
Or install manually:

pip install streamlit tensorflow numpy Pillow beautifulsoup4 requests
```
###🚀 Run the app
streamlit run app.py

📄 requirements.txt

streamlit
tensorflow
numpy
Pillow
beautifulsoup4
requests
🧪 Sample Output

✅ Prediction: Neem Plant

📄 Summary:
Azadirachta indica (Neem) is a tree in the mahogany family native to the Indian subcontinent. 
It has widespread medicinal and agricultural uses.

🔗 Wikipedia: https://en.wikipedia.org/wiki/Neem
🎯 Future Enhancements

🔍 Add more plant species for better coverage
🧾 Multilingual summary support (Tamil, Hindi, etc.)
📦 Offline summary caching for repeated queries
🧠 Model ensembling for confidence boost
🌐 Integration with AYUSH, PubMed APIs
🛠️ Built With

TensorFlow
Keras
VGG16 Architecture
Streamlit
BeautifulSoup
Wikipedia
Healthline
📜 License

This project is licensed under the MIT License – feel free to use, adapt, and distribute with credit.

🙌 Acknowledgements

Keras for pre-trained VGG16 model
Public datasets of medicinal plants
Wikipedia and Healthline for live data
Open-source community for Streamlit and Python tools
