"""
Lab 4: Q1D: Delete a key pair
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName="ecs024Lab4_1fKey")
print('Success', response)