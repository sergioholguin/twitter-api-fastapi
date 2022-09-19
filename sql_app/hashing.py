
# PassLib
from passlib.context import CryptContext

# Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Create Hashed password
def get_password_hash(password):
    hashed_password = pwd_context.hash(password)
    return hashed_password


# Verified password
def verify_password(plain_password: str, hashed_password: str):
    valid_credentials = pwd_context.verify(plain_password, hashed_password)
    return valid_credentials

