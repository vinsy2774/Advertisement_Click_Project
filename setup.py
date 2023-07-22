from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'
def get_requirements(filepath):
    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='AdClick',
    version='0.0.1',
    author='vinsy',
    author_email='vinsy2774@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)