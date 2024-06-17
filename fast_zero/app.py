from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def reead_root():
    return {'msg': 'ola mundo'}
