from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

# Load precomputed data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")


from fastapi.responses import RedirectResponse

@app.get("/")
def root():
    return RedirectResponse(url="/book")


@app.get("/book", response_class=HTMLResponse)
def index(request: Request):
    # Prepare a list of dictionaries for all books
    books_data = [
    {
        "book_name": str(row['Book-Title']),
        "author": str(row['Book-Author']),
        "image": str(row['Image-URL-M']),
        "votes": int(row['num_rating']),
        "rating": float(row['avg_rating'])
    }
    for _, row in popular_df.iterrows()
]
    return templates.TemplateResponse("index.html", {"request": request, "books_data": books_data})


@app.get("/recommend", response_class=HTMLResponse)
def recommend_ui(request: Request):
    return templates.TemplateResponse("recommend.html", {"request": request})


@app.post("/recommend_books", response_class=HTMLResponse)
def recommend_books(request: Request, user_input: str = Form(...)):
    if user_input not in pt.index:
        raise HTTPException(status_code=404, detail="Book not found")

    index = np.where(pt.index == user_input)[0][0]

    # Get top 5 similar books
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_books = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        recommended_books.append({
            "book_name": str(temp_df['Book-Title'].values[0]),
            "author": str(temp_df['Book-Author'].values[0]),
            "image": str(temp_df['Image-URL-M'].values[0])
        })

    return templates.TemplateResponse(
        "recommend.html",
        {"request": request, "recommended_books": recommended_books, "user_input": user_input}
    )
