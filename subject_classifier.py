def infer_subject(text: str) -> str:
    text = text.lower()

    rules = {
        "Biology": ["photosynthesis", "cell", "organism", "enzyme", "dna", "genetics"],
        "Physics": ["force", "acceleration", "velocity", "newton", "gravity", "energy"],
        "Chemistry": ["atom", "molecule", "reaction", "acid", "base", "compound"],
        "Mathematics": ["equation", "algebra", "geometry", "calculus", "theorem"],
        "History": ["war", "revolution", "king", "empire", "battle"],
        "Geography": ["continent", "ocean", "mountain", "river", "climate"],
    }

    for subject, keywords in rules.items():
        if any(keyword in text for keyword in keywords):
            return subject

    return "General"