
# Libraries
import pytest
from uuid import UUID
from datetime import date
from fastapi import status
from .conftest import client

# Models
from models import Tweet


# Show tweets Tests
@pytest.mark.show
@pytest.mark.tweet
def test_show_all_tweets():
    response = client.get('/')
    response_info = response.json()

    assert response.status_code == status.HTTP_200_OK

    # Verify if all response are tweets
    for tweet_dict_info in response_info:
        Tweet(**tweet_dict_info)


@pytest.mark.show
@pytest.mark.tweet
def test_show_my_tweets(set_up_tweets):
    for user in set_up_tweets.values():  # user_1 and user_2
        user_info = user['user_info']
        header = user['header']

        response = client.get('/tweets/me', headers=header)
        response_info = response.json()

        assert response.status_code == status.HTTP_200_OK

        # Verify if all tweets are from the defined user
        for tweet_dict_info in response_info:
            tweet_info = Tweet(**tweet_dict_info)
            assert str(tweet_info.user_id) == user_info.user_id


@pytest.mark.show
@pytest.mark.tweet
def test_show_tweet_by_id(set_up_tweets):
    header = set_up_tweets['user_1']['header']

    for user in set_up_tweets.values():  # user_1 and user_2

        for tweet_number in range(1, 3):  # tweet_1 and tweet_2
            tweet = user[f'tweet_{tweet_number}']
            tweet_id = tweet["tweet_id"]
            response = client.get(f'/tweets/{tweet_id}', headers=header)
            response_info = response.json()

            assert response.status_code == status.HTTP_200_OK

            # Verify if the responses is the tweet
            assert response_info == tweet


@pytest.mark.show
@pytest.mark.tweet
def test_show_tweet_by_id_failed(set_up_tweets):
    header = set_up_tweets['user_1']['header']

    tweet_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f'/tweets/{tweet_id}', headers=header)
    response_info = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_info['detail'] == "Tweet not found!"


@pytest.mark.create
@pytest.mark.tweet
def test_post_tweet(set_up_tweets):
    user_info = set_up_tweets['user_1']['user_info']
    header = set_up_tweets['user_1']['header']

    data_to_send = {"content": "Some tweet to test posting."}

    response = client.post('/post', json=data_to_send, headers=header)
    response_info = response.json()

    tweet_id = response_info['tweet_id']

    expected_response = {
        "tweet_id": tweet_id,
        "content": data_to_send["content"],
        "created_at": str(date.today()),
        "updated_at": str(date.today()),
        "user_id": user_info.user_id
    }

    assert response.status_code == status.HTTP_201_CREATED
    assert type(UUID(tweet_id)) == UUID
    assert response_info == expected_response


@pytest.mark.delete
@pytest.mark.tweet
def test_delete_tweet_failed(set_up_tweets):
    header = set_up_tweets['user_1']['header']

    tweet_id = "00000000-0000-0000-0000-000000000000"
    response = client.delete(f'/tweets/{tweet_id}/delete', headers=header)
    response_info = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_info["detail"] == "Tweet doesn't exist!"


@pytest.mark.delete
@pytest.mark.tweet
def test_delete_tweet(set_up_tweets):
    user = set_up_tweets['user_1']
    user_info = user['user_info']
    header = user['header']

    tweet_id = user['tweet_1']["tweet_id"]
    response = client.delete(f'/tweets/{tweet_id}/delete', headers=header)
    response_info = response.json()

    expected_response = {
        "tweet_id": tweet_id,
        "delete_message": f'Tweet written by {user_info.first_name} has been deleted successfully!'
    }

    assert response.status_code == status.HTTP_200_OK
    assert response_info == expected_response


@pytest.mark.update
@pytest.mark.tweet
def test_update_tweet_failed(set_up_tweets):
    user = set_up_tweets['user_1']
    header = user['header']

    tweet_id = "00000000-0000-0000-0000-000000000000"

    data_to_send = {"content": "This is the new content of the tweet to test posting."}

    response = client.put(f'/tweets/{tweet_id}/update', json=data_to_send, headers=header)
    response_info = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_info["detail"] == "Tweet doesn't exist!"


@pytest.mark.update
@pytest.mark.tweet
def test_update_tweet(set_up_tweets):
    user = set_up_tweets['user_1']
    user_info = user['user_info']
    header = user['header']

    tweet = user['tweet_1']
    tweet_id = tweet["tweet_id"]

    data_to_send = {"content": "This is the new content of the tweet to test posting."}

    response = client.put(f'/tweets/{tweet_id}/update', json=data_to_send, headers=header)
    response_info = response.json()

    expected_response = {
        "tweet_id": tweet_id,
        "content": data_to_send["content"],
        "created_at": tweet["created_at"],
        "updated_at": str(date.today()),
        "user_id": user_info.user_id
    }

    assert response.status_code == status.HTTP_200_OK
    assert response_info == expected_response

