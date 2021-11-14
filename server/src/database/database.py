from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_LOGIN = os.getenv("DATABASE_LOGIN")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

class Database:
    
    def __init__(self, uri, login, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(login, password))
        
    def close(self) -> None:
        self.driver.close()
        
    def get(self, serializer, request, selector):
        with self.driver.session() as session:
            response = session.read_transaction(request, selector)
            result = []
            if len(response) > 0:
                result = serializer(response[0]["n"])
        self.close()
        return result
        
    def get_multi(self, serializer, request):
        with self.driver.session() as session:
            response = session.read_transaction(request)
            result = [serializer(node["n"]) for node in response]
        self.close()
        return result
        
    def post(self, serializer, request, params):
        with self.driver.session() as session:
            response = session.write_transaction(request, params)
            result = serializer(response[0]["n"])
        self.close()
        return result
    
    def update(self, serializer, request, id, params):
        with self.driver.session() as session:
            response = session.write_transaction(request, id, params)
            result = []
            if len(response) > 0:
                result = serializer(response[0]["n"])
        self.close()
        return result
    
    def delete(self, serializer, request, id):
        with self.driver.session() as session:
            response = session.write_transaction(request, id)
            result = []
            if len(response) > 0:
                result = serializer(response[0]["n"])
        self.close()
        return result
        
db = Database(DATABASE_URL, DATABASE_LOGIN, DATABASE_PASSWORD)
    