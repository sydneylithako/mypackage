from setuptools import setup, find_packages

setup(
name= 'my package',
version= '0.1',
packages= find_packages(exclude=['tests*']),
license= 'MIT',
description= 'EDSA example python package',
long_description= open('README.md').read(),
instal_requires=['NUMPY'],
url='https://github.com/<username>/<package.name>',
author= '<Your Name>',
author_email= '<Your Email>'
)