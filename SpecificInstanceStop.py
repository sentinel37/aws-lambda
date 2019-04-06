import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

     response=ec2.describe_instances()

     for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            id="i-0e6a7b2841c1baaf6","i-066a1bd1440d0d535"

            if instance["State"]["Name"]=="running":

                ec2.stop_instances(InstanceIds=id)