import requests
from fastapi import FastAPI

app = FastAPI()

URL = 'https://restcountries.com/v3.1/all?fields=name,flags`'

@app.get("/")
async def first_api(book_title:str):
    for book in URL:
        if book.get('common').casefold() == book_title.casefold():
            return book


    # response = requests.get(URL)
    # # response.json() will convert the JSON from the API into a Python dictionary
    # return response










