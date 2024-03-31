from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

class Ninja:
    _DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_ninja(cls, data):
        query = """
                INSERT INTO ninjas
                (dojo_id, first_name, last_name, age, created_at, updated_at)
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s,%(age)s, NOW(), NOW());
                """
        results = connectToMySQL(cls._DB).query_db(query, data)
        return results