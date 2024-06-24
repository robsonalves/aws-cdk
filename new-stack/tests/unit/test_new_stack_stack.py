import aws_cdk as core
import aws_cdk.assertions as assertions

from new_stack.new_stack_stack import NewStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in new_stack/new_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NewStackStack(app, "new-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
