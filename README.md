# 🧩 SYNTHIA – AI-Based Synthetic Dataset Generator

SYNTHIA is a full-stack AI application that generates **auto-labeled synthetic image datasets** from a simple text prompt.  
It combines React.js (frontend), **Node.js + Express (backend)**, and a **Python ML pipeline** for image generation and annotation.

![image alt](https://github.com/annastudent2003/Synthia---AI-Powered-Image-Dataset-Generation/blob/00ab0837691551063042fba5235946101f44115e/images/Screenshot%202025-10-23%20234501.png)

## 🚀 Features
- 🎯 Enter a **text prompt** (e.g., “cats in the park”)  
- 🧠 Backend runs a **Python ML pipeline** (`annotate_pipeline.py`)  
- 🖼️ Generates multiple synthetic images and auto-labels them  
- 📦 Zips all labeled images into a ready-to-download dataset  
- 💾 Frontend shows the first 10 preview images and allows **“Download All”** 


## 🧱 Project Structure
SYNTHIA/
![image alt](https://github.com/annastudent2003/Synthia---AI-Powered-Image-Dataset-Generation/blob/f1bba68851d0647890430e81e7998ccc2aa1b7f5/images/a16eb651-1447-4bc3-86b9-fa81159b3c37.png)



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

### 🖥️ 3. Backend Setup (Node.js + Express)
```bash
cd ../backend
npm install express cors archiver
```
Then run
```bash
node server.js
```

### 🧠 4. Python ML Setup
.........
...........

### 🔄 End-to-End Flow

- Frontend (React) – user enters a prompt → sends POST to /generate
- Backend (Node) – receives prompt → runs Python (annotate_pipeline.py)
- Python ML – generates + labels dataset → saves to backend/generated/dataset_output
- Backend – zips dataset → returns /downloads/dataset.zip
- Frontend – displays top 10 images and enables Download All
