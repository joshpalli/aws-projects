# Generating a Serverless Data Lake

## Description
This data engineering project is a deep dive into real-time data ingestion, ETL, and analytics services on AWS. In this project, I created a data set with Amazon Kinesis Data Firehose using a Kinesis Data Generator(KDG), using real-time data generating and streaming to build a data lake. From there, I used AWS Glue Crawlers to automatically construct a schema for my data lake and catalog my data. I then launched an ETL job on AWS Glue for my data to be extracted from files stored in S3, transformed into an Apache Parquet format, and then loaded onto a separate folder on my S3 bucket. I was able to build a processing pipeline without using clusters that was able to process vast amounts of data. The last stage of the project was about running analytics on the data lake. I configured Amazon Athena to query my data lake and Amazon QuickSight to create different visualizations to analyze business trends.

## AWS Services Used
* AWS Glue (Crawlers and Jobs)
* Amazon S3
* Amazon Athena
* Amazon QuickSight
* AWS CloudFormation
* AWS IAM
* Amazon Kinesis Data Firehose
* Amazon Cognito
* Amazon CloudWatch Events

## Other Technologies Used
* JSON
* Apache Parquet
* Structured Query Language (SQL)
* Python 3

## Generalized Procedure
### Part 1: Real-Time Data Streaming to Data Lake
1. Create an Amazon Kinesis Firehose Delivery Stream
2. Install the Kinesis Data Generator using AWS CloudFormation and configure a username and password for the generator using Cognito User Pools
3. Copy and paste the URL for the generator and log in using Cognito credentials
4. Configure stream to generate 100 records per second, copy and paste JSON file to communicate data format, and run the generator
5. Check Amazon CloudWatch Events for metrics and Amazon S3 to confirm data was transferred to S3 bucket

### Part 2.1: Cataloging Your Data
1. Create an AWS Glue Crawler to auto discover schema of data from Amazon S3
2. AWS Glue Crawler's configuration automatically creates cataloging tables, go to the "Table" section to see it.
3. Edit Metadata Schema and fix Partition Indexes

