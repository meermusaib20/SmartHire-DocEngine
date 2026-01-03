# SmartHire Document Intelligence Engine

An AI-powered document intelligence backend for **SmartHire**, designed to extract structured information from unstructured resumes and match candidates against job descriptions using NLP, OCR, and machine learning techniques.

This project focuses on **real-world document processing challenges** such as noisy PDFs, OCR fallback, entity extraction, and explainable resume–JD matching.

---

## 🚀 Key Features

- Resume parsing (PDF / text)
- OCR fallback for scanned documents
- Entity extraction:
  - Name
  - Email
  - Phone number
- Skill extraction with normalization
- Resume vs Job Description matching
- Explainable skill match scoring
- Semantic similarity using TF-IDF
- REST API built with FastAPI
- Modular, production-style architecture

---

## 🧠 System Architecture

Client (Swagger / Frontend)
|
v
FastAPI (API Layer)
|
v
Resume Pipeline
├── Text Cleaning
├── Entity Extraction (spaCy)
├── Skill Extraction
├── Skill Matching
└── Semantic Similarity (TF-IDF)
|
v
Structured JSON Output


---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **API Framework:** FastAPI
- **OCR:** Tesseract OCR + pytesseract
- **PDF Parsing:** pdfplumber
- **NLP:** spaCy
- **ML:** scikit-learn (TF-IDF + cosine similarity)
- **Server:** Uvicorn

---

## 📂 Project Structure

SmartHire-DocEngine/
│
├── app/
│ ├── main.py
│ └── api/
│ └── routes.py
│
├── pipelines/
│ └── resume_pipeline.py
│
├── nlp/
│ ├── cleaner.py
│ ├── entity_extractor.py
│ └── skill_extractor.py
│
├── ocr/
│ ├── pdf_extractor.py
│ └── tesseract_engine.py
│
├── scoring/
│ ├── skill_matcher.py
│ └── resume_matcher.py
│
├── utils/
│ └── file_utils.py
│
├── tests/
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/meermusaib20/SmartHire-DocEngine.git
cd SmartHire-DocEngine

2️⃣ Create and activate virtual environment
python -m venv venv311
venv311\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install spaCy model
python -m spacy download en_core_web_sm

5️⃣ (Windows) Install Tesseract OCR
Download from: https://github.com/UB-Mannheim/tesseract/wiki
Install Tesseract OCR
The project explicitly sets the Tesseract binary path in code to avoid PATH issues.

6️⃣ Run the server
uvicorn app.main:app --reload

**🔎 API Endpoints**
Health Check
GET /health

**Analyze Resume**
POST /analyze-resume
Input: Resume file (PDF / text)
Output: Extracted entities and skills

**Match Resume with Job Description**
POST /match-resume
Input: Resume file + Job Description text
Output:
Extracted skills
Matched skills
Skill match score
Semantic similarity
Final weighted score

**Swagger UI available at:**
http://127.0.0.1:8000/docs

**📊 Scoring Logic (Explainable)**
Skill Match Score: Percentage of JD skills found in resume
Semantic Similarity: TF-IDF cosine similarity

Final Score:
Final Score = 0.6 × Skill Match + 0.4 × Semantic Similarity
```

This ensures interpretability, not black-box ranking.


🎓 Academic & Practical Relevance

This project demonstrates:
Handling of unstructured real-world data
OCR + NLP pipeline integration
Production-style backend architecture
Debugging of OS-level and Python dependencies
Explainable AI logic for recruitment systems

🔮 Future Improvements

Experience-based weighting (junior/senior roles)
Resume section detection
LLM-based reasoning for explanations
Dockerization for deployment
Frontend integration with SmartHire

👤 Author

Mir Musaib
B.Tech Computer Science & Engineering
Final Year Project – SmartHire

📜 License

This project is for academic and learning purposes.


---

## ✅ What to do now

1. Open `README.md` in your project  
2. Paste the content above  
3. Save  
4. Commit:
