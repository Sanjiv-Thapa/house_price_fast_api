from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.models import HouseFeatures, PredictionResponse
from app.predict import predict_price

app = FastAPI()

# Serve the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html", "r") as file:
        return file.read()

@app.post("/predict", response_model=PredictionResponse)
def predict_house_price(features: HouseFeatures):
    price = predict_price(features)
    return PredictionResponse(price=price)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
