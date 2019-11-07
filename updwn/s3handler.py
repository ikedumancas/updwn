import json
import os
from pathlib import Path

import boto3
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError


CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')


class S3Handler:
    """
    This class handles all the S3 interaction.
    """

    def __init__(self):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            self.bucket_name = config['bucketName']
            self.list_max_items_per_page = config['listMaxItemsPerPage']
            self.client = boto3.client(
                's3',
                aws_access_key_id=config['accessKeyID'],
                aws_secret_access_key=config['secreteAccessKey'],
            )

    def upload_file(self, upload_path, file_path):
        object_name = Path(upload_path) / Path(file_path).name
        try:
            self.client.upload_file(
                file_path, self.bucket_name, object_name.as_posix())
        except S3UploadFailedError as e:
            return False, e
        return True, None

    def download_file(self, path):
        object_path = Path(path)
        try:
            self.client.download_file(
                self.bucket_name,
                object_path.as_posix(),
                object_path.name
            )
        except ClientError as e:
            return False, e
        return True, None

    def list_all_files(self, next_token=''):
        list_obj_kwargs = {
            'Bucket': self.bucket_name,
            'MaxKeys': self.list_max_items_per_page
        }
        if next_token:
            list_obj_kwargs['ContinuationToken'] = next_token
        try:
            response = self.client.list_objects_v2(**list_obj_kwargs)
        except ClientError as e:
            return False, e, {}
        result = {
            'contents': response['Contents'],
            'next_token': ''
        }
        if 'NextContinuationToken' in response:
            result['next_token'] = response['NextContinuationToken']
        return True, None, result
