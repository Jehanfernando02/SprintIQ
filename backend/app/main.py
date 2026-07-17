from fastapi import FastAPI

app = FastAPI(title = "SprintIQ API")

@app.get("/")
def root():
    return {"message": "SprintIQ is running"}

@app.get("/health")
def health():
    return {"status": "ok"}


