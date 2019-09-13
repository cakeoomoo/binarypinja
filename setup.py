from setuptools import find_packages, setup

setup(
    name='pinja',
    packages=find_packages(),
    version='0.1.0',
    entry_points={  
        'console_scripts':  
            'pinja = pinja.main:main'  
    },  
    description='A short description of the project.',
    author='*pinja_sec',
    license='BSD-3',
)

