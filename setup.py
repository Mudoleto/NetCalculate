import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.2'
PACKAGE_NAME = 'NetCalculate'
AUTHOR = 'Sergio Alberto Sandoval Garcia (Mudoleto)'
AUTHOR_EMAIL = 'sergio.sandoval83@hotmail.com'
URL = "https://github.com/Mudoleto"

LICENSE = 'MIT'
DESCRIPTION = 'This tool provides a quick and efficient solution for calculating the network ID and broadcast address of an IP address in binary format, along with the identification of the network class to which it belongs.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'termcolor'
    ]

setup(
    name = PACKAGE_NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = LONG_DESC_TYPE,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    install_requires = INSTALL_REQUIRES,
    license = LICENSE,
    packages = find_packages(),
    include_package_data = True
    )
