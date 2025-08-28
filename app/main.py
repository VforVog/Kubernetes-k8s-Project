import os

from fastapi import FastAPI # type: ignore to stop the warning cause it works fine

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"From: {os.environ.get('ENV', 'DEFAULT_ENV')}"}


