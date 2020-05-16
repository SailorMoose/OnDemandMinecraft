class Config:
    # AWS Information
    ec2_region = "eu-north-1"  # Same as environment variable EC2_REGION
    ec2_amis = ['ami-0d4e2b57f569e9daa']
    ec2_keypair = 'McOnDemand'
    ec2_secgroups = ['minecraft']
    ec2_instancetype = 't3.medium'
