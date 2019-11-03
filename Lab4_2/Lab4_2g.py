"""
Lab 4: Q2F: Retrieve a bucket policy
"""
import boto3
import json
s3 = boto3.client('s3')
bucket_name = 'ecs024lab42abucket'
bucket_policy = {
    'Version':'2012-10-17', 
    'Statement': [{
        'Sid':'AddPerm', 
        'Effect': 'Allow', 
        'Principal': '*', 
        'Action': ['s3.GetObject'], 
        'Resource': 'arn:aws:s3:::%s/*' % bucket_name
    }]
}
bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
response = s3.get_bucket_policy(Bucket=bucket_name)
print(response['Policy'])