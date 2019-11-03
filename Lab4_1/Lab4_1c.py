"""
#Starts and stops Amazon EC2 instance
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action == 'ON':
    #Do a dryrun first to verify pernmissions
    try: 
        ec2.start_instances(InstanceIds=['i-0ed7f2537971596c4'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances again without dryrun
    try: 
        response = ec2.start_instances(InstanceIds=['i-0ed7f2537971596c4'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    #Do a dryrun first to verify pernmissions
    try: 
        ec2.stop_instances(InstanceIds=['i-0ed7f2537971596c4'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run failed
    try: 
        response = ec2.stop_instances(InstanceIds=['i-0ed7f2537971596c4'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)