# The python package to connect to AWS
import boto3
#import sys
import click

# Create session with your credentials
session = boto3.Session(profile_name='iam_user')

# connect to an AWS rescources
ec2 = session.resource('ec2', region_name='us-east-1')

#@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
        
if __name__ == '__main__':
    list_instances()