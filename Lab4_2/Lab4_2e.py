"""
Lab 4: Q2E: Create presigned URL's
"""
import boto3
import logging
bucket_name = 'ecs024lab42abucket'
key = 'README.md'
s3 = boto3.client('s3')
response = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket':bucket_name, 'Key': key})

print(response)