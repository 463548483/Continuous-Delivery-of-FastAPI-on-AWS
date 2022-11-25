from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel

app = FastAPI()

# load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# train model
model = GaussianNB()
model.fit(X, y)


class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
async def root():
    return {"message": "Hello, this is page to make prediction"}


@app.post("/predict")
async def predict(body: request_body):
    X_new = [[body.sepal_length, body.sepal_width, body.petal_length, body.petal_width]]
    y_pred = model.predict(X_new)[0]
    return {"class": iris.target_names[y_pred]}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
