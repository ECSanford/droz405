"""
Lab 4: Q1D: Get info about security groups
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds=['sg-036d4db37daddba11'])
    print('Success', response)
except ClientError as e:
    print(e)