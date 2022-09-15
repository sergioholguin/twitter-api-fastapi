
from sql_app.database import SessionLocal


# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
