from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

def preprocess_input(df):
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num',StandardScaler(),numerical_cols),
            ('cat',OneHotEncoder(handle_unknown='ignore'),categorical_cols)
        ]
    )
    df_preprocessed = preprocessor.fit_transform(df)
    return df_preprocessed

