from fastapi import FastAPI

app1 = FastAPI()


@app1.get('/')
def main():
    response = {"data": {"name": "pooja", "person": "learner"}}
    return response


@app1.get('/about')
def main():
    response = {"about": "page"}
    return response