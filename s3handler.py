import json
from pathlib import Path

import boto3
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError


class S3Handler:
    """
    This class handles all the S3 interaction.
    """

    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.bucket = config['bucketName']
            self.client = boto3.client(
                's3',
                aws_access_key_id=config['accessKeyID'],
                aws_secret_access_key=config['secreteAccessKey'],
            )

    def upload_file(self, upload_path, file_path):
        object_name = Path(upload_path) / Path(file_path).name
        try:
            self.client.upload_file(
                file_path, self.bucket, object_name.as_posix())
        except S3UploadFailedError as e:
            click.echo(e, err=True)
            return False
        return True

    def download_file(self, path):
        object_path = Path(path)
        try:
            self.client.download_file(
                self.bucket, object_path.as_posix(), object_path.name)
        except ClientError as e:
            click.echo(e, err=True)
            return False
        return True
