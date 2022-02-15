from setuptools import setup, find_packages
from pathlib import Path

with open('requirements.txt', 'r') as f:
    dependencies = [l.strip() for l in f]

setup(
   name='tunnelboard',
   version='0.1.0',
   author='Utkarsh Giri',
   author_email='utkarshgiri18@gmail.com',
   packages=['tunnelboard'],
   scripts = [x.as_posix() for x in list(Path('tunnelboard').glob('*'))],
   description='Script to automate remote tensorboard run',
   install_requires=dependencies,
)
