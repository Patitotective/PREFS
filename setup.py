from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='PREFS',
  version='0.0.85',
  description='A simple program that creates, read and write prefs',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Patitotective/PREFS',  
  author='Cristobal Riaga',
  author_email='cristobalriaga@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='prefs', 
  packages=find_packages(),
  install_requires=[''], 

  long_description_content_type='text/markdown'
)