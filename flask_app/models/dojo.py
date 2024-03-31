from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:
    _DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(Dojo._DB).query_db(query)
        dojos = []
        for each_dojo in results:
            dojo = Dojo(each_dojo)
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = """
                INSERT INTO dojos
                (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());
                """
        results = connectToMySQL(cls._DB).query_db(query, data)
    
    @classmethod
    def get_one_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': dojo_id}
        results = connectToMySQL(Dojo._DB).query_db(query, data)
        pprint(results)
        return cls(results[0])

    @classmethod
    def get_dojo_ninjas(cls, data):
        dojo_id={
            "id": data
        }
        query = "SELECT * FROM ninjas WHERE dojo_id= %(id)s;"
        results = connectToMySQL(cls._DB).query_db(query, dojo_id)
        ninjas=[]
        for each_ninja in results:
            if each_ninja["id"] is not None:

                row = {
                    "id": each_ninja["id"],
                    "first_name": each_ninja["first_name"],
                    "last_name": each_ninja["last_name"],
                    "age": each_ninja["age"],
                    "created_at": each_ninja["created_at"],
                    "updated_at": each_ninja["updated_at"],
                }
                ninjas.append(Ninja(row))
        return ninjas