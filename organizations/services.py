from organizations.models import Organization, Member
from organizations.db import SessionLocal, create_dynamic_db


# This could be Better Organizaed using Reposirity Pattern
def create_organization(db, organization_name, email, password):
    dynamic_db_url = f"sqlite:///./{organization_name}.db"
    create_dynamic_db(dynamic_db_url)

    org = Organization(name=organization_name, db_url=dynamic_db_url)
    db.add(org)
    db.commit()
    db.refresh(org)

    member = Member(email=email, password=password, organization_id=org.id)
    db.add(member)
    db.commit()
    db.refresh(member)

    return org

def get_organization_by_name(db, name):
    return db.query(Organization).filter(Organization.name == name).first()
