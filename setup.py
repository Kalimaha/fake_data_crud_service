from setuptools import setup
from setuptools import find_packages

setup(
    name='TestDataCRUDServices',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    description='Simple CRUD services for test data.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors', 'gunicorn', 'pymongo'
    ],
    url='http://pypi.python.org/pypi/TestDataCRUDServices/'
)