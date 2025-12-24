from setuptools import setup

setup(
    name="LogAnalyzer",
    version="1.0.0",
    description="A lightweight tool to analyze SSH brute force attacks.",
    author="Cheetahh1",
    py_modules=["analyzer", "cli"],  
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'log-check=cli:main',  #  creates a command 'log-check'
        ],
    },
)