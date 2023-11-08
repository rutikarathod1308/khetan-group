from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in khetangroup/__init__.py
from khetangroup import __version__ as version

setup(
	name="khetangroup",
	version=version,
	description="khetangroup",
	author="khetan",
	author_email="khetan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

