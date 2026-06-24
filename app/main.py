from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "whisper STT API" ,
        "status": "running"
    }