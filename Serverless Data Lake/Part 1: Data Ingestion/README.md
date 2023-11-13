# Part 1: Data Ingestion
## Description
In this part of the project, I installed a Kinesis Data Generator using AWS CloudFormation with Amazon Cognito credentials, and used that generator to create data for my data lake. I then used a Kinesis Data Delivery Stream to push the data to Amazon S3.

## AWS Services
* AWS CloudFormation
* Amazon Cognito
* Amazon Kinesis Data Firehose
* Amazon S3
* AWS IAM

## Other Technologies Used
* JSON files

## File Guide
1. CloudFormationTemplates.png - An image of the CloudFormation stacks that were created for this project.
2. CognitoUserPool.png - An image of the Cognito User Pool configuration with my username for the Kinesis Data Generator confirmed.
3. DataIngestedToS3 - An image showing the data successfully delivered to Amazon S3
4. DataIngestionCloudWatchMonitoring.png - An image of the CloudWatch metrics for the Kinesis Data Firehose Delivery Stream.
5. DataTemplate.json - A JSON file for the general structure parameters of the data.
6. ExampleDataGenerated.json - A JSON file showing a test run of the Kinesis Data Generator, where it generated a single piece of data.
7. JSONDataIngestionTemplate.png - An image showing DataTemplate.json being uploaded to the Kinesis Data Generator.
8. serverlessDataLakeImmersionIAMcf.json - A file that implements the appropriate IAM roles and policies needed to complete the project.
