from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def semantic_score(self, resume_text: str, jd_text: str) -> float:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        return round(score * 100, 2)
