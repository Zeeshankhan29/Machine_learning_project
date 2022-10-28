from pkg_resources import Requirement
from setuptools import setup,find_packages
from typing import List



#Declaring variables for setup functions
PROJECT_NAME="housing-prediction",
VERSION="0.0.2",
AUTHOR="Zeeshan Khan",
DESCRIPTION ='This is the House price prediction project',
PACKAGES=["Housing"],
REQUIREMENT_FILE_NAME ="requirements.txt"





def get_requirements_list()->List[str]:
    '''
    this functions returns the list of libraries what we have mentioned in requirements.txt file
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

    setup(
        name =PROJECT_NAME,
        version=VERSION,
        author=AUTHOR,
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires = get_requirements_list())

# if __name__=="__main__":
#     print(get_requirements_list())
