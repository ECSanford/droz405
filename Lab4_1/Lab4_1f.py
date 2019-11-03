"""
Lab 4: Q1D: Create a new key pair
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName="ecs024Lab4_1fKey")
print('Success', response)