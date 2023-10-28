from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()  
      
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pvlib',
    version='1.0',
    author='Danila Valko',
    author_email='d.v.valko@gmail.com',
    description="Some tools for Photovoltaic equipment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ellariel/pvlib',
    license='MIT',
    include_package_data=True,
    package_data={'pvlib': ['pvlib/*.py']},
    packages=['pvlib'],
    install_requires=required,
)
