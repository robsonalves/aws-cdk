import jsii
from aws_cdk import(
    IAspect,
    Stack,
    Annotations,
    aws_ec2 as ec2
)


@jsii.implements(IAspect)
class EC2InstanceTypeChecker:
    def visit(self, node):

        if isinstance(node, ec2.CfnInstance):
            if node.instance_type not in ['t2.micro', 't3.micro']:
                Annotations.of(node).add_warning(f'{node.instance_type} instance type is invalid.')

                node.instance_type = 't2.micro'

@jsii.implements(IAspect)
class SSHAnywhereChecker:
    def visit(self, node):
        if isinstance(node, ec2.CfnSecurityGroup):
            rules = Stack.of(node).resolve(node.security_group_ingress)

            for rule in rules:
                if rule['ipProtocol'] == 'tcp' and rule['fromPort'] <= 22 and rule ['toPort'] >= 22:
                    Annotations.of(node).add_error('SSH from anywhere is not allowed!')