from setuptools import setup, find_packages


setup(
    name='globus-identifiers-client', version='0.1.0',
    description='Globus Identifiers Service Client Command',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "globus-sdk>=1.4.0",
        "six>=1.10.0,<2.0.0",
    ],
    entry_points={
        'console_scripts': [
            ('globus-identifiers-client = identifiers_client:main')
        ]
    }
)
