
# Libraries
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

# Token Variables
SECRET_KEY = "d519c254149acf907a0fa554535efd82562ef6cd0d2dc4011cc6875c8238336b"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    # Encoding
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
