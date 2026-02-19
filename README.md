# Internship Matcher API

This is a backend project I built to practice building a real-world API with authentication, databases, and basic recommendation logic.

The idea is simple: a student registers, logs in, and gets internship recommendations based on how similar their skills are to the required skills of internships stored in the system.

---

## Why I Built This

As a second-year Information Systems and Technologies student, I wanted to move beyond small academic projects and build something that includes:

- Authentication
- Database design
- API development
- Basic NLP-based similarity matching
- Deployment to the cloud

This project helped me understand how backend systems are structured and how different layers (auth, database, logic) interact with each other.

---

## What It Does

- Students can register and log in (passwords are hashed).
- Login returns a JWT token.
- Protected endpoints require authentication.
- The system compares student skills with internship requirements.
- Internships are ranked using TF-IDF and cosine similarity.
- Missing skills are also returned.

Example response:

```json
[
  {
    "company": "Google",
    "title": "Backend Intern",
    "match_percentage": 72.41,
    "missing_skills": ["docker", "aws"]
  }
]
