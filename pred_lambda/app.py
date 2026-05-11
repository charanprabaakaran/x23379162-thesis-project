import json
import joblib
import numpy as np
from mlxtend.classifier import StackingClassifier
# Load model ONCE (outside handler)
model = joblib.load("heart_model.sav")

def lambda_handler(event, context):
    try:
        # If invoked via API Gateway, body may be string
        if isinstance(event, dict) and "body" in event:
            event = json.loads(event["body"])

        features = [
            float(event["age"]),
            float(event["sex"]),
            float(event["cp"]),
            float(event["trestbps"]),
            float(event["chol"]),
            float(event["fbs"]),
            float(event["thalach"]),
            float(event["exang"]),
            float(event["restecg"]),
            float(event["oldpeak"]),
            float(event["slope"]),
            float(event["ca"]),
            float(event["thal"])
        ]

        prediction = int(model.predict([features])[0])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": prediction
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }