from pydantic import BaseModel
class HouseFeatures(BaseModel):
    area: float
    bedrooms:int
    bathrooms:int
    stories: int
    mainroad : object
    guestroom : object
    basement : object
    hotwaterheating:object
    airconditioning:object
    parking:int
    prefarea:object
    furnishingstatus:object

class PredictionResponse(BaseModel):
    price : float

