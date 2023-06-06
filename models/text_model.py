import mysql.connector
import json
from flask import render_template, redirect, url_for, make_response, request, jsonify
from datetime import datetime, date, time, timedelta
import jwt
from functools import wraps
# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

class text_model():
    def __init__(self):
        self.id = 0
        self.total_id = []
        self.secratekey = "asdflkjhmnbvzxcpqowieuryt"
        # connection between mysql and python
        try:
            self.con = mysql.connector.connect(
                user = 'Prince Malani',
                password = 'Hetu@0617',
                database = 'zigy'
                )
            # cursor object
            self.con.autocommit = True
            self.cursor = self.con.cursor(dictionary=True)
            print('Done-Connection')
        except Exception as e:
            print(e)
    
    def data_return(self):
        query = "SELECT * FROM zigy.textdata;"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
    
    def insert_models(self, text_data):
        query = f"INSERT INTO zigy.textdata (Text, CheckBox) VALUES ('{text_data}', '1');"
        self.cursor.execute(query)
        return True
    
    def find_data_models(self, id):
        
        qu = f"select id from zigy.textdata;"
        self.cursor.execute(qu)
        id_list = self.cursor.fetchall()
        la = [row['id'] for row in id_list] 
        if id in la:
            query = f"UPDATE zigy.textdata SET CheckBox = '0' WHERE (id = '{id}');"
            self.cursor.execute(query)
            return True
        else:
            return False