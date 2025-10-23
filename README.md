# 🧩 SYNTHIA – AI-Based Synthetic Dataset Generator

SYNTHIA is a full-stack AI application that generates **auto-labeled synthetic image datasets** from a simple text prompt.  
It combines React.js (frontend), **Node.js + Express (backend)**, and a **Python ML pipeline** for image generation and annotation.



## 🚀 Features
- 🎯 Enter a **text prompt** (e.g., “cats in the park”)  
- 🧠 Backend runs a **Python ML pipeline** (`annotate_pipeline.py`)  
- 🖼️ Generates multiple synthetic images and auto-labels them  
- 📦 Zips all labeled images into a ready-to-download dataset  
- 💾 Frontend shows the first 10 preview images and allows **“Download All”** 


## 🧱 Project Structure
SYNTHIA/
├── frontend/                  ← React.js UI
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   └── Results.jsx
│   │   ├── components/
│   │   │   ├── ImageGrid.jsx
│   │   │   └── FooterButtons.jsx
│   │   ├── assets/
│   │   │   └── bg-video.mp4
│   │   ├── App.js
│   │   └── App.css
│   └── package.json
│
├── backend/                   ← Node.js + Express
│   ├── server.js
│   ├── routes/
│   │   └── generate.js
│   ├── generated/             ← Output (images + dataset.zip)
│   ├── package.json
│   │
│   └── python/
│       ├── image_generation/  ← (for later)
│       │   └── generate_images.py
│       └── auto_label/
│           ├── annotate_pipeline.py
│           ├── export_coco.py
│           ├── extract_boxes.py
│           ├── run_midas.py
│           ├── run_sam.py
│           └── utils.py



## ⚙️ Installation & Setup

### 🧩 1. Clone the Repository
```bash
git clone https://github.com/your-username/synthia.git
cd synthia
```

### 💻 2. Frontend Setup (React.js)
```bash
cd frontend
npm install
npm start
```


