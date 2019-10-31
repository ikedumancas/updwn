import click

from s3handler import S3Handler


@click.command()
@click.option(
    '--upload',
    type=(click.Path(file_okay=False), click.Path(exists=True, dir_okay=False)),
    default=(None, None),
    metavar='<upload path> <file path>',
    help='Upload <file path> to server <upload path>'
)
@click.option(
    '--download',
    metavar='<path>',
    help='Download server <path> to current directory'
)
def main(upload, download):
    """
    This script can upload and download file to the server.
    """

    if upload == (None, None) and download is None:
        click.echo('Try "updwn --help" for help.', err=True)
        return

    handler = S3Handler()
    if upload != (None, None):
        upload_path, file_path = upload
        upload_to_root = upload_path == "''" or upload_path == "."
        click.echo("Uploading file %s to %s" % (
            file_path, upload_path if not upload_to_root else 'root directory'))

        success = handler.upload_file(upload_path, file_path)
        msg = "Upload success!!" if success else "Upload Failed :("
        click.echo(msg, err=not success)

    if download is not None:
        click.echo("Downloading file %s to current directory" % download)
        success = handler.download_file(download)
        msg = "Download success!!" if success else "Download Failed :("
        click.echo(msg, err=not success)
