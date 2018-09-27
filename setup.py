from setuptools import setup, find_packages


setup(
    name='globus-identifiers-client', version='0.1.0',
    description='Globus Identifiers Service Client Command',
    include_package_data=True,
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            ('globus-identifiers-client = identifiers_client:main')
        ]
    }
)
