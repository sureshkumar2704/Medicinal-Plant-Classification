# 🧠 Medicinal Plant Classifier & Identifier

This project leverages **deep learning (VGG16)** to classify medicinal plants from either **leaf** or **full plant** images. It features a web-based interface built using **Streamlit**, allowing users to upload an image and get predictions instantly. The predicted plant name is also linked to its corresponding **Wikipedia page** (or alternative sources like Healthline) for dynamic summarization.

---

## 🌿 Project Motivation

Identifying medicinal plants accurately is critical for health, agriculture, and biodiversity conservation. However, differentiating between species using visual features like leaves and whole plants can be challenging.

To solve this, a **VGG16-based CNN model** was fine-tuned to distinguish between different plant classes using both leaf and plant images, improving classification robustness in real-world scenarios.

---

## 📁 Dataset Structure

To support classification of both **leaf** and **plant** images for each species, the dataset was organized into:

combined_dataset/
├── train/
│ ├── tulsi_leaf/
│ ├── tulsi_plant/
│ ├── neem_leaf/
│ ├── neem_plant/
│ └── ...
├── test/
│ └── (same structure as train)
├── valid/
│ └── (same structure as train)



- `*_leaf` and `*_plant` folders help the model learn features from both image types.
- `train`, `test`, and `valid` ensure proper model generalization.

---

## 🧠 Model Details

- **Base Model**: `VGG16` (pretrained on ImageNet)
- **Modifications**:
  - Removed top layers
  - Added Flatten, Dense, Dropout, and Softmax layers
- **Input Size**: `(224, 224, 3)`
- **Number of Classes**: Based on total `leaf_` + `plant_` categories

---

## 🚀 Features

- 🌱 Upload a plant or leaf image
- 🤖 Real-time prediction using the fine-tuned VGG16 model
- 🔍 Auto-search for plant description from:
  - Wikipedia (first attempt)
  - Healthline or alternative links (fallback)
- ✅ Displays both **actual class** and **predicted class**
- 📝 Shows a **live summary** of the plant fetched dynamically

---

## 🖥️ Streamlit Web App (`app.py`)

- Loads the trained `.keras` model
- Predicts using uploaded image
- Uses `requests` + `BeautifulSoup` to fetch plant summary
- Displays:
  - Uploaded image
  - Predicted plant type
  - Wikipedia link
  - Summary (if available)

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/medicinal-plant-classifier.git
cd medicinal-plant-classifier

# Install dependencies
pip install -r requirements.txt
# or manually
pip install streamlit tensorflow numpy Pillow beautifulsoup4 requests

# Run the app
streamlit run app.py

🧪 Example Output

✅ Prediction: Tulsi Plant
📄 Summary: Tulsi (Ocimum tenuiflorum), also known as holy basil, is an aromatic perennial plant...
🔗 [Learn more on Wikipedia »](https://en.wikipedia.org/wiki/Tulsi)
🔍 Future Enhancements

Improve model accuracy with more data
Integrate medicinal usage info from research databases
Add multilingual support
Enable offline summary caching
🛠️ Built With

TensorFlow / Keras
VGG16 CNN Architecture
Streamlit
BeautifulSoup
Wikipedia / Healthline APIs
📜 License

This project is open-source and available under the MIT License.

🙌 Acknowledgements

Pretrained models from Keras
Publicly available plant datasets
Wikipedia, Healthline for content
