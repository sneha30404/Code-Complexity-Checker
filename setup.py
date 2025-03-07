# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pathlib

# Read README.md
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='code-complexity-checker',  
    version='0.1.4',  
    packages=find_packages(),
    install_requires=[
        'radon>=5.1.0',  
    ],
    entry_points={
        'console_scripts': [
            'code-checker=checker.complexity:main',  
        ],
    },
    author='Sneha',
    author_email='sneha30404@gmail.com',
    description='A simple Python tool to calculate code complexity.',
    long_description=README,  
    long_description_content_type='text/markdown',
    url='https://github.com/sneha30404/code-complexity-checker',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
