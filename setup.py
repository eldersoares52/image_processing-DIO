from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ess",
    version="0.0.1",
    author="Elder",
    author_email="elder.soares52@gmail.com",
    description="Package for image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eldersoares52/image_processing-DIO.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)