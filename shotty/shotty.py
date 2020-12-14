# The python package to connect to AWS
import boto3

# Create session with your credentials
session = boto3.Session(profile_name='iam_user')

# connect to an AWS rescources
ec2 = session.resource('ec2', region_name='us-east-1')

for i in ec2.instances.all():
    print(i)