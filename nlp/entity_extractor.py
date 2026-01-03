import re
import spacy

nlp = spacy.load("en_core_web_sm")

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
PHONE_REGEX = r'(\+?\d{1,3}[\s\-]?)?\d{10}'

class ResumeEntityExtractor:
    def extract_email(self, text: str):
        matches = re.findall(EMAIL_REGEX, text)
        return matches[0] if matches else None

    def extract_phone(self, text: str):
        matches = re.findall(PHONE_REGEX, text)
        if matches:
            # flatten tuple result
            phone = matches[0]
            return ''.join(phone) if isinstance(phone, tuple) else phone
        return None

    def extract_name(self, text: str):
        """
        Strategy:
        - Look at first ~5 lines (names are usually at top)
        - Use spaCy PERSON entity
        """
        lines = text.split("\n")[:5]
        joined = " ".join(lines)

        doc = nlp(joined)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return None

    def extract(self, text: str) -> dict:
        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text)
        }
