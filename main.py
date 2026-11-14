import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def hello():
    return {"message": "Hello from SPARC Cloud!", "colour": os.getenv("COLOUR", "(not set)")}
