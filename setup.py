from setuptools import setup

install_requires = open("requirements.txt").read().strip().split("\n")

setup(
    name="example_project",
    version="0.0.1",
    description="A demonstration of Prefect flow registration with modules",
    author="Michael Adkins",
    author_email="michael@prefect.io",
    packages=["example_project"],
    install_requires=install_requires,
)

