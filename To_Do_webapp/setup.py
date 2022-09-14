from setuptools import find_packages,setup

setup(
    # directory name of the project
    name='flaskr',
    version='1.0.0',
    # finds the directorys
    packages=find_packages(),
    # includes other files (static, templates) 
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)