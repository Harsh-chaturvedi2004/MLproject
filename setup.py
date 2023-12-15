from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT_E = '-e .'
def get_requirements(file_path:str)->List[str]:#This function will return the list of requirements
    requirements=[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        [req.replace("\n","")for req in requirements]#to tackle change in lines
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Harsh',
    author_email='harsh.chats04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
