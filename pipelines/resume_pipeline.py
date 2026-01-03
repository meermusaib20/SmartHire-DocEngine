from nlp.cleaner import TextCleaner
from nlp.entity_extractor import ResumeEntityExtractor
from nlp.skill_extractor import SkillExtractor, JDExtractor
from scoring.skill_matcher import SkillMatcher
from scoring.resume_matcher import ResumeMatcher

class ResumePipeline:
    def __init__(self):
        self.cleaner = TextCleaner()
        self.entity_extractor = ResumeEntityExtractor()
        self.skill_extractor = SkillExtractor()
        self.skill_matcher = SkillMatcher()
        self.semantic_matcher = ResumeMatcher()

    def run(self, resume_text: str, jd_text: str = None) -> dict:
        clean_resume = self.cleaner.clean(resume_text)

        entities = self.entity_extractor.extract(clean_resume)
        resume_skills = self.skill_extractor.extract(clean_resume)

        result = {
            "entities": entities,
            "resume_skills": resume_skills,
        }

        if jd_text:
            clean_jd = self.cleaner.clean(jd_text)

            jd_extractor = JDExtractor(self.skill_extractor.skills_db)
            jd_skills = jd_extractor.extract(clean_jd)

            skill_score, matched_skills = self.skill_matcher.score(
                resume_skills, jd_skills
            )

            semantic_score = self.semantic_matcher.semantic_score(
                clean_resume, clean_jd
            )

            final_score = round(
                (0.6 * skill_score) + (0.4 * semantic_score), 2
            )

            result.update({
                "jd_skills": jd_skills,
                "matched_skills": matched_skills,
                "skill_match_score": skill_score,
                "semantic_similarity": semantic_score,
                "final_score": final_score
            })

        return result
