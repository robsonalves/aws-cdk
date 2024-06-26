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