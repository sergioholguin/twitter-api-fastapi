
from sql_app.database import SessionLocal


# DB-Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



