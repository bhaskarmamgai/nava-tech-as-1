from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from organizations.schema import OrganizationCreate
from organizations.db import SessionLocal
from organizations.services import create_organization, get_organization_by_name

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This Route Should Not Be REST Compliance. Doing since its an requirement by Assignment
@router.post("/create")
def create_org(payload: OrganizationCreate, db: Session = Depends(get_db)):
    return create_organization(db, payload.organization_name, payload.email, payload.password)

# This Route Should Not Be REST Compliance. Doing since its an requirement by Assignment
@router.get("/get")
def get_org(name: str, db: Session = Depends(get_db)):
    org = get_organization_by_name(db, name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org
