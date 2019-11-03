"""
Lab 4: First Python Boto3 activity
Q1A
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)