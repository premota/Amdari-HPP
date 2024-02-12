from setuptools import find_packages, setup
from typing import List

editable = "-e ."
def find_requirements(file_path: str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if editable in requirements:
            requirements.remove(editable)



setup(
    name = "House price prediction",
    version = "0.1",
    author = "precious",
    author_email = "",
    packages = find_packages(),
    install_require = find_requirements("requirements.txt")
)