from setuptools import setup, find_packages

setup(
    name='code-complexity-checker',  
    version='0.1.0',  
    packages=find_packages(),
    install_requires=[
        'radon>=5.1.0',  
    ],
    entry_points={
        'console_scripts': [
            'code-checker=checker.complexity:main',  
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple Python tool to calculate code complexity.',
    url='https://github.com/sneha30404/code-complexity-checker',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
