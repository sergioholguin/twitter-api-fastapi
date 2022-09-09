from enum import Enum


# Examples
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

post_tweet_examples = {

}


# Enum
class Examples(Enum):
    singup = signup_examples
