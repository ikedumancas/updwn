from setuptools import setup


setup(
    name="UpDwn",
    version="1.0",
    packages=['updwn'],
    install_requires=['Click', 'boto3'],
    entry_points={'console_scripts': 'updwn=updwn.updwn:main'}
)
