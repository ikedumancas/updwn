# Assignment details: 

Create an application that has a CLI which can upload files to a particular path. You may use any language, library and service that you like. However, you cannot upload the file as a blob into a database. For example:

updwn --upload ‘some/path/here’ something.jpeg

The uploader must have a config.json file that has all the credentials required to upload this file to a blob storage service (like AWS S3 or Azure Blob Storage). You can get a free AWS S3 account as well as a free Azure account.

You must be able to download the file:

updwn –-download ‘some/path/here/something.jpeg’

The config.json should have the credentials to download the file as well. For extra credit, you can also implement a listing command, that lists all the files:

updwn --list

You should also be able to list all the command available via --help:
```
updwn --help

updwn --upload <upload path> <file path>
updwn --download <path>
updown --list
```

# Install Requirements
1. Python 3.x
2. pip

# How to Install for development:
1. Run the command below:
    > pip install --editable .