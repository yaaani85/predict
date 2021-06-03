from brane_predict import predict

#local testing
def test_predict():
  assert predict(True, True) == "Preprocessed data"
  
