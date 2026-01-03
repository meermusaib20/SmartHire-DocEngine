from pipelines.resume_pipeline import ResumePipeline

resume = """
John Doe
Machine Learning Engineer
Email: johndoe@gmail.com
Phone: +91 9876543210

Skills: Python, Machine Learning, NLP, FastAPI
"""

jd = """
Looking for a Machine Learning Engineer with experience in
Python, NLP, Deep Learning, and FastAPI.
"""

pipeline = ResumePipeline()
result = pipeline.run(resume, jd)

print(result)
