from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from matching import match_student_to_internships
import models
import schemas
import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Internship Matcher API with Database 🚀"}


# CREATE STUDENT
@app.post("/register/")
def register(student: schemas.StudentRegister, db: Session = Depends(get_db)):
    hashed_pw = auth.hash_password(student.password)

    new_student = models.Student(
        name=student.name,
        email=student.email,
        hashed_password=hashed_pw,
        skills_text=student.skills_text,
        cv_text=student.cv_text
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "User registered successfully"}

from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.Student).filter(models.Student.email == form_data.username).first()

    if not db_user:
        return {"error": "Invalid email"}

    if not auth.verify_password(form_data.password, db_user.hashed_password):
        return {"error": "Invalid password"}

    access_token = auth.create_access_token(
        data={"sub": db_user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}


# LIST STUDENTS
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# CREATE INTERNSHIP
@app.post("/internships/")
def create_internship(internship: schemas.InternshipCreate, db: Session = Depends(get_db)):
    new_internship = models.Internship(**internship.dict())
    db.add(new_internship)
    db.commit()
    db.refresh(new_internship)
    return new_internship



# LIST INTERNSHIPS
@app.get("/internships/")
def get_internships(db: Session = Depends(get_db)):
    return db.query(models.Internship).all()

# MATCH STUDENT TO INTERNSHIPS
from fastapi import Depends

@app.get("/match/")
def match(current_user: models.Student = Depends(auth.get_current_user),
          db: Session = Depends(get_db)):

    internships = db.query(models.Internship).all()

    matches = match_student_to_internships(current_user.skills_text, internships)

    return [
        {
            "company": intern.company,
            "title": intern.title,
            "match_percentage": round(score * 100, 2),
            "missing_skills": missing_skills
        }
        for intern, score, missing_skills in matches
    ]



    
