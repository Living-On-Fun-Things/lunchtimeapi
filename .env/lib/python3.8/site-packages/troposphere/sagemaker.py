# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class GitConfig(AWSProperty):
    props = {
        'Branch': (str, False),
        'RepositoryUrl': (str, True),
        'SecretArn': (str, False),
    }


class CodeRepository(AWSObject):
    resource_type = "AWS::SageMaker::CodeRepository"

    props = {
        'CodeRepositoryName': (str, False),
        'GitConfig': (GitConfig, True)
    }


class Endpoint(AWSObject):
    resource_type = "AWS::SageMaker::Endpoint"

    props = {
        'EndpointName': (str, False),
        'EndpointConfigName': (str, True),
        'Tags': (Tags, False)
    }


class CaptureContentTypeHeader(AWSProperty):
    props = {
        'CsvContentTypes': ([str], False),
        'JsonContentTypes': ([str], False),
    }


class CaptureOption(AWSProperty):
    props = {
        'CaptureMode': (str, True),
    }


class DataCaptureConfig(AWSProperty):
    props = {
        'CaptureContentTypeHeader': (CaptureContentTypeHeader, False),
        'CaptureOptions': ([CaptureOption], True),
        'DestinationS3Uri': (str, True),
        'EnableCapture': (boolean, False),
        'InitialSamplingPercentage': (integer, True),
        'KmsKeyId': (str, False),
    }


class ProductionVariant(AWSProperty):
    props = {
        'ModelName': (str, True),
        'VariantName': (str, True),
        'InitialInstanceCount': (integer, True),
        'InstanceType': (str, True),
        'InitialVariantWeight': (float, True)
    }


class EndpointConfig(AWSObject):
    resource_type = "AWS::SageMaker::EndpointConfig"

    props = {
        'DataCaptureConfig': (DataCaptureConfig, False),
        'EndpointConfigName': (str, False),
        'KmsKeyId': (str, False),
        'ProductionVariants': ([ProductionVariant], True),
        'Tags': (Tags, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (str, False),
        'Environment': (dict, False),
        'Mode': (str, False),
        'ModelDataUrl': (str, False),
        'Image': (str, True)
    }


class VpcConfig(AWSProperty):
    props = {
        'Subnets': ([str], True),
        'SecurityGroupIds': ([str], True)
    }


class Model(AWSObject):
    resource_type = "AWS::SageMaker::Model"

    props = {
        'Containers': ([ContainerDefinition], False),
        'ExecutionRoleArn': (str, True),
        'ModelName': (str, False),
        'PrimaryContainer': (ContainerDefinition, False),
        'Tags': (Tags, False),
        'VpcConfig': (VpcConfig, False),
    }


class MonitoringExecutionSummary(AWSProperty):
    props = {
        'CreationTime': (str, True),
        'EndpointName': (str, False),
        'FailureReason': (str, False),
        'LastModifiedTime': (str, True),
        'MonitoringExecutionStatus': (str, True),
        'MonitoringScheduleName': (str, True),
        'ProcessingJobArn': (str, False),
        'ScheduledTime': (str, True),
    }


class ConstraintsResource(AWSProperty):
    props = {
        'S3Uri': (str, False),
    }


class StatisticsResource(AWSProperty):
    props = {
        'S3Uri': (str, False),
    }


class BaselineConfig(AWSProperty):
    props = {
        'ConstraintsResource': (ConstraintsResource, False),
        'StatisticsResource': (StatisticsResource, False),
    }


class MonitoringAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([str], False),
        'ContainerEntrypoint': ([str], False),
        'ImageUri': (str, True),
        'PostAnalyticsProcessorSourceUri': (str, False),
        'RecordPreprocessorSourceUri': (str, False),
    }


class EndpointInput(AWSProperty):
    props = {
        'EndpointName': (str, True),
        'LocalPath': (str, True),
        'S3DataDistributionType': (str, False),
        'S3InputMode': (str, False),
    }


class MonitoringInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class MonitoringInputs(AWSProperty):
    props = {
        'MonitoringInputs': ([MonitoringInput], False),
    }


class S3Output(AWSProperty):
    props = {
        'LocalPath': (str, True),
        'S3UploadMode': (str, False),
        'S3Uri': (str, True),
    }


class MonitoringOutput(AWSProperty):
    props = {
        'S3Output': (S3Output, True),
    }


class MonitoringOutputConfig(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'MonitoringOutputs': ([MonitoringOutput], True),
    }


class ClusterConfig(AWSProperty):
    props = {
        'InstanceCount': (integer, True),
        'InstanceType': (str, True),
        'VolumeKmsKeyId': (str, False),
        'VolumeSizeInGB': (integer, True),
    }


class MonitoringResources(AWSProperty):
    props = {
        'ClusterConfig': (ClusterConfig, True),
    }


class NetworkConfig(AWSProperty):
    props = {
        'EnableInterContainerTrafficEncryption': (boolean, False),
        'EnableNetworkIsolation': (boolean, False),
        'VpcConfig': (VpcConfig, False),
    }


class StoppingCondition(AWSProperty):
    props = {
        'MaxRuntimeInSeconds': (integer, True),
    }


class MonitoringJobDefinition(AWSProperty):
    props = {
        'BaselineConfig': (BaselineConfig, False),
        'Environment': (dict, False),
        'MonitoringAppSpecification': (MonitoringAppSpecification, True),
        'MonitoringInputs': (MonitoringInputs, True),
        'MonitoringOutputConfig': (MonitoringOutputConfig, True),
        'MonitoringResources': (MonitoringResources, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
    }


class ScheduleConfig(AWSProperty):
    props = {
        'ScheduleExpression': (str, True),
    }


class MonitoringScheduleConfig(AWSProperty):
    props = {
        'MonitoringJobDefinition': (MonitoringJobDefinition, True),
        'ScheduleConfig': (ScheduleConfig, False),
    }


class MonitoringSchedule(AWSObject):
    resource_type = "AWS::SageMaker::MonitoringSchedule"

    props = {
        'CreationTime': (str, False),
        'EndpointName': (str, False),
        'FailureReason': (str, False),
        'LastModifiedTime': (str, False),
        'LastMonitoringExecutionSummary':
            (MonitoringExecutionSummary, False),
        'MonitoringScheduleArn': (str, False),
        'MonitoringScheduleConfig': (MonitoringScheduleConfig, True),
        'MonitoringScheduleName': (str, True),
        'MonitoringScheduleStatus': (str, False),
        'Tags': (Tags, False),
    }


class NotebookInstanceLifecycleHook(AWSProperty):
    props = {
        'Content': (str, False)
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props = {
        'NotebookInstanceLifecycleConfigName': (str, False),
        'OnCreate': ([NotebookInstanceLifecycleHook], False),
        'OnStart': ([NotebookInstanceLifecycleHook], False)
    }


class NotebookInstance(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstance"

    props = {
        'AcceleratorTypes': ([str], False),
        'AdditionalCodeRepositories': ([str], False),
        'DefaultCodeRepository': (str, False),
        'DirectInternetAccess': (str, False),
        'InstanceType': (str, True),
        'KmsKeyId': (str, False),
        'LifecycleConfigName': (str, False),
        'NotebookInstanceName': (str, False),
        'RoleArn': (str, True),
        'RootAccess': (str, False),
        'SecurityGroupIds': ([str], False),
        'SubnetId': (str, False),
        'Tags': (Tags, False),
        'VolumeSizeInGB': (integer, False),
    }


class CognitoMemberDefinition(AWSProperty):
    props = {
        'CognitoClientId': (str, True),
        'CognitoUserGroup': (str, True),
        'CognitoUserPool': (str, True),
    }


class MemberDefinition(AWSProperty):
    props = {
        'CognitoMemberDefinition': (CognitoMemberDefinition, True),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'NotificationTopicArn': (str, True),
    }


class Workteam(AWSObject):
    resource_type = "AWS::SageMaker::Workteam"

    props = {
        'Description': (str, False),
        'MemberDefinitions': ([MemberDefinition], False),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'Tags': (Tags, False),
        'WorkteamName': (str, False),
    }
