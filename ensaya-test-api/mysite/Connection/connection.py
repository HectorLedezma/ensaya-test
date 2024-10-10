import json
from bson import json_util
import pymysql.cursors
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
# Connect to the database

def connectMySQL():
    try:
        connection = pymysql.connect(
            host=os.getenv("MySQLhost"),
            user=os.getenv("MySQLuser"),
            password=os.getenv("MySQLpass"),
            database=os.getenv("MySQLbase"),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connection Successful")
        return connection
    except Exception as e:
        print("Connection Error:",str(e))


def connectMongoDB():
    try:
        client = MongoClient(os.getenv("MongoDBuri"))#server
        connection = client[os.getenv("MongoDBase")]#DB
        print("Connection Successful")
        return connection#"Connection Successful"
    except Exception as e:
        return {"error":e}

def getAllUser():
    connection = connectMySQL()
    #connection.begin()
    sql = "SELECT * FROM user;"
    print(sql)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchall()
            print("result:",result)
            return result
    except Exception as e:
        print("Request Error",e)
        return [{"Request Error":str(e)}]


def allDocs():
    connection = connectMongoDB()
    collection = connection[os.getenv("MongoDBcoll")]
    try:
        Doc = list(collection.find())
        docs_json = json.dumps(Doc, default=json_util.default)
        return docs_json
    except Exception as e:
        return e
"""

"""