"""Setup module for ntuity."""
from pathlib import Path

from setuptools import setup

PROJECT_DIR = Path(__file__).parent
README_FILE = PROJECT_DIR / "README.md"
VERSION = "0.1.0"

setup(
    name="ntuity",
    version="VERSION",
    author="Tobias Lechenauer",
    author_email="tobiaslechenauer@gmail.com",
    description="Python wrapper for getting data from the Ntuity API",
    long_description=README_FILE.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/Lechtob/ntuity",
    license="Apache-2.0 License",
    packages=["ntuity"],
    package_data={"ntuity": ["py.typed"]},
    python_requires=">=3.11, <3.12",
    install_requires=["aiohttp>=3.9.1","orjson>=3.9.12"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",  
    ],   
)