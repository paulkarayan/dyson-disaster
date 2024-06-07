from pydantic import BaseModel
import datetime

class TweetBase(BaseModel):
    content: str

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
