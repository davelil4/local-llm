from fastapi import FastAPI
from pydantic import BaseModel
import download as dl

app = FastAPI(debug=True)

class Generation(BaseModel):
    text: str

class Model(BaseModel):
    model: str

@app.get('/')
async def root():
    return {'message': 'Hello World!'}


@app.post('/t2t')
async def text2text(body: Generation):
    return body

@app.post('/tg')
async def text_gen(body: Generation):
    return body

@app.post('/imodel')
async def install_model(model: Model):
    try:
        res = dl.install_model(model.model)
    except:
        return "Model Doesn't Exist"
    return f"Installed Model, status code {res}"