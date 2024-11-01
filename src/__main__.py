from fastapi import FastAPI
from routes import password_router


app = FastAPI()
app.include_router(password_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)