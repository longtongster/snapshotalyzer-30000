# The python package to connect to AWS
import boto3
#import sys
import click


# Create session with your credentials
session = boto3.Session(profile_name='iam_user')

# connect to an AWS rescources
ec2 = session.resource('ec2', region_name='us-east-1')

@click.group()
def instances():
    """Commands for instances"""

    
@instances.command('list')
@click.option('--project', default=None,
             help="Only instances for project (tag Project:<name)")
def list_instances(project):
    "List EC2 instances"
    instances = []
    
    if project:
        filters = [{'Name':'tag:Name','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
        
    for i in instances:
        #print(i.tags)
        tags = {element['Key']:element['Value'] for element in i.tags or []}
        #print(tags)
        print(', '.join((
                i.id,
                i.instance_type,
                i.placement['AvailabilityZone'],
                i.state['Name'],
                i.public_dns_name,
                tags.get('Project','<no projects>'))))
        print()
        
if __name__ == '__main__':
    instances()