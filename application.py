# from flask import Flask, render_template, request, jsonify
# import boto3
# import json
# import hashlib
# from datetime import datetime

# app = Flask(__name__)


# import boto3
# from botocore.config import Config

# config = Config(region_name="us-east-1")

# REGION = "us-east-1"
# LAMBDA_FUNCTION_NAME = "x23379162-lambda"
# DYNAMODB_TABLE = "x23379162-dynamodb"

# lambda_client = boto3.client("lambda", region_name=REGION)
# dynamodb = boto3.resource("dynamodb", region_name=REGION)
# table = dynamodb.Table(DYNAMODB_TABLE)


# @app.route("/")
# def home():
#     return render_template("Classifier.html")


# # @app.route("/predictsc", methods=["POST"])
# # def predictsc():
# #     try:
        
# #         lambda_client = boto3.client("lambda", region_name="us-east-1")
# #         dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
# #         table = dynamodb.Table("x23379162-dynamodb")
        
# #         required_fields = [
# #             "age","sex","cp","trestbps","chol","fbs",
# #             "restecg","thalach","exang","oldpeak",
# #             "slope","ca","thal"
# #         ]

# #         input_data = {}

# #         for field in required_fields:
# #             value = request.form.get(field)
# #             if value is None or value == "":
# #                 return f"Missing field: {field}"
# #             input_data[field] = value

# #         # Generate deterministic request_id
# #         request_json = json.dumps(input_data, sort_keys=True)
# #         request_id = hashlib.sha256(request_json.encode()).hexdigest()

# #         #  1. Check if record already exists
# #         existing_item = table.get_item(Key={"request_id": request_id})

# #         if "Item" in existing_item:
# #             print("Cache hit — returning stored prediction")
# #             prediction = int(existing_item["Item"]["prediction"])

# #         else:
# #             print("Cache miss — calling Lambda")

# #             lambda_response = lambda_client.invoke(
# #                 FunctionName=LAMBDA_FUNCTION_NAME,
# #                 InvocationType="RequestResponse",
# #                 Payload=json.dumps(input_data)
# #             )

# #             payload = json.loads(lambda_response["Payload"].read())

# #             if payload.get("statusCode") != 200:
# #                 return f"Lambda Error: {payload}"

# #             body = json.loads(payload["body"])
# #             prediction = int(body["prediction"])

# #             table.put_item(
# #                 Item={
# #                     "request_id": request_id,
# #                     "prediction": prediction,
# #                     "timestamp": str(datetime.utcnow())
# #                 }
# #             )

# #         result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

# #         return render_template("result.html", result=result)

# #     except Exception as e:
# #         return f"Flask Error: {str(e)}"



# @app.route("/predictsc", methods=["POST"])
# def predictsc():
#     try:
#         lambda_client = boto3.client("lambda", region_name="us-east-1")
#         dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
#         table = dynamodb.Table("x23379162-dynamodb")

#         required_fields = [
#             "age","sex","cp","trestbps","chol","fbs",
#             "restecg","thalach","exang","oldpeak",
#             "slope","ca","thal"
#         ]

#         input_data = {}

#         for field in required_fields:
#             value = request.form.get(field)
#             if value is None or value == "":
#                 return f"Missing field: {field}"
#             input_data[field] = value

#         # 🔹 Bucketization function
#         def bucketize_input(data):
#             return {
#                 "age": int(data["age"]) // 5 * 5,
#                 "sex": int(data["sex"]),
#                 "cp": int(data["cp"]),
#                 "trestbps": int(data["trestbps"]) // 10 * 10,
#                 "chol": int(data["chol"]) // 20 * 20,
#                 "fbs": int(data["fbs"]),
#                 "restecg": int(data["restecg"]),
#                 "thalach": int(data["thalach"]) // 5 * 5,
#                 "exang": int(data["exang"]),
#                 "oldpeak": round(float(data["oldpeak"]) * 2) / 2,
#                 "slope": int(data["slope"]),
#                 "ca": int(data["ca"]),
#                 "thal": int(data["thal"])
#             }

#         # 🔹 Apply bucketization
#         bucketed_data = bucketize_input(input_data)

#         # 🔹 Generate request_id using bucketed values
#         request_json = json.dumps(bucketed_data, sort_keys=True)
#         request_id = hashlib.sha256(request_json.encode()).hexdigest()

#         # 🔹 Check cache
#         existing_item = table.get_item(Key={"request_id": request_id})

#         if "Item" in existing_item:
#             print("Cache hit — returning stored prediction")
#             prediction = int(existing_item["Item"]["prediction"])

#         else:
#             print("Cache miss — calling Lambda")

#             lambda_response = lambda_client.invoke(
#                 FunctionName=LAMBDA_FUNCTION_NAME,
#                 InvocationType="RequestResponse",
#                 Payload=json.dumps(input_data)  # send original data to model
#             )

#             payload = json.loads(lambda_response["Payload"].read())

#             if payload.get("statusCode") != 200:
#                 return f"Lambda Error: {payload}"

#             body = json.loads(payload["body"])
#             prediction = int(body["prediction"])

#             # 🔹 Store in DynamoDB
#             table.put_item(
#                 Item={
#                     "request_id": request_id,
#                     "bucketed_input": bucketed_data,
#                     "original_input": input_data,
#                     "prediction": prediction,
#                     "timestamp": str(datetime.utcnow())
#                 }
#             )

#         result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

#         return render_template("result.html", result=result)

#     except Exception as e:
#         return f"Flask Error: {str(e)}"
        

# # Create fresh clients per request (prevents expired token issues)
# def get_lambda_client():
#     return boto3.client("lambda", region_name=REGION)


# def get_dynamodb_table():
#     dynamodb = boto3.resource("dynamodb", region_name=REGION)
#     return dynamodb.Table(DYNAMODB_TABLE)


# @app.route("/normal", methods=["POST"])
# def normal():
#     try:
#         data = request.get_json()

#         if not data:
#             return jsonify({"error": "Invalid JSON"}), 400

#         required_fields = [
#             "age","sex","cp","trestbps","chol","fbs",
#             "restecg","thalach","exang","oldpeak",
#             "slope","ca","thal"
#         ]

#         input_data = {}

#         for field in required_fields:
#             if field not in data:
#                 return jsonify({"error": f"Missing field: {field}"}), 400
#             input_data[field] = data[field]

#         # Generate deterministic request_id
#         request_json = json.dumps(input_data, sort_keys=True)
#         request_id = hashlib.sha256(request_json.encode()).hexdigest()

#         lambda_client = get_lambda_client()
        
#         print("Lambda hit")

#         lambda_response = lambda_client.invoke(
#             FunctionName=LAMBDA_FUNCTION_NAME,
#             InvocationType="RequestResponse",
#             Payload=json.dumps(input_data)
#         )

#         payload = json.loads(lambda_response["Payload"].read())
        
#         # i want to create key for range of inputs like heartbeat and other medical metrics changes every second so it will send every request to the 
#         # lambda so i want when user gives some input it will create request_id on the basis of that range and check in dynamodb so that it wont go for lambda on every small change in input   
        
#         body = json.loads(payload["body"])
#         prediction = int(body["prediction"])

#         table.put_item(
#             Item={
#                 "request_id": request_id,
#                 "prediction": prediction,
#                 "timestamp": str(datetime.utcnow())
#             }
#         )

#         return jsonify({"prediction": prediction}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)
    

from flask import Flask, render_template, request, jsonify
import boto3
import json
import hashlib
from datetime import datetime
from decimal import Decimal

app = Flask(__name__)

REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "x23379162-lambda"
DYNAMODB_TABLE = "x23379162-dynamodb"


# Create fresh clients
def get_lambda_client():
    return boto3.client("lambda", region_name=REGION)


def get_dynamodb_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(DYNAMODB_TABLE)


# Convert floats → Decimal (for DynamoDB)
def convert_floats_to_decimal(obj):
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimal(i) for i in obj]
    return obj


#  Bucketization (range grouping)
def bucketize_input(data):
    return {
        "age": int(data["age"]) // 5 * 5,
        "sex": int(data["sex"]),
        "cp": int(data["cp"]),
        "trestbps": int(data["trestbps"]) // 10 * 10,
        "chol": int(data["chol"]) // 20 * 20,
        "fbs": int(data["fbs"]),
        "restecg": int(data["restecg"]),
        "thalach": int(data["thalach"]) // 5 * 5,
        "exang": int(data["exang"]),
        "oldpeak": round(float(data["oldpeak"]) * 2) / 2, 
        "slope": int(data["slope"]),
        "ca": int(data["ca"]),
        "thal": int(data["thal"])
    }


@app.route("/")
def home():
    return render_template("Classifier.html")


# =========================================================
#  WITH CACHE (Range-based request_id)
# =========================================================
@app.route("/predictsc", methods=["POST"])
def predictsc():
    try:
        lambda_client = get_lambda_client()
        table = get_dynamodb_table()

        required_fields = [
            "age","sex","cp","trestbps","chol","fbs",
            "restecg","thalach","exang","oldpeak",
            "slope","ca","thal"
        ]

        input_data = {}

        for field in required_fields:
            value = request.form.get(field)
            if value is None or value == "":
                return f"Missing field: {field}"
            input_data[field] = value

        #  Bucketize
        bucketed_data = bucketize_input(input_data)

        #  Generate request_id
        request_json = json.dumps(bucketed_data, sort_keys=True)
        request_id = hashlib.sha256(request_json.encode()).hexdigest()

        #  Check cache
        existing_item = table.get_item(Key={"request_id": request_id})

        if "Item" in existing_item:
            print("Cache hit")
            prediction = int(existing_item["Item"]["prediction"])

        else:
            print("Cache miss → calling Lambda")

            lambda_response = lambda_client.invoke(
                FunctionName=LAMBDA_FUNCTION_NAME,
                InvocationType="RequestResponse",
                Payload=json.dumps(input_data)
            )

            payload = json.loads(lambda_response["Payload"].read())

            if payload.get("statusCode") != 200:
                return f"Lambda Error: {payload}"

            body = json.loads(payload["body"])
            prediction = int(body["prediction"])

            #  Convert to Decimal before storing
            bucketed_data_db = convert_floats_to_decimal(bucketed_data)

            table.put_item(
                Item={
                    "request_id": request_id,
                    "bucketed_input": bucketed_data_db,
                    "original_input": input_data,
                    "prediction": prediction,
                    "timestamp": str(datetime.utcnow())
                }
            )

        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Flask Error: {str(e)}"


# =========================================================
#  WITHOUT CACHE (but still stores result)
# =========================================================
@app.route("/normal", methods=["POST"])
def normal():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        required_fields = [
            "age","sex","cp","trestbps","chol","fbs",
            "restecg","thalach","exang","oldpeak",
            "slope","ca","thal"
        ]

        input_data = {}

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
            input_data[field] = data[field]

        lambda_client = get_lambda_client()
        table = get_dynamodb_table()

        print("Lambda hit")

        lambda_response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",
            Payload=json.dumps(input_data)
        )

        payload = json.loads(lambda_response["Payload"].read())
        body = json.loads(payload["body"])
        prediction = int(body["prediction"])

        #  Bucketize for storage
        bucketed_data = bucketize_input(input_data)
        bucketed_data_db = convert_floats_to_decimal(bucketed_data)

        request_json = json.dumps(bucketed_data, sort_keys=True)
        request_id = hashlib.sha256(request_json.encode()).hexdigest()

        table.put_item(
            Item={
                "request_id": request_id,
                "bucketed_input": bucketed_data_db,
                "original_input": input_data,
                "prediction": prediction,
                "timestamp": str(datetime.utcnow())
            }
        )

        return jsonify({"prediction": prediction}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)