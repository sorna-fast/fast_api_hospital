from fastapi import FastAPI
from router import drs, parts, Nurses, Employees, Patients, post, File
from database.db import engine
from database.models import base
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

app.include_router(drs.router)
app.include_router(parts.router)
app.include_router(Nurses.router)
app.include_router(Employees.router)
app.include_router(Patients.router)
app.include_router(post.router)
app.include_router(File.router)

#base.metadata.create_all(engine)