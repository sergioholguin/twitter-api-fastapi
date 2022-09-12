from enum import Enum


# User Path Operation Examples
signup_examples = {
    "example-1": {
        "summary": "First Example",
        "value": {
            "first_name": "Pedro",
            "last_name": "SomeLastName",
            "email": "pedro@example.com",
            "password": "thisisthepedropassword",
            "country": "Peru",
            "birth_date": "2000-01-01",
            "creation_account_date": "2010-09-09"
        }
    },
    "example-2": {
        "summary": "Second Example",
        "value": {
            "first_name": "Sergio",
            "last_name": "SomeLastName",
            "email": "sergio@example.com",
            "password": "thisisthesergiopassword",
            "country": "Peru",
            "birth_date": "2003-01-01",
            "creation_account_date": "2013-09-09"
        }
    },
    "example-3": {
        "summary": "Third Example",
        "value": {
            "first_name": "Azucena",
            "last_name": "SomeLastName",
            "email": "azucena@example.com",
            "password": "thisistheazucenapassword",
            "country": "Peru",
            "birth_date": "2006-01-01",
            "creation_account_date": "2016-09-09"
        }
    }
}


id_examples = {
    "example-1": {
        "summary": "First Example",
        "value": "731b0e35-64ce-4de2-8746-47ac3fe9ee8b"
    },
    "example-2": {
        "summary": "Second Example",
        "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    },
    "example-3": {
        "summary": "Third Example",
        "value": "3fa85f64-5717-4562-b3fc-2c943f66afa3",
    }
}


# Enum
class UserExamples(Enum):
    user_info = signup_examples
    user_id = id_examples
