"""
Lab 4: Q1D: Get info about security groups
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.create_security_group(GroupName='Lab41I', Description='Lab41I created 10/29/19')
    print('Success', response)
except ClientError as e:
    print(e)