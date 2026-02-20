from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all websites (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add 5 sample books (runs once)
def add_sample_books():
    db = SessionLocal()
    if db.query(models.Book).count() == 0:
        books = [
            models.Book(title="Python Basics", author="John Smith", category="Programming", available=True),
            models.Book(title="Rich Dad Poor Dad", author="Robert Kiyosaki", category="Finance", available=True),
            models.Book(title="Data Structures", author="Mark Allen", category="Programming", available=False),
            models.Book(title="Clean Code", author="Robert C. Martin", category="Programming", available=True),
            models.Book(title="The Alchemist", author="Paulo Coelho", category="Fiction", available=True),
        ]
        db.add_all(books)
        db.commit()
    db.close()


add_sample_books()


# ----------------- CHAT API -----------------

@app.post("/chat")
def chat(message: dict, db: Session = Depends(get_db)):
    user_msg = message.get("message").lower()
    reply = "Sorry, I didn't understand that."

    # Availability check
    if "available" in user_msg:
        for book in db.query(models.Book).all():
            if book.title.lower() in user_msg:
                if book.available:
                    reply = f"Yes, '{book.title}' is available."
                else:
                    reply = f"Sorry, '{book.title}' is currently not available."
                break

    # Author check
    elif "author" in user_msg:
        for book in db.query(models.Book).all():
            if book.title.lower() in user_msg:
                reply = f"The author of '{book.title}' is {book.author}."
                break

    # Category listing
    elif "category" in user_msg or "show books" in user_msg:
        for book in db.query(models.Book).all():
            if book.category.lower() in user_msg:
                books = db.query(models.Book).filter(
                    models.Book.category.ilike(book.category)
                ).all()
                titles = [b.title for b in books]
                reply = f"Books in {book.category} category: " + ", ".join(titles)
                break

    # Save chat history
    chat_record = models.ChatHistory(
        user_message=user_msg,
        bot_reply=reply
    )
    db.add(chat_record)
    db.commit()

    return {"reply": reply}


# ----------------- BOOK APIs -----------------

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books


@app.post("/books")
def add_book(book: dict, db: Session = Depends(get_db)):
    new_book = models.Book(
        title=book["title"],
        author=book["author"],
        category=book["category"],
        available=book["available"]
    )
    db.add(new_book)
    db.commit()
    return {"message": "Book added successfully"}
