from .crud_base import CRUDBase
from ..database import db

class CRUDUser(CRUDBase):
    def read_by_email(self, email):
        response = db.get(serializer=self.serializer, request=self.__read_by_email_request, selector=email)
        return response
    
    def __read_by_email_request(self, tx, email):
        result = list(tx.run("MATCH (n:{}) WHERE n.email = $email RETURN n LIMIT 1".format(self.table), email=email))
        return result

def user_serializer(n):
    return {
        "id": n["id"],
        "username": n["username"],
        "email": n["email"],
        "password": n["password"],
        "is_superuser": n["is_superuser"],
        "is_admin": n["is_admin"],
        "creation_date": n["creation_date"],
        "update_date": n["update_date"],
    }

user_crud = CRUDUser(
    serializer=user_serializer,
    table="User"
)