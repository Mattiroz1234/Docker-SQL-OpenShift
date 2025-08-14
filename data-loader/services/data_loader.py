from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel

app = FastAPI(title="FastAPI + MySQL")

MYSQL_USER = "root"
MYSQL_PASSWORD = "pwd"
MYSQL_HOST = "mysql"
MYSQL_PORT = 3306
MYSQL_DB = "testdb"

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users")
def read_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, name, email FROM users"))
        users = [User(id=row.id, name=row.name, email=row.email) for row in result]
    return users
