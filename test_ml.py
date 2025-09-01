import pytest
import pandas as pd
from ml.data import apply_label
from ml.model import train_model, compute_model_metrics
from sklearn.linear_model import LogisticRegression

def test_apply_label():
    """
    Test the apply_label function.
    """
    assert apply_label([0]) == "<=50K"


def test_logistic_regression():
    """
    Test the logistic regression model training.
    """
    data = pd.DataFrame({
        'age': [40, 60, 30],
        'salary': [50000, 60000, 70000]
    })

    model = train_model(data[['age']], data['salary'])
    assert isinstance(model, LogisticRegression)


def test_three():
    """
    Test the compute_model_metrics function.
    """
    p,r,f1 = compute_model_metrics([1,0,1,1],[1,0,0,1])

    assert p == 1.0
    assert round(r, 4) == .6667
    assert f1 == .8
