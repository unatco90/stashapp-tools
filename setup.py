import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="stashapp-tools",
    version="v0.2.22",
    description="A python library for interfacing with a stashapp's API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/unatco90/stashapp-tools",
    author="unatco90",
    author_email="99694038+unatco90@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["stashapi"],
    include_package_data=True,
    install_requires=["requests"],
)