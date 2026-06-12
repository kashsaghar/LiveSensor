from setuptools import find_packages, setup
# from typing import List

#func returning a list of requirements
def get_requirements() -> list[str]:
    requirements_list: list[str] = []

    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Kashmala",
    packages=find_packages(), 
    install_requires= get_requirements()
    # [
    #     "pymongo"   
    # ]
)