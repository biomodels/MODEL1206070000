from setuptools import setup, find_packages

setup(name='MODEL1206070000',
      version=20140916,
      description='MODEL1206070000 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/MODEL1206070000',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )