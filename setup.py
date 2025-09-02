from setuptools import setup, find_packages

setup(
    name='myweather_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.3.2',
        'numpy>=2.3.2'
    ],
    author='Corbin',
    description='Canadian weather CSV statistics utilities',
    url='https://github.com/PhysicistsOfDoom/CS3270',
)