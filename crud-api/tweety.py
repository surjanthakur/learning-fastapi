from fastapi import FastAPI, status, HTTPException, Query
from fastapi.responses import JSONResponse
import json
import uuid
from pydantic_schema import Tweety

app = FastAPI()


def load_tweets():
    with open("tweety.json", "r") as file:
        result = json.load(file)
    return result


def save_tweets(data):
    with open("tweety.json", "w") as file:
        json.dump(data, file)


@app.get("/tweets")
def get_all_tweets():
    data = load_tweets()
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)


@app.get("/tweets/sort")
def sorted_tweets(sort_by: str = Query(title="get tweets base on username")):
    tweets = load_tweets()
    usernames = []
    for tweet in tweets:
        usernames.append(tweet["username"])
    print(usernames)


@app.post("/tweets/create")
def create_tweet(tweet_data: Tweety):
    data = load_tweets()
    tweet_id = str(uuid.uuid4())
    new_tweet = Tweety(
        id=tweet_id, username=tweet_data.username, content=tweet_data.content
    )
    tweet_dict = new_tweet.model_dump()
    data.append(tweet_dict)
    save_tweets(data)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content="tweet created successfully"
    )
