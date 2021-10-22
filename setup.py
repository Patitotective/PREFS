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
 
with open("README.md", "r") as file:
  long_description = file.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

github_url = "https://github.com/Patitotective/PREFS"

setup(
  name="PREFS",
  version="0.2.60",
  author="Cristobal Riaga",
  author_email="cristobalriaga@gmail.com",
  maintainer="Cristobal Riaga", 
  maintainer_email="cristobalriaga@gmail.com",
  url=github_url,  
  project_urls={
    "Website": "https://patitotective.github.io/PREFS/", 
    "Documentation": 'https://patitotective.github.io/PREFS/docs', 
    'Source code': github_url,
    'Changelog': f'{github_url}/blob/main/CHANGELOG.md',
    'Issues': f'{github_url}/issues', 
    'Pull requests': f'{github_url}/pulls', 
    'Discord server': "https://discord.gg/as85Q4GnR6"
  },
  description="Python library that helps you to store and manage user preferences and settings.",
  long_description=open("README.md").read(),
  classifiers=classifiers,
  platforms= ["Windows", "Linux", "MacOS"],
  keywords=["prefs", "preferences", "settings"],  
  license="MIT", 
  packages=find_packages(),
  install_requires=requirements, 
  entry_points={
    "console_scripts": [
      "PREFS = PREFS.__main__:main"
    ]
  }, 

  long_description_content_type="text/markdown"
)
