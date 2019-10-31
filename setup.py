from setuptools import setup


setup(
    name="UpDwn",
    version="1.0",
    py_modules=['updwn'],
    install_requires=['Click', 'boto3'],
    entry_points={'console_scripts': 'updwn=updwn:main'}
)
