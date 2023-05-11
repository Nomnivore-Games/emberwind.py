from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["aiohttp>=3"]

setup(
    name="client.py",
    version="0.0.1",
    author="MimicByte",
    author_email="Aidan.MurphyCM@gmail.com",
    description="A Python wrapper for the Emberwind API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Nomnivore-Games/emberwind.py",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
