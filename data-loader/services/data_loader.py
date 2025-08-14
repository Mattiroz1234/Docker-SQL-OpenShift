from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel

app = FastAPI()

MYSQL_USER = "root"
MYSQL_PASSWORD = "pwd"
MYSQL_HOST = "mysql"
MYSQL_PORT = 3306
MYSQL_DB = "testdb"

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)

class User(BaseModel):
    id: int
    first_name: str
    last_name: str

@app.get("/users")
def read_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM data"))
        users = [User(id=row.id, first_name=row.first_name, last_name=row.last_name) for row in result]
    return users
