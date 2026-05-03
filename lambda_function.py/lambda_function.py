import boto3
import csv
import uuid
from io import StringIO

# Initialize AWS services
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(" lambda-project-table")  # DynamoDB table name

def lambda_handler(event, context):
    print("Received event:", event)

    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        # Read CSV file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response["Body"].read().decode("utf-8")
        csv_reader = csv.DictReader(StringIO(file_content))

        # Save each row into DynamoDB
        for row in csv_reader:
            row["id"] = str(uuid.uuid4())  # Generate a unique ID
            table.put_item(Item=row)
            print(f"Saved to DynamoDB: {row}")

    return {"statusCode": 200, "body": "CSV Data Saved Successfully"}