from setuptools import setup, find_packages

setup(
    name='cmd',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gnfd-cmd = cmd.main:gnfd',
        ],
    },
)
