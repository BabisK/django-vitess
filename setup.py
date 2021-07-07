from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-vitess",
    version="0.0.2",
    description="Custom database driver for Vitess.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Babis Kaidos",
    author_email="ckaidos@intracom-telecom.com",
    url="https://github.com/BabisK/django-vitess",
    packages=find_packages(),
    install_requires=[
        "Django>=2.2"
    ],
    license="Apache Software License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Database"
    ]
)
