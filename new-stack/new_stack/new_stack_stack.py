from aws_cdk import (
    CfnOutput,
    NestedStack,
    aws_ec2 as ec2,
    aws_s3_assets as s3
)
from constructs import Construct

class NewStackStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, my_vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        web_server = ec2.Instance(self, 'WebServer',
                                  machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                  instance_type=ec2.InstanceType.of(instance_class=ec2.InstanceClass.T3,
                                                                    instance_size=ec2.InstanceSize.MICRO),
                                  vpc=my_vpc,
                                  vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                                  user_data_causes_replacement=True)

        #Attaching an Elastic IP to keep the DNS name on Updates
        ec2.CfnEIP(self, 'ElasticIP',
                   instance_id=web_server.instance_id)

        web_server.add_user_data('yum updaete -y',
                                 'amazon-linux-extras install nginx1',
                                 'rm -rf /usr/share/nginx/html/*')

        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), 'Allow HTTP access from the Internet')
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(22), 'Allow SSH access from the Internet')

        CfnOutput(self, 'WebServerDnsName',
                  value=web_server.instance_public_dns_name)


        # Deploying a web page to the web server

        web_page_asset = s3.Asset(self, 'WebPageAsset',
                                  path='web_pages/index.html')
        web_server.user_data.add_s3_download_command(bucket=web_page_asset.bucket,
                                                     bucket_key=web_page_asset.s3_object_key,
                                                     local_file='/usr/share/nginx/html/index.html')
        web_page_asset.grant_read(web_server.role)
        web_server.add_user_data('service nginx start')

        web_page_asset = s3.Asset(self, 'WebImageAsset',
                            path='web_pages/image.png')