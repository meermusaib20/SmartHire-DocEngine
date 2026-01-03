from fastapi import APIRouter, UploadFile, File, Form
from pipelines.resume_pipeline import ResumePipeline
from utils.file_utils import extract_text_from_upload

router = APIRouter()
pipeline = ResumePipeline()


@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_upload(content, file.filename)

    result = pipeline.run(text)
    return result



@router.post("/match-resume")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_bytes = await resume.read()
    resume_text = extract_text_from_upload(resume_bytes, resume.filename)

    result = pipeline.run(resume_text, job_description)
    return result
