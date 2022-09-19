
# Libraries
from fastapi import status, HTTPException
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError

# Model
from models import TokenData

# Token Variables
SECRET_KEY = "d519c254149acf907a0fa554535efd82562ef6cd0d2dc4011cc6875c8238336b"
ALGORITHM = "HS256"

# Credentials_Exception
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# Access Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    # Encoding
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Verify Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email)
        return token_data

    except JWTError:
        raise credentials_exception
