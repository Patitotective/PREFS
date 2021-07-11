from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Intended Audience :: Developers",
  "Natural Language :: English",  
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "Operating System :: MacOS :: MacOS X",
  "Operating System :: POSIX :: Linux",  
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.6", 
  "Programming Language :: Python :: 3.7", 
  "Programming Language :: Python :: 3.8", 
  "Programming Language :: Python :: 3.9", 
  "Topic :: Software Development :: Libraries :: Python Modules", 
]
 
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "docs/README.md"), encoding="utf-8") as f:
    long_description = f.read()

github_url = "https://github.com/Patitotective/PREFS"

setup(
  name="PREFS",
  version="0.1.1",
  author="Cristobal Riaga",
  author_email="cristobalriaga@gmail.com",
  maintainer="Cristobal Riaga", 
  maintainer_email="cristobalriaga@gmail.com",
  url=github_url,  
  project_urls={
    "Documentation": f'{github_url}/wiki', 
    'Source Code': github_url,
    'Changelog': f'{github_url}/blob/main/docs/CHANGELOG.md',
    'Issues': f'{github_url}/issues'
  },
  description="A simple but useful python library that helps you to manage user preferences",
  long_description=open("docs/README.md").read(),
  download_url="https://github.com/Patitotective/PREFS", 
  classifiers=classifiers,
  platforms= ["Windows", "Linux", "MacOS"],
  keywords=["prefs", "preferences"],  
  license="MIT", 
  packages=find_packages(),
  install_requires=["pypistats"], 

  long_description_content_type="text/markdown"
)
