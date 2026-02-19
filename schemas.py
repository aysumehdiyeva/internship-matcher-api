from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    skills_text: str
    cv_text: str


class InternshipCreate(BaseModel):
    company: str
    title: str
    description: str
    required_skills: str

class StudentRegister(BaseModel):
    name: str
    email: str
    password: str
    skills_text: str
    cv_text: str


class StudentLogin(BaseModel):
    email: str
    password: str
