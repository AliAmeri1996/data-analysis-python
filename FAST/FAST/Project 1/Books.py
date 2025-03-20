from fastapi import Body, FastAPI
from typing import Optional

app=FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'math'}
]
@app.get("/books")# you have to add this endopoint to the end of URL, this
#will show the books
async def read_all_books():
    return BOOKS





@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

"""this is an example of using both path parameter and query parameter"""








@app.get("/books/mybooks/{id}")# books/mybooks are added into to path of url, with them,
# you cant fetch any information.
async def read_all_books(id:int):
    return {"book_title":f"My Favorite Book and {id}"}







@app.get("/books3/{id}")#basically, you can fill inside the curly bracket
#with whatever you want to get like /books/title%20four, which gives back
#book 4 title 4
async def read_book(book_title: Optional[str]=None):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

"""we can also default the query parameters, for example in the top example,
ive default it None which wouldnt accept anything, with optional, the default
value wouldnt be mentioned and also it wouldnt be required for the user too respond the
question.
"""






@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            # casefold means lower case
            return book # with this method, when you ask for example title one in the
        #swagger section, the information of title one appear






@app.get("/books2/{dynamic_param}")# the dynamic param inside the curly baracket
#must be similar to the one in the function below,
async def read_all_books(dynamic_param:str):#the str means the param must be a string.
    return {"dynamic_param":f"{dynamic_param}"}

"""so when we open uvicorn, we can copy the URL http://127.0.0.1:8000/books2/ali
and add to the end of it like the way mentioned, the outcome would be "dynamic_param":ali """









@app.get("/")# we dont have anything after book because in fastapi it automatically
#recognise that it should be whatever it is in the function.
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get("category").casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return
"""The given code defines an asynchronous FastAPI endpoint (/book/)
 that retrieves books based on a specified category.
 It iterates through a list of books (BOOKS),
checking if each book's category (case-insensitive comparison)
 matches the provided category parameter.
 If a match is found, the book is added to the books_to_return list .....
 http://127.0.0.1:8000/book/?category=history this is the URL, if you pay atterntion,
 ull notice the question mark"""






@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
"""this is an exmaple of both path parameter and query parameter for GET """







@app.post("/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    """you have to use double quotation mark when you want to post something"""

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

"""PUT is for updating the information not creating, that POST method
copy and paste the book from the original BOOKS in the box of rhe PUT method,
then change whatever you want to change and then execute"""

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):#the name book_title is what we have given,
    #its not important, what is important is "title" in the get method,from there,
    #you can pick a title
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():#"title" allows you to
            #get a specific information from the BOOKS api
            BOOKS.pop(i)
            break

"""this is for deleting the information"""