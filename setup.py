from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Sankalp",
    author_email="sankalpupadhyay2702@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)

