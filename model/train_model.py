import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import pickle

# Load the dataset
data = pd.read_csv('./data/Housing.csv')

def preprocess_data(df):
    df = df.dropna()  # Drop rows with missing values
    X = df.drop('price', axis=1)  # Separate features
    y = df['price']  # Separate target variable
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

    # Create preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ])
    
    X = preprocessor.fit_transform(X)
    return X, y, preprocessor

# Preprocess the data
X, y, preprocessor = preprocess_data(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")

# Save the trained model and preprocessor
with open('./model/housing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('./model/preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)
