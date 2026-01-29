import re


def analyze_resume_against_job_description(resume_text: str, job_description: str):
    jd_keywords = set(re.findall(r"\b[a-zA-Z]{3,}\b", job_description.lower()))
    resume_keywords = set(re.findall(r"\b[a-zA-Z]{3,}\b", resume_text.lower()))

    matched = sorted(jd_keywords.intersection(resume_keywords))
    missing = sorted(jd_keywords.difference(resume_keywords))

    coverage_ratio = len(matched) / len(jd_keywords) if jd_keywords else 0
    score = int(round(coverage_ratio * 100))

    return {
        "ats_score": score,
        "total_keywords": len(jd_keywords),
        "matched_keywords": matched[:20],
        "missing_keywords": missing[:20],
        "coverage_ratio": round(coverage_ratio, 3),
        "suggestions": [
            "Add missing keywords from the job description",
            "Use stronger action verbs",
            "Include measurable achievements",
        ],
    }
