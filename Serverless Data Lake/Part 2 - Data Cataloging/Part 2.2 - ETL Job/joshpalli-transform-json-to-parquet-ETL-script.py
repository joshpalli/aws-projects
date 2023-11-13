import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1699738022587 = glueContext.create_dynamic_frame.from_catalog(
    database="joshpalli-sdl-demo-data",
    table_name="raw",
    transformation_ctx="AmazonS3_node1699738022587",
)

# Script generated for node Change Schema
ChangeSchema_node1699738113071 = ApplyMapping.apply(
    frame=AmazonS3_node1699738022587,
    mappings=[
        ("productname", "string", "productname", "string"),
        ("department", "string", "department", "string"),
        ("product", "string", "product", "string"),
        ("imageurl", "string", "imageurl", "string"),
        ("datesoldsince", "string", "date_start", "string"),
        ("datesolduntil", "string", "date_until", "string"),
        ("price", "int", "price", "int"),
        ("campaign", "string", "campaign", "string"),
        ("year", "string", "year", "string"),
        ("month", "string", "month", "string"),
        ("day", "string", "day", "string"),
        ("hour", "string", "hour", "string"),
    ],
    transformation_ctx="ChangeSchema_node1699738113071",
)

# Script generated for node Amazon S3
AmazonS3_node1699738125605 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1699738113071,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://sdl-immersion-day-690773662582/compressed-parquet/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1699738125605",
)

job.commit()
