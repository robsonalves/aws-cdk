import aws_cdk as core
import aws_cdk.assertions as assertions

from new_cdk_empty_project.new_cdk_empty_project_stack import NewCdkEmptyProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in new_cdk_empty_project/new_cdk_empty_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NewCdkEmptyProjectStack(app, "new-cdk-empty-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
