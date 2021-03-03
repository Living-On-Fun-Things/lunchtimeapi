from . import AWSObject, AWSProperty, Tags
from .validators import json_checker
from .compat import policytypes


class LifecyclePolicy(AWSProperty):
    props = {
        'LifecyclePolicyText': (str, False),
        'RegistryId': (str, False),
    }


class Repository(AWSObject):
    resource_type = "AWS::ECR::Repository"

    props = {
        'ImageScanningConfiguration': (dict, False),
        'ImageTagMutability': (str, False),
        'LifecyclePolicy': (LifecyclePolicy, False),
        'RepositoryName': (str, False),
        'RepositoryPolicyText': (policytypes, False),
        'Tags': (Tags, False),
    }
