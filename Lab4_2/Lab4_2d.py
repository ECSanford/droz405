"""
Lab 4: Q2D: Download files from our Amazon S3 bucket
"""
import boto3
import botocore
s3 = boto3.resource('s3')
filename = 'README.md'
bucket_name = 'ecs024lab42abucket'
key = 'README.md'
s3.Bucket(bucket_name).download_file(key, filename)
