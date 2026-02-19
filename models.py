from sqlalchemy import Column, Integer, String, Text
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    skills_text = Column(Text)
    cv_text = Column(Text)


class Internship(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    title = Column(String)
    description = Column(Text)
    required_skills = Column(Text)
