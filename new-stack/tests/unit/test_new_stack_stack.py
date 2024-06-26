import aws_cdk as core
import aws_cdk.assertions as assertions

from new_stack.new_stack_stack import NewStackStack
from new_stack.network_stack import NetworkStack

def test_network_stack_resource_counts():
    app = core.App()
    
    root_stack = core.Stack(app, 'RootStack')

    network_stack = NetworkStack(root_stack, 'NetworkStack')

    template = assertions.Template.from_stack(network_stack)
    
    template.resource_count_is('AWS::EC2::VPC', 1)
    template.resource_count_is('AWS::EC2::NatGateway', 0)

    application_stack = NewStackStack(root_stack, "NewStackStack", my_vpc=network_stack.vpc)

def test_application_stack_web_server():

    app = core.App()
    
    root_stack = core.Stack(app, 'RootStack')

    network_stack = NetworkStack(root_stack, 'NetworkStack')
    application_stack = NewStackStack(root_stack, "NewStackStack", my_vpc=network_stack.vpc)

    template = assertions.Template.from_stack(application_stack)
    
    template.has_resource_properties('AWS::EC2::Instance', {
        'InstanceType': 't3.micro',
        'ImageId': assertions.Match.any_value(),
        'KeyName': assertions.Match.any_value(),
        'Custom': assertions.Match.absent()
    })
