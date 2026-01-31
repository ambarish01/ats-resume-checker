# ATS Resume Checker (FastAPI)

A backend application built with **FastAPI** that analyzes a resume PDF against a job description and returns an **ATS-style score**, along with matched and missing keywords.

This project demonstrates real-world backend development skills such as API design, file handling, text processing, and clean project structure.

---

## 🚀 Features

- Upload resume in **PDF format**
- Compare resume content with a **job description**
- Generate an **ATS-style score (0–100)**
- Identify **matched keywords**
- Identify **missing keywords**
- Simple and interactive **Swagger UI** for testing
- Health check endpoint for monitoring

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **pdfplumber**
- **Starlette**

---

## 📂 Project Structure

```bash

ats-resume-checker/
│
├── main.py # FastAPI application and API routes
├── ats_analyzer.py # ATS scoring and keyword analysis logic
├── pdf_parser.py # PDF text extraction logic
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md

```


---

## ⚙️ How It Works

1. The user uploads a resume PDF.
2. The PDF is parsed and converted into plain text.
3. Keywords are extracted from the job description.
4. Resume text is compared against job description keywords.
5. An ATS score is calculated based on keyword coverage.
6. The API returns structured JSON results.

---

## ▶️ Running the Project Locally

### 1️⃣ Install dependencies

python -m pip install -r requirements.txt



### 2️⃣ Start the FastAPI server

python -m uvicorn main:app --reload


### 3️⃣ Open Swagger UI



http://127.0.0.1:8000/docs
```bash


🔌 API Endpoints
Health Check

GET /health

Response:
{
  "status": "ok"
}

Resume Analysis
POST /analyze

Inputs:

resume_file (PDF file)
job_description (Text)

Response (example):
{
  "ats_score": 72,
  "total_keywords": 18,
  "matched_keywords": ["python", "fastapi", "api"],
  "missing_keywords": ["docker", "cloud", "sql"],
  "coverage_ratio": 0.4,
  "suggestions": [
    "Add missing keywords from the job description",
    "Use stronger action verbs",
    "Include measurable achievements"
  ]
}

```
## 🎯 Use Cases

- **Students optimizing resumes for job applications**

- **Job seekers checking ATS compatibility**

- **Recruiters performing quick resume screening**

- **Backend API reference project**



## 🔮 Future Improvements

- **AI-based semantic resume analysis**

- **Skill weighting and role-based scoring**

- **Resume improvement suggestions**

- **Frontend UI (React / Next.js)**

- **Authentication and user history**

- **Deployment with Docker**

## 👨‍💻 Author

Ambarish S A
Computer Science Engineer | Automation & AI Enthusiast

## 📜 License

This project is licensed under the MIT License.
