#!/usr/bin/env python3
import os

import aws_cdk as cdk

from new_stack.new_stack_stack import NewStackStack
from new_stack.network_stack import NetworkStack


app = cdk.App()

root_stack = cdk.Stack(app, 'RootStack')

network_stack = NetworkStack(root_stack, 'NetworkStack')

application_stack = NewStackStack(root_stack, "NewStackStack", my_vpc=network_stack.vpc)


# Stack-Level tagging

cdk.Tags.of(network_stack).add('category', 'network')
cdk.Tags.of(application_stack).add('category', 'application',
                                   priority=200)

app.synth()
