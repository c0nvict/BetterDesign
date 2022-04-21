import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="BetterDesign",
    version="2.0.0",
    description="Used to make your design of terminal apps easier!",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="convict",
    license="MIT",
    packages=find_packages(),
    install_requires=None,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    project_urls={'GitHub': 'https://github.com/c0nvict/BetterDesign'}
)
