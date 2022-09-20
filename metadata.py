
from controllers.tags import Tags


description = """
TwitterLike API that imitates original Twitter

You will be able to:

## Users

- **Authenticate and Sing Up**
- **Create, Read, Delete and Update users**

## Twitter

- **Create, Read, Delete and Update Tweets**
"""

APIMetadata = {
    "title": "TwitterLike",
    "description": description,
    "version": "3.0",
    "terms_of_service": "https://example.com/terms/",
    "contact": {
        "name": "Sergio_HC",
        "url": "https://example/contact/",
        "email": "sergiohc@example.com"
    },
    "license_info": {
        "name": "Example Apache 2.0",
        "url": "https://www.exampleapache.org/licenses/LICENSE-2.0.html",
    }
}


tags_metadata = [
    {
        "name": Tags.auth,
        "description": "Authentication. The **login** logic is also here."
    },
    {
        "name": Tags.users,
        "description": "Operations with _users_."
    },
    {
        "name": Tags.tweets,
        "description": "Operations with _tweets_."
    },
]
