from sqlalchemy.orm import Session
from . import models, schemas

def get_tweets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tweet).offset(skip).limit(limit).all()

def create_tweet(db: Session, tweet: schemas.TweetCreate):
    db_tweet = models.Tweet(content=tweet.content)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet
