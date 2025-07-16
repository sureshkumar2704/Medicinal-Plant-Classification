# 🧠 Medicinal Plant Classifier & Identifier

This project uses a **VGG16-based Convolutional Neural Network (CNN)** to classify medicinal plants from images of either **leaves** or **entire plants**. It features a **Streamlit-powered web app** that predicts the plant type and dynamically fetches a summary from **Wikipedia** or **Healthline**.

---

## 🌿 Motivation

Medicinal plants are vital in herbal medicine, agriculture, and biodiversity. However, accurate identification from images is often difficult due to variations in shape, lighting, and perspective. This project aims to solve that problem using deep learning.

---

## 🧠 Model Architecture

- **Base Model**: Pre-trained `VGG16` (from Keras, trained on ImageNet)
- **Modifications**:
  - Removed top classification layers
  - Added `Flatten`, `Dense`, `Dropout`, and final `Softmax` layers
- **Image Input Size**: 224 × 224 × 3
- **Final Layer**: Number of output classes = Number of unique folders in dataset (leaf & plant variants)

---

## 🗂️ Dataset Structure

The dataset is custom-organized under `combined_dataset/` into three subsets: `train/`, `test/`, and `valid/`, each having subfolders for every class.

combined_dataset/
├── train/
│ ├── tulsi_leaf/
│ ├── tulsi_plant/
│ ├── neem_leaf/
│ ├── neem_plant/
│ └── ... more classes
├── test/
│ └── same structure as train/
├── valid/
│ └── same structure as train/


- Each subfolder contains images of a specific class (either leaf or plant).
- Folders are named like `plantname_leaf` and `plantname_plant` to differentiate.
- Helps the model generalize better by learning from both parts of the plant.

---

## 🚀 Features

- 📤 Upload an image of a **leaf** or **whole plant**
- 🔍 Real-time prediction using a fine-tuned VGG16 model
- 📑 Automatically fetch plant description from:
  - Wikipedia (preferred)
  - Healthline (fallback if Wikipedia fails)
- 🧾 Displays:
  - Predicted class (e.g., "Neem Plant")
  - Actual internal class label
  - Dynamic summary
  - External knowledge links

---

## 🖼️ Web App (`app.py`)

### 🔧 Core Functionality:
- Loads your `medicinal_model.keras` model
- Preprocesses and predicts image class using TensorFlow
- Uses `requests` and `BeautifulSoup` to fetch description from Wikipedia
- Provides fallback search using Healthline

### 📋 Example Output:
✅ Predicted: Tulsi Leaf
🔍 Actual Class: tulsi_leaf

📘 Summary:
Tulsi (Ocimum tenuiflorum), also known as holy basil, is an aromatic perennial plant...

🌐 Learn more on Wikipedia »


---

## 🔧 Installation & Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/sureshkumar2704/Medicinal-Plant-Classification.git
cd Medicinal-Plant-Classification
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Launch the App
``` streamlit run app.py
```
---
##🛠️ Built With

TensorFlow
VGG16
Streamlit
BeautifulSoup4
Wikipedia 
---
##🚧 Future Work

Enhance model with more diverse plant images
Add multilingual description generation
Enable offline summary caching
Add image enhancement and correction features

---

##📜 License

This project is open-source under the MIT License.

---
numpy==1.24.3
Pillow==9.5.0
requests==2.31.0
beautifulsoup4==4.12.3
