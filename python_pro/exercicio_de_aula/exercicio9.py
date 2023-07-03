from troposphere import Base64, FindInMap, GetAtt, Join
from troposphere import Output, Parameter, Ref, Template
from troposphere.ec2 import Instance, NetworkInterfaceProperty, SecurityGroup
from troposphere.ec2 import SecurityGroupRule

t = Template()

sg = t.add_resource(SecurityGroup(
    "MySecurityGroup",
    GroupDescription="Allow SSH and ICMP traffic",
    SecurityGroupIngress=[
        SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        ),
        SecurityGroupRule(
            IpProtocol="icmp",
            FromPort="8",
            ToPort="-1",
            CidrIp="0.0.0.0/0",
        ),
    ],
))

instance = t.add_resource(Instance(
    "MyInstance",
    ImageId="ami-0c55b159cbfafe1f0",
    InstanceType="t2.micro",
    KeyName="mykeypair",
    NetworkInterfaces=[
        NetworkInterfaceProperty(
            GroupSet=[Ref(sg)],
            AssociatePublicIpAddress="true",
            DeviceIndex="0",
            DeleteOnTermination="true",
            SubnetId="subnet-abcde012",
        ),
    ],
))

print(t.to_yaml())