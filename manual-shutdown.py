#!/usr/bin/env python

import sys
import time
import os
import pprint
from datetime import datetime, timedelta
from dateutil.tz import tzutc

import boto3
from moto import mock_ec2

@mock_ec2
def main():
    # aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    # aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

    client = boto3.client('ec2', region_name='eu-west-1')

    client.run_instances(
        ImageId="ami-0ce8e484b3cf57bbb", 
 
        MinCount=1, 
 
        MaxCount=1,

        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Javier'
                    },
                    {
                        'Key': 'Team',
                        'Value': 'Devops'
                    },
                    {
                        'Key': 'Environment',
                        'Value': 'QA'
                    },

                ]
            },
        ],
    )	


# Terminate instance on conditions

instances = client.describe_instances()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
                                
            # Convert list to a dict
            tags = {c['Key']:c['Value']  for c in instance['Tags']}
            if (tags['Name'] == "Javier") and (tags['Environment'] == "QA") and (tags['Team'] == "Devops"):
                    pprint('Instancias:', instance['InstanceId'])
                    instanceId = instance['InstanceId']                  

                    print(instanceId)
                    raw_input("eliminar instancia?")
                    #response = client.terminate_instances(InstanceIds=[instanceId])                                                                  
                    #print(response)
                    sys.exit()
   


if __name__ == '__main__':
    main()
