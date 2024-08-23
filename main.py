from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get("/auth")
def read_root():
    return FileResponse ('/templates/login.html')

# 將 static 目錄掛載到 /static 路徑
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)
