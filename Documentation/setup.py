from setuptools import setup, find_packages

setup(
    name="meta_analysis",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    author="Martin Adamčík",
    author_email="maths38@gmail.com",
    description="A package for meta-analysis of studies with complex knowledge and unexplained heterogeneity",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maths38/meta-analysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
