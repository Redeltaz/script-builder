from .crud_base import CRUDBase

class CRUDPackage(CRUDBase):
    pass

def package_serializer(n):
    return {
        "id": n["id"],
        "name": n["name"],
        "type": n["type"],
    }

package_crud = CRUDPackage(
    serializer=package_serializer,
    table="Package"
)