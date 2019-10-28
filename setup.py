from setuptools import setup


setup(
    name="UpDwn",
    version="1.0",
    py_modules=['updwn'],
    install_requires=['Click'],
    entry_points={'console_scripts': 'updwn=updwn:main'}
)
