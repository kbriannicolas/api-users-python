from fastapi import FastAPI
import webbrowser
from src.routes import users_db
app = FastAPI()

app.include_router(users_db.router)


@app.get('/')
async def root():
    url = "https://apiusers-1-v3146811.deta.app/docs"
    return open_page(url)


def open_page(url):
    webbrowser.open(url)
