from pydantic import BaseModel

class Package(BaseModel):
    id: int
    name: str
    type: str
    
class PackageCreate(BaseModel):
    name: str
    type: str
    
class PackageUpdate(BaseModel):
    name: str
    type: str