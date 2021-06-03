from brane_predict import predict

# local testing
def test_predict():
    assert predict("lightgbm", True, True) == "Made prediction"
