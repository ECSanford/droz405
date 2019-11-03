"""
Lab 4: Q1D: Reboot an Amazon EC2 Instance
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['i-0c3a22281f7b6de20'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You do not have permission to reboot instances")
        raise
# Dry run succeeded, run start_instances again without dryrun
try:
    response = ec2.reboot_instances(InstanceIds=['i-0c3a22281f7b6de20'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)  
    # Do a dryrun first to verify permissions

