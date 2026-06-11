from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Base
import crud
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quote Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quote")
def get_quote():

    response = requests.get("https://dummyjson.com/quotes/random")

    data = response.json()

    quote = data["quote"]

    author = data["author"]

    db = SessionLocal()

    crud.save_quote(db, quote, author)

    db.close()

    return {

        "quote": quote,

        "author": author

    }


@app.get("/history")
def history():

    db = SessionLocal()

    data = crud.get_history(db)

    db.close()

    return data