from app.models import HouseFeatures
from app.predict import predict_price

# Sample input based on the features defined in HouseFeatures
sample_input = HouseFeatures(
    area=7420,
    bedrooms=4,
    bathrooms=2,
    stories=3,
    mainroad='yes',            # String values should be in quotes
    guestroom='no',
    basement='no',
    hotwaterheating='no',
    airconditioning='no',
    parking=2,
    prefarea='yes',
    furnishingstatus='yes'            # Assuming 'furnished' is part of the features
)

# Call the predict_price function
predicted_price = predict_price(sample_input)

# Print the predicted price
print(f"Predicted Price: {predicted_price}")
