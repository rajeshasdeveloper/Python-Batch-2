import sqlite3
import os
from pathlib import Path

if "codegen.db" in os.listdir(os.getcwd()):
    os.remove("codegen.db")

users_table = '''
CREATE TABLE IF NOT EXISTS USERS (
    USERNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL UNIQUE ,
    PASSWORD TEXT NOT NULL,
    MOBILE TEXT
)
'''
conn = sqlite3.connect("codegen.db", check_same_thread=False)
cursor = conn.cursor()

def db_util(query:str, param:list=[]):
    try:
        cursor.execute(query, param)
        conn.commit()
    except Exception as err:
        raise err

db_util(users_table)




