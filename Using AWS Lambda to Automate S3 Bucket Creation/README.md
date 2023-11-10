# Using AWS Lambda and Boto3 SDK for Python to Automate Creation of S3 Buckets
In this project, I got to gain hands-on experience in working with Boto3. I was originally learning Boto3 to implement a script into a separate AWS project I was working on. The script uses the create_bucket function found on the [S3 Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html) and takes in a name and region for the bucket.

## AWS Services Used
* Amazon S3
* AWS Lambda

## Challenges
The biggest challenge I had to overcome in this project was learning Boto3 without any previous knowledge. I watched a video tutorial online to build a basic function and learn the general structure of the programming SDK. I had some trial and error mainly with the naming conventions of S3, as there were bucket names that were already being used. After some basic trial and error in the testing phase of the Lambda function, I got it to work, and I checked the S3 console for confirmation that the bucket was created.
