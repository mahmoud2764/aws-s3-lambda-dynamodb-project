# AWS S3 → Lambda → DynamoDB Project

## Project Overview
This project demonstrates an event-driven serverless architecture using AWS.

When a CSV file is uploaded to Amazon S3:

1. Amazon S3 triggers AWS Lambda
2. Lambda reads the CSV file
3. Lambda processes each row
4. Data is stored in Amazon DynamoDB

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- AWS IAM

---

## Architecture

S3 Bucket → Lambda Function → DynamoDB Table

---

## Implementation Steps

### Step 1: Created S3 Bucket
Created an S3 bucket for file uploads.

Bucket Name:
bucket-fto-lambda

---

### Step 2: Created DynamoDB Table
Created a DynamoDB table.

Table Name:
lambda-project-table

Partition Key:
id

---

### Step 3: Created Lambda Function
Created a Python-based Lambda function.

Lambda function tasks:

- Trigger when file is uploaded to S3
- Read CSV file from S3
- Generate unique ID for each row
- Store records in DynamoDB

---

### Step 4: Connected S3 Trigger
Configured ObjectCreated event trigger from S3 to Lambda.

---

### Step 5: Tested the Project
Uploaded trigger.csv into S3 bucket.

Lambda executed automatically.

Verified inserted records in DynamoDB.

---

## Project Output

Successfully built a serverless data pipeline using AWS services.

CSV data uploaded to S3 is automatically processed and stored in DynamoDB.

---

## Skills Demonstrated

- Serverless Architecture
- Event-Driven Design
- Python with boto3
- Cloud Debugging
- AWS Service Integration
