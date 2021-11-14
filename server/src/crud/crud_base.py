from ..database import db

class CRUDBase():
    """
    Base crud class, all crud class need to inherit from this one,
    this is an abstract class !!!!!!!!!!!!!!!!!!!!!!!!!
    """    
    def __init__(self, serializer: dict, table: str) -> None:
        self.serializer = serializer
        self.table = table
        
    def read(self, id):
        response = db.get(serializer=self.serializer, request=self.__read_request, selector=id)
        return response
        
    def read_all(self):
        response = db.get_multi(serializer=self.serializer, request=self.__read_all_request)
        return response
    
    def create(self, params):
        response = db.post(serializer=self.serializer, request=self.__create_request, params=params)
        return response
    
    def update(self, id, params):
        response = db.update(serializer=self.serializer, request=self.__update_request, id=id, params=params)
        return response
    
    def delete(self, id):
        response = db.delete(serializer=self.serializer, request=self.__delete_request, id=id)
        return response
    
    def __read_request(self, tx, id):
        result = list(tx.run("MATCH (n:{}) WHERE n.id = $id RETURN n LIMIT 1".format(self.table), id=int(id)))
        return result
        
    def __read_all_request(self, tx):
        result = list(tx.run("MATCH (n:{}) RETURN n".format(self.table)))
        return result
    
    def __create_request(self, tx, params):
        result = list(tx.run("CREATE (n:{}) SET n = $params, n.id = id(n) RETURN n".format(self.table), params=params))
        return result
    
    def __update_request(self, tx, id, params):
        result = list(tx.run("MATCH (n:{}) WHERE n.id = $id SET n += $params RETURN n".format(self.table), id=int(id), params=params))
        return result
    
    def __delete_request(self, tx, id):
        result = list(tx.run("MATCH (n:{}) WHERE n.id = $id DELETE n RETURN n".format(self.table), id=int(id)))
        return result