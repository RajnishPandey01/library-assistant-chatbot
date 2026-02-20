📚 Library Assistant Chatbot

A simple Full Stack Web Application built using FastAPI, SQLite, HTML, CSS, and JavaScript.

This chatbot helps users:

✅ Check book availability

✅ Find book authors

✅ View books by category

✅ Store chat history

🚀 Tech Stack
🔹 Backend

Python

FastAPI

SQLite

🔹 Frontend

HTML

CSS

JavaScript

📁 Project Structure

library-assistant-chatbot/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md

 💡 Features

Keyword-based chatbot logic

SQLite database integration

Chat history storage

Simple and clean UI

REST API using FastAPI

Interactive API docs

🛠 How to Run the Project

🔹 Step 1: Clone the Repository
git clone https://github.com/your-username/library-assistant-chatbot.git
cd library-assistant-chatbot
🔹 Step 2: Setup Backend
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install fastapi uvicorn pydantic
🔹 Step 3: Run Backend Server
python -m uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API Docs available at:

http://127.0.0.1:8000/docs
🔹 Step 4: Run Frontend

Open frontend/index.html

Right click → Open with Live Server

Make sure URL looks like:

http://127.0.0.1:5500/index.html


