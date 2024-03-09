"""
Setup file
"""
from setuptools import setup, find_packages

setup(
    name='project',
    version='0.0.1',
    description='description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='author',
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "langchain",
        "openai",
        "uvicorn",
        "pylint",
        "streamlit"
    ],
)
