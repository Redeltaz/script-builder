from .crud_base import CRUDBase

class CRUDUser(CRUDBase):
    pass

def user_serializer(n):
    return {
        "id": n["id"],
        "username": n["username"],
        "email": n["email"],
        "password": n["password"],
        "is_superuser": n["is_superuser"],
        "is_admin": n["is_admin"],
    }

user_crud = CRUDUser(
    serializer=user_serializer,
    table="User"
)