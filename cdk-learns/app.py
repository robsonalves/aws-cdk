#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_learns.cdk_learns_stack import CdkLearnsStack


app = cdk.App()
CdkLearnsStack(app, "CdkLearnsStack")

app.synth()
