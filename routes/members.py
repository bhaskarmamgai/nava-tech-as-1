from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from organizations.schema import MemberLogin
from organizations.db import SessionLocal
from organizations.auth import create_jwt_token
from organizations.models import Member

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def member_admin(payload: MemberLogin, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.email == payload.email).first()
    if not member or member.password != payload.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt_token({"sub": member.email})
    return {"access_token": token, "token_type": "bearer"}
