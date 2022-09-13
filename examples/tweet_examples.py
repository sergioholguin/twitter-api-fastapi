from enum import Enum

# Tweet Path Operation Examples
tweet_info_examples = {
    "example-1": {
        "summary": "First Example",
        "value": {
            "content": "Pedrotweet",
            "by": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
    },
    "example-2": {
        "summary": "Second Example",
        "value": {
            "content": "Island is the best story I've read so far",
            "by": "f097222b-ae18-4739-bf68-f6b57635849a"
        }
    },
    "example-3": {
        "summary": "Third Example",
        "value": {
            "content": "Sometimes I want to walk around the university",
            "by": "731b0e35-64ce-4de2-8746-47ac3fe9ee8b"
        }
    }
}

tweet_id_examples = {
    "example-1": {
        "summary": "First Example",
        "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    },
    "example-2": {
        "summary": "Second Example",
        "value": "6c69519b-12d7-4309-bca2-9685cd36413c",
    },
    "example-3": {
        "summary": "Third Example",
        "value": "4861aaca-d9cf-46e2-b347-d10ffdadd38f",
    }
}

tweet_update_examples = {
    "example-1": {
        "summary": "First Example",
        "value": {
            "content": "Lorem Ipsum adfadf Pedrotweet",
        }
    },
    "example-2": {
        "summary": "Second Example",
        "value": {
            "content": "TAMASHIIIIIIIII NO IRO WAAAAAAAAAA",
        }
    },
    "example-3": {
        "summary": "Third Example",
        "value": {
            "content": "I want to travel to other countries y'know.",
        }
    }
}


# Enum
class TweetExamples(Enum):
    tweet_info = tweet_info_examples
    tweet_id = tweet_id_examples
    tweet_updates = tweet_update_examples

