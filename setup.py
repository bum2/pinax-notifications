import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Developers",
    author_email="developers@pinaxprojects.com",
    description="User notification management for the Django web framework",
    name="pinax-notifications",
    long_description=read("README.rst"),
    version="2.0.0",
    url="http://pinax-notifications.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.notifications": [
            "locale/**/**/*",
            "templates/**/*.html"
        ]
    },
    install_requires=[
        "django-user-accounts>=1.0.1"
    ],
    test_suite="runtests.runtests",
    tests_require=[
        "django-user-accounts>=1.0.1"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
