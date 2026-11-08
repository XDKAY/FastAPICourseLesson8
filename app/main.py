from fastapi import FastAPI, Query

from .models import (
    FeedackRequestScheme,
    FeedbackResponseScheme
)
from .message import message_handler


app = FastAPI(
    title="FastAPI Course Lesson 8"
)


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.post("/feedback", response_model=FeedbackResponseScheme)
async def feedback_handler(
    feedback: FeedackRequestScheme,
    is_premium: bool = Query(default=False)
):
    return FeedbackResponseScheme(
        message=message_handler(
            username=feedback.username,
            is_premium=is_premium
        )
    )
