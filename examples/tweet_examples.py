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

}


# Enum
class TweetExamples(Enum):
    tweet_info = tweet_info_examples
    tweet_id = tweet_id_examples

