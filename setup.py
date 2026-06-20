from setuptools import setup, find_packages

setup(
    name="media_library",
    version="0.1.0",
    author="Joono1229",
    author_email="l01066083119@gmail.com",
    description="A Python package for managing a collection of books and movies.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joono1229/media_library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)