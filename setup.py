from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyHashKit",
    version="0.1.0",
    author="fmasterpro27",
    description="A modern Python toolkit for file hashing, checksum generation, verification, and integrity checking.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fmasterpro27/PyHashKit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],  # hashing.py only uses standard library 'hashlib'
    extras_require={
        "test": ["pytest"],
    },
)
