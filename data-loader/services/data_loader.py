from fastapi import FastAPI, HTTPException
import mysql.connector
import os

app = FastAPI()


DB_HOST = "mysql"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = os.getenv("MYSQL_ROOT_PASSWORD", "pwd")
DB_NAME = 'testdb'


def get_conn():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        connection_timeout=8
    )

@app.get("/users")
def get_users():
    try:
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, first_name, last_name FROM data")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
