from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class UserCreateModel(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
