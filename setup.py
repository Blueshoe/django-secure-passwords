# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = (
    "django-secure-passwords is a package that adds more password validation options as "
    "often required in large corporations"
)


setup(
    name="django-secure-passwords",
    description=DESCRIPTION,
    version=VERSION,
    install_requires=[
        "Django>=2.2",
    ],
    python_requires="~=3.8",
    packages=[
        "securepasswords",
        "securepasswords.migrations",
    ],
    author="Veit Rückert",
    author_email="veit@blueshoe.de",
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1" "",
        "Programming Language :: Python :: 3.8",
    ],
)
