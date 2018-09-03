# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in remove_help_tab/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('remove_help_tab/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='remove_help_tab',
	version=version,
	description='Remove Help Tab from top menu',
	author='Jazib Zaman',
	author_email='jazib@wparena.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
