from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    email: str
    location: str
    description: str


class CompanyCreate(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    id: int

    class Config:
        from_attributes = True