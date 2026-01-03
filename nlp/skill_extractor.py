class SkillExtractor:
    def __init__(self):
        self.skill_aliases = {
            "python": ["python"],
            "machine learning": ["machine learning", "ml"],
            "deep learning": ["deep learning", "dl"],
            "nlp": ["nlp", "natural language processing"],
            "sql": ["sql"],
            "tensorflow": ["tensorflow", "tf"],
            "pytorch": ["pytorch", "torch"],
            "fastapi": ["fastapi"],
            "docker": ["docker"],
            "aws": ["aws", "amazon web services"]
        }

    def extract(self, text: str):
        text = text.lower()
        found = []

        for canonical, aliases in self.skill_aliases.items():
            for alias in aliases:
                if alias in text:
                    found.append(canonical)
                    break

        return list(set(found))


class JDExtractor(SkillExtractor):
    pass
