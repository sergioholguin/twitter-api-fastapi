
# PassLib
from passlib.context import CryptContext

# Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hashing password
def get_password_hash(password):
    hashed_password = pwd_context.hash(password)
    return hashed_password
