from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class NewStackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        my_vpc = ec2.Vpc(self, 'MyVpc', nat_gateways=0)
        web_server = ec2.Instance(self, 'WebServer',
                                  machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                  instance_type=ec2.InstanceType.of(instance_class=ec2.InstanceClass.T2,
                                                                    instance_size=ec2.InstanceSize.MICRO),
                                  vpc=my_vpc,
                                  vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                                  user_data_causes_replacement=True)

        #Attaching an Elastic IP to keep the DNS name on Updates
        ec2.CfnEIP(self, 'ElasticIP',
                   instance_id=web_server.instance_id)

        web_server.add_user_data('yum updaete -y',
                                 'amazon-linux-extras install nginx1',
                                 'service nginx start')

        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), 'Allow HTTP access from the Internet')

        CfnOutput(self, 'WebServerDnsName',
                  value=web_server.instance_public_dns_name)