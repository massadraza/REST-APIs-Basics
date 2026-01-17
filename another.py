from fastapi import FastAPI

app = FastAPI()

@app.get("/nothing")
async def root():
    return {"message": "Hello World"}