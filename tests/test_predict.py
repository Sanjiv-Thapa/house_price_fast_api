import unittest
from app.models import HouseFeatures
from app.predict import predict_price

class TestPredictPrice(unittest.TestCase):

    def test_predict_price(self):
        # Create a sample input based on the HouseFeatures model
        sample_input = HouseFeatures(
            area=7420,
            bedrooms=4,
            bathrooms=2,
            stories=3,
            mainroad='yes',
            guestroom='no',
            basement='no',
            hotwaterheating='no',
            airconditioning='no',
            parking=2,
            prefarea='yes',
            furnished='yes',
            furnishingstatus='semi-furnished'
        )

        # Call the predict_price function with the sample input
        predicted_price = predict_price(sample_input)

        # Assert that the prediction is a float
        self.assertIsInstance(predicted_price, float)

        # Optional: Add a check for a reasonable range
        self.assertGreater(predicted_price, 0)

if __name__ == "__main__":
    unittest.main()
