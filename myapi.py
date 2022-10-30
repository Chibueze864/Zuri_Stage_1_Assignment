from fastapi import FastAPI



app = FastAPI()



@app.get("/")
def index():
    return { "slackUsername": "Chibueze", "backend": True, "age": 27, "bio": "Excited to be here"}


