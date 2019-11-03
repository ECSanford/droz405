"""
Lab 4: Q1B: Start and Stop Detailed Monitoring of an EC2 instance
"""
import sys
import boto3
ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-0fc3330382c802464'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-0fc3330382c802464'])
print(response)