from fastapi import FastAPI

app = FastAPI()

search_started = False

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/start-search")
def start_search():
    global search_started
    search_started = True
    return {"message": "Job search started"}
