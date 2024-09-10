
# House Price Prediction API

This is a simple application built to predict house prices using FastAPI. The project leverages a machine learning model trained on house pricing data and provides a REST API to make predictions.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Directory Structure](#directory-structure)
4. [Model Information](#model-information)
5. [Testing](#testing)
6. [Contributing](#contributing)
---

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd house_price
```

### 2. Set up a virtual environment (Optional but recommended)
```bash
python3 -m venv myenv
source myenv/bin/activate   # On Windows use: myenv\Scripts\activate
```

### 3. Install dependencies
Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Start the application
Once the environment is set up and dependencies are installed, run the FastAPI app:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

---

## Usage

Once the application is running, you can make API requests to predict house prices. 

### Example Request

Send a POST request to the `/predict` endpoint with the required features as a JSON payload.

**Sample Payload**:
```json
{
  'area':7420,
    'bedrooms':4,
    'bathrooms':2,
    'stories':3,
    'mainroad':'yes',            # String values should be in quotes
    'guestroom':'no',
    'basement':'no',
    'hotwaterheating':'no',
    'airconditioning':'no',
    'parking':2,
    'prefarea':'yes',
    'furnishingstatus':'yes'
}
```

**Sample Response**:
```json
{
  "predicted_price": 450000
}
```

---

## Directory Structure

Here’s an overview of the main folders and their purpose:

```
house_price/
│
├── app/               # Contains the FastAPI app logic
├── data/              # Data files used for training the model
├── model/             # Contains the machine learning model files
├── notebooks/         # Jupyter notebooks for data exploration and model training
├── static/            # Static files (e.g., images, CSS files)
├── tests/             # Unit tests for the API
├── README.md          # This file
├── requirements.txt   # List of dependencies
└── test_predict.py    # Test script for model predictions
```

---

## Model Information

The machine learning model is trained on a dataset of house prices. The key features include:

- Number of bedrooms
- Number of bathrooms
- Square footage of living space and lot
- Number of floors
- House condition and grade

The model was trained using the following steps (if applicable, mention the algorithm and process):

1. Data Cleaning and Preprocessing
2. Feature Engineering
3. Model Training (e.g., Linear Regression, Random Forest, etc.)
4. Model Evaluation using metrics like RMSE (Root Mean Squared Error) and R² score.

---

## Testing

To ensure everything is working correctly, you can run the unit tests provided in the `tests/` folder.

```bash
pytest tests/
```

Additionally, there’s a `test_predict.py` script that tests the prediction functionality:

```bash
python test_predict.py
```

---

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

---
