from fastapi.testclient import TestClient
from app.main import app
import unittest

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_predict_endpoint(self):
        # Sample input data
        sample_data = {
            "area": 7420,
            "bedrooms": 4,
            "bathrooms": 2,
            "stories": 3,
            "mainroad": "yes",
            "guestroom": "no",
            "basement": "no",
            "hotwaterheating": "no",
            "airconditioning": "no",
            "parking": 2,
            "prefarea": "yes",
            "furnishingstatus": "semi-furnished"
        }

        # Send a POST request to the /predict endpoint
        response = client.post("/predict", json=sample_data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains a price key
        data = response.json()
        self.assertIn("price", data)

        # Assert that the price is a float and greater than 0
        self.assertIsInstance(data["price"], float)
        self.assertGreater(data["price"], 0)

if __name__ == "__main__":
    unittest.main()
