from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PREFS',
  version='0.0.45',
  description='A simple program that creates, read and write prefs',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Cristobal Riaga',
  author_email='cristobalriaga@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='prefs', 
  packages=find_packages(),
  install_requires=[''] 
)