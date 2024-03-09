"""
API for Pypercraft
"""
import os
from fastapi import FastAPI, HTTPException, Query
from project import project

app = FastAPI()

DEFAULT_API_KEY = os.getenv("OPENAI_API_KEY")


@app.get("/example/")
async def some_example(
        api_key: str = Query(
            DEFAULT_API_KEY,
            title="API Key",
            description="Your API key."),
):
    """
    Function that generates a paper
    :param api_key: uuid
    :return:
    """
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Please provide an API Key.")

    result = project.Project(
        DEFAULT_API_KEY
    ).my_method()

    return result
