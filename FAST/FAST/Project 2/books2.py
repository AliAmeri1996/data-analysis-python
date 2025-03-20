from typing import Optional

from fastapi import  FastAPI, Path,Query,HTTPException,status
from pydantic import BaseModel,Field
# field is for making validation even more specific

app=FastAPI()


class Book:
    # Class-level type hints
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__( self,id: int,title: str,author: str,description: str,rating: int, published_date:int ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date=published_date




class BookRequest(BaseModel):# this is for validating the imformation that we want to add
    # to the books api via post
    id:Optional[int] # this give the id the ability to not be seen
    title: str=Field(min_length=3)# field makes a specified filter for each information that we want to
    #to post
    author: str=Field(min_length=1)
    description: str=Field(min_length=1,max_length=100)
    rating: int=Field(gt=0,lt=5)
    published_date :int=Field(gt=1950,lt=2050)


    model_config={ # this will show by default how you should post data
       "json_schema_extra":{
          "example":{"id":2,
            "title":"A new book",
            "author":"coding with ali",
            "description":"A new era",
            "rating":5,
            "published":1985
    }


 }


}





BOOKS=[ Book(1,"computer pro","coding with ruby","hes doing good",5,1990),
        Book(2,"Physics","Ali ","hes doing bad",3,1995),
        Book(3,"math","hos ","all good",1,1998)]




@app.get("/books")
async def read():
    return BOOKS





@app.get("/books",status_code=status.HTTP_200_OK)
async def published_year(book_published:int=Query(gt=1950,lt=2050)):#this
    #query makes sure that no date out of the boundary is mentioned
    for book in BOOKS:
        if book.published_date==book_published:
          return book





@app.get("/books/{book_id}/",status_code=status)# with this method we can get the books by typing the id number
async def read_book_on_id(book_id:int=Path(gt=0)):# the path is extra validation,
    #if 0 is entered as an id, and we dont have zero, itll throw an error
    for book in BOOKS:
        if book.id==book_id:
            return book
        raise HTTPException(status_code=404,detail="Item not find")
        """with this raise method, when an id that does not exist is requested,
        we get the error which says Item not find"""
        """this method where the book_id is both in the {} and the following function,
        is called path parameter method....also the status code in the paranthesis shows
        the status codes, so you dont need to memorise them"""



@app.get("/books/")# with this method we can get the books by typing the rating number
async def read_book_on_rating(book_rating:int=Query(gt=0,lt=6)):
    books_to_return=[]# list is important if the result is more than one
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return
"""this method that the path is only mentioned in the function 
, is called query parameter method"""




@app.get("/books4")
async def read_title(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book




@app.post("/create_book")
async def create_book(book_request:BookRequest):#now this BookRequest basically
    #filters the information that is posted with the format that have been mentioned
    #The double asterisk (**) in Book(**book_request.dict())
    # is used for unpacking a dictionary into keyword arguments.
    new_book=Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):# this function allows that whenever we add a newbook,
    #regardless of what number we give to id, itll asign a number in front of the last id
    #so even if we add a book with id=0, itll automatically changes to the next number
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id +1
    return book


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id== book.id:
            BOOKS[i] = book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail="Item not found")
    """this method of raise is for extra validation and it could be quite usefull"""


@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int=Path(gt=0)):#the name book_title is what we have given,
    #its not important, what is important is "title" in the get method,from there,
    #you can pick a title
    for i in range(len(BOOKS)):
        if BOOKS[i].id ==book_id:
            #get a specific information from the BOOKS api
            BOOKS.pop(i)
            break

