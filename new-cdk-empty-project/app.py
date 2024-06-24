#!/usr/bin/env python3
import os

import aws_cdk as cdk

from new_cdk_empty_project.new_cdk_empty_project_stack import NewCdkEmptyProjectStack


app = cdk.App()
NewCdkEmptyProjectStack(app, "NewCdkEmptyProjectStack")

app.synth()
