from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import bass_guitars

app = FastAPI(
    title="Leo's Music Shop API",
    version="0.0.1",
    description="This is the coolest API for Leo's Music Shop."
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(bass_guitars.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
