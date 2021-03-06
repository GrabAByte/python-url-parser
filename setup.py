import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-url-parser",
    version="0.1.2",
    description="A forked repository for testing Python CI and Release",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/GrabAByte/python-url-parser",
    author="GrabAByte",
    author_email="grababyte@github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["url-parser"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "grababyte=reader.__main__:main",
        ]
    },
)
