from setuptools import setup

name = '{{cookiecutter.project_name}}'

setup(
    name=name,
    version='0.1',
    author='ktpr1223',
    # packagesは指定する必要あり
    packages=['src', 'src.preprocess'])
