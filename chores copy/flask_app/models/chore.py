from flask import Flask, render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login
from flask import flash




class Chore:
    db = "chores_db"
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.location = data['location']
        self.date = data['date']
        self.host_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.host = None



    #Create chore Models

    @classmethod
    def create_chore(cls, data):
        if not cls.validate_chore_data(data): return False
        query = """
            INSERT INTO chores
                (title, description, location, date, user_id)
            VALUES
                (%(title)s, %(description)s, %(location)s, %(date)s, %(user_id)s)
            ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_chores_by_user(cls, user_id): # I would call this get user by id with chores, and put it in the user model
        query = """
            SELECT * 
            FROM chores
            JOIN users 
            ON users.id = chores.user_id
            WHERE users.id = %(user_id)s
            ;"""
        data = {"user_id" :  user_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        print("get_all_chores_by_user data", results)
        chores = []
        for result in results: 
            chore_list = {
                "id": result['id'],
                "title": result['title'],
                "description": result['description'],
                "location": result['location'],
                "date": result['date'],
                "created_at": result['created_at'],# belongs to the chore
                "updated_at": result['updated_at'],# belongs to the chore, not the user
            }
            this_chore = Chore(result)
            this_chore.host = login.Login.instantiate_user(chore_list)
            chores.append(this_chore)
        return chores

    #read chore Models

    @classmethod
    def get_all_chore_w_hosts(cls):
        query = """
            SELECT * 
            FROM chores
            JOIN users
            ON  users.id = chores.user_id
            ;"""
        results = connectToMySQL(cls.db).query_db(query)
        chores = [] 
        for result in results:
            this_chore = cls(result)
            this_chore.host = login.Login.instantiate_user(result)
            chores.append(this_chore)
        return chores

    @classmethod
    def get_chore_by_id_w_host(cls, id):
        data = {'id' : id}
        query = """
            SELECT * 
            FROM chores
            JOIN users
            ON  users.id = chores.user_id
            WHERE chores.id = %(id)s
            ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        this_chore = cls(result[0])
        this_chore.host = login.Login.instantiate_user(result[0])
        return this_chore


    #update chore Models   

    @classmethod
    def update_chore(cls, data):
        if not cls.validate_chore_data(data): return False
        query = """
            UPDATE chores
            SET 
                title = %(title)s,
                description = %(description)s,
                location = %(location)s,
                date = %(date)s
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return True


    #delete chore Models

    @classmethod
    def delete_chore_by_id(cls,id):
        data = {'id' : id}
        query = """
            DELETE FROM chores
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return 


    #Validations

    @classmethod
    def validate_chore_data(cls,data):
        is_valid = True 
        if len(data['title']) < 3:
            flash('Title is required')
            is_valid = False 
        if len(data['description']) < 10:
            flash('Description shold be at least 10 characters.')
            is_valid = False
        if len(data['location']) == 0 :
            flash("Location is required.")
            is_valid = False
        if not data['date']:
            flash('A date is required')
            is_valid = False
        return is_valid


