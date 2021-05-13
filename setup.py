# -*- coding: utf-8 -*-
import os

from setuptools import setup

base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "VERSION")) as f:
    VERSION = f.read()

with open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

DESCRIPTION = (
    "django-secure-passwords is a package that adds more password validation options as "
    "often required in large corporations"
)


setup(
    name="django-secure-passwords",
    description=DESCRIPTION,
    version=VERSION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "Django>=2.2",
    ],
    python_requires="~=3.6",
    packages=[
        "securepasswords",
        "securepasswords.migrations",
        "securepasswords.management",
        "securepasswords.management.commands",
    ],
    author="Veit Rückert",
    author_email="veit@blueshoe.de",
    include_package_data=True,
    package_data={"securepasswords": ["locale/*/LC_MESSAGES/*.mo"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1" "",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
