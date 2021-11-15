from pydantic import BaseModel

class Package(BaseModel):
    id: int
    name: str
    
class PackageCreate(BaseModel):
    name: str
    
class PackageUpdate(BaseModel):
    name: str