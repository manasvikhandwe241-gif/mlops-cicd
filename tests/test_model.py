
from src.model import train_model


def test_model_accuracy():
    accuracy = train_model()

    assert accuracy >= 1.01, (
        f"Model accuracy is too low: {accuracy}"
    )
