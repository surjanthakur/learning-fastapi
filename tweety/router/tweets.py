from fastapi import APIRouter, HTTPException, status, Depends, Path
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from database.database import get_session
from validation.pydantic_schema import pydantic_tweet
from database.sql_model import Tweet
from sqlmodel import select

tweet_router = APIRouter(tags=["tweets"], prefix="/tweets")


@tweet_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_tweet(db: AsyncSession = Depends(get_session)):
    result = await db.exec(select(Tweet))
    tweets = result.all()
    if not tweets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="db has no tweets right now !!",
        )
    return tweets
