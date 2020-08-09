from setuptools import setup
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

setup(
    name='backend-test',
    version='1.0.0',
    author='Noah Alex',
    author_email='noahcalex@gmail.com',
    license='None',
    packages=['backend-test', 'scraper', 'reviews', 'dictionary'],
    py_modules=['scraper', 'top_three', 'dictionary'],
    long_description=open(os.path.join(__location__, 'README.md'), 'r'),
    install_requires=['bs4', 'requests']
)