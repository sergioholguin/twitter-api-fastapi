
# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_TEST_DATABASE_URL = 'mysql://root:password@localhost:3306/test_twitter_api'

mysql_test_engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=mysql_test_engine)


# Dependency Override
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
