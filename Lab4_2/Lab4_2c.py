"""
Lab 4: Q2C: Upload files to our bucket
"""
import boto3
s3_client = boto3.client('s3')
filename = 'README.md'
bucket_name = 'ecs024lab42abucket'
s3_client.upload_file(filename, bucket_name, filename)
