from distutils.core import setup

url="https://github.com/Akaame/interval"
version = "0.1.0"

setup(name="Interval",
version=version,
description="Interval tree implementation in Python.",
author="Siddik Acil",
url=url,
download_url=url+"/archive/"+version+".tar.gz", # There will be a download_url here
author_email="sddkacil.1@gmail.com", 
packages=["."]
)

# To get a download_url ->
# Steps: 
# git tag 0.1.0 -m "Add a tag for PyPI"
# git push --tags origin master