# snapshotalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## Remark 

Code does not run in a notebook nor in spyder. 
You really need to use the command line

## About

This project is a demo, and uses boto3 to manage 
AWS EC2 instance snapshots.

##

Shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`python shotty/shotty.py`

*command* is list, start or stop
*project* is optional
