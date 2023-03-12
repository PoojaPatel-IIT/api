from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    response = {"data": {"name": "pooja", "person": "learner"}}
    return response


@app.get('/about')
def about():
    response = {"about": "page"}
    return response