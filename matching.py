from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_student_to_internships(student_text, internships):
    if not internships:
        return []

    texts = [student_text] + [intern.required_skills for intern in internships]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    student_skills_set = set(student_text.lower().split())

    results = []

    for i, score in enumerate(similarities[0]):
        internship = internships[i]
        internship_skills_set = set(internship.required_skills.lower().split())

        missing_skills = list(internship_skills_set - student_skills_set)

        results.append((internship, float(score), missing_skills))

    results.sort(key=lambda x: x[1], reverse=True)

    return results
