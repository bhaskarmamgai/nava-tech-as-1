from pydantic import BaseModel

class OrganizationCreate(BaseModel):
    organization_name: str
    email: str
    password: str

class MemberLogin(BaseModel):
    email: str
    password: str
