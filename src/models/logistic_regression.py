from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd


def log_regression(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series):

    categorical_cols = X_train.select_dtypes(include="object").columns
    numerical_cols = X_train.select_dtypes(exclude="object").columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numerical_cols),
        ]
    )

    model = Pipeline(steps=[("preprocessing", preprocessor), ("classifier", LogisticRegression(max_iter=10000))])

    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test)) * 100

    print(f"Logistic Regression model accuracy: {acc:.2f}%")
