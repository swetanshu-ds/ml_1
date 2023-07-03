from setuptools import setup
from typing import List, Dict



PROJECT_NAMe= "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "SWETANSHU_PANDEY"
DESCRIPTION = "THIS"
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name = PROJECT_NAMe,
    version= VERSION,
    author = AUTHOR,
    description= DESCRIPTION,
    install_requires = get_requirements_list()
)

