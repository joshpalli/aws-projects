# Building a Serverless Web Application called WildeRydes
In this project, I was given HTML code to deploy and host on AWS Amplify. This site, WildeRydes, is kind of like Uber, but with unicorns. In the general architecture of the website, I got to implemnent different features into the web application using AWS. First, I got to implement an authentication layer using Amazon Cognito so that users can create an account for the website. I also created a user pool and SNS notification so that there was a verification step for creating an account. I also got to add RESTful APIs to the application for communication between services using Amazon API Gateway. It was a great introduction project for serverless development.

## AWS Services Used
* AWS Amplify
* Amazon Cognito
* AWS IAM
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* AWS CLI

## Additional Technologies Used
* Python 3.11
* Git
* Terminal

## Challenges
* The biggest challenge in this project was working with Git for the first time. Setting up Git and AWS CLI had a lot of issues at first, but I ended up getting it done.
* Another big challenge was setting up verification and using user pools in Cognito. I ran into issues with receiving a confirmation email for my account. I fixed the issue by gaining a deeper understanding of the verification process, and restarting that implementation.
