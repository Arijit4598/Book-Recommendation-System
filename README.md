# 📚 Book Recommendation System

A machine learning project that recommends books to users based on popularity and content similarity.  
This system helps users discover new books tailored to their interests.

---

## 🚀 Features
- Popularity-based recommendations (Top trending books)
- Content-based filtering using cosine similarity
- Preprocessing of book metadata (title, author, genre, etc.)
- Simple API powered by **FastAPI**
- Scalable design for deployment with Docker

---

## 🛠️ Tech Stack
- **Python 3**
- **FastAPI** (for serving recommendations)
- **Pandas, NumPy**
- **Scikit-learn** (for similarity calculation)
- **Uvicorn** (server)
- **Jupyter Notebook** (for experimentation)

---

## 📂 Project Structure
- Book-Recommendation-System/
- ├── data/ # Dataset (books.csv, ratings.csv, etc.)
- ├── notebooks/ # Jupyter notebooks for EDA and experiments
- ├── app/
- │ ├── main.py # FastAPI app entrypoint
- │ ├── model.pkl # (Optional) Precomputed similarity matrix
- ├── requirements.txt # Dependencies
- └── README.md # Documentation
