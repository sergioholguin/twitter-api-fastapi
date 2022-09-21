
# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database Imports
from sql_app.database import Base

SQLALCHEMY_TEST_DATABASE_URL = 'mysql://root:password@localhost:3306/test_twitter_api'

mysql_engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine)

# Drop and Recreate Tables
Base.metadata.drop_all(bind=mysql_engine)
Base.metadata.create_all(bind=mysql_engine)


# Dependency Override
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


