# setup.py is responsible in creating ML application as a package

import setuptools
from typing import List

with open("README.md","r",encoding="utf-8") as f:
    long_description=  f.read()

__version__ = "0.0.0"
REPO_NAME = "deep-coccidiosis-detection"
AUTHOR_USER_NAME = "umairsiddique3171"
AUTHOR_EMAIL = "umairsiddique3171@gmail.com"
SRC_REPO = "cnnClassifier"

E_DOT = "-e ."

def get_requirements(filepath)->List[str]:
    requirements = []
    with open(filepath) as inst:
        requirements = inst.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    if E_DOT in requirements:
        requirements.remove(E_DOT)

    
setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Package for CNN Classfication App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')
)