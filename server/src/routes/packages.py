from fastapi import APIRouter, HTTPException
from typing import List

from ..crud import package_crud
from ..schemas import Package, PackageCreate, PackageUpdate

package_router = APIRouter()

@package_router.get("/", response_model=List[Package])
def get_packages():
    """
    get all packages
    """
    packages_db = package_crud.read_all()
    
    return packages_db

@package_router.get("/{package_id}", response_model=Package)
def get_package(package_id: str):
    """
    get package by id
    """
    package_db = package_crud.read(package_id)
    if not package_db:
        raise HTTPException(status_code=404, detail="Package not found")
    
    return package_db

@package_router.post("/", response_model=Package)
def create_package(request_body: PackageCreate):
    """
    create package
    """
    package_params = dict(request_body)
    package_params["is_superpackage"] = False
    package_params["is_admin"] = False
    
    package_db = package_crud.create(package_params)
    
    return package_db

@package_router.put("/{package_id}", response_model=Package)
def update_package(
    package_id: str,
    request_body: PackageUpdate
):
    """
    update package
    """
    package_params = dict(request_body)
    
    package_db = package_crud.read(package_id)
    if not package_db:
        raise HTTPException(status_code=404, detail="Package not found")
    
    package_db = package_crud.update(package_id, package_params)
    
    return package_db

@package_router.delete("/{package_id}")
def delete_package(package_id: str):
    """
    delete package
    """
    package_db = package_crud.read(package_id)
    if not package_db:
        raise HTTPException(status_code=404, detail="Package not found")
    
    package_db = package_crud.delete(package_id)
    
    return package_db