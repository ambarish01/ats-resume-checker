from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_400_BAD_REQUEST

from pdf_parser import extract_text_from_pdf
from ats_analyzer import analyze_resume_against_job_description

app = FastAPI(
    title="ATS Resume Checker",
    version="0.1.0",
    description="FastAPI backend to analyze resumes against job descriptions",
)

# CORS (safe for local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    if resume_file.content_type not in ("application/pdf", "application/x-pdf"):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported",
        )

    pdf_bytes = await resume_file.read()
    resume_text = extract_text_from_pdf(pdf_bytes)

    result = analyze_resume_against_job_description(
        resume_text=resume_text,
        job_description=job_description,
    )

    return result
