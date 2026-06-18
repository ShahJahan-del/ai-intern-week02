import pytest
import numpy as np
from sklearn.linear_model import LogisticRegression

# Simulate model and false data (unit test)
def test_predict_shape():
    # 1. Preparation of the model
    X_dummy = np.random.rand(10, 11)  # 10 lines, 11 features (like with the wine)
    y_dummy = np.random.randint(0, 2, 10)
    
    model = LogisticRegression()
    model.fit(X_dummy, y_dummy)
    
    # 2. Generate new test data (5 samples)
    X_test_dummy = np.random.rand(5, 11)
    
    # 3. Prediction
    predictions = model.predict(X_test_dummy)
    
    # 4. Checking correct shape : (5,)
    assert predictions.shape == (5,)