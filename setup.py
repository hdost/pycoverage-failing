#!/usr/bin/env python3
import setuptools
import os


def _read(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return f.read()


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return [s.strip() for s in f.readlines() if (s.strip() and not s.startswith("#"))]


_REQUIREMENTS_TXT = _read_reqs("requirements.txt")
_DEPENDENCY_LINKS = [elem for elem in _REQUIREMENTS_TXT if "://" in elem]
_INSTALL_REQUIRES = [elem for elem in _REQUIREMENTS_TXT if "://" not in elem]


setuptools.setup(
    name="testcoverage",
    version="0.1",
    maintainer="Harold Dost",
    maintainer_email="github@hdost.com",
    description="A way to test the coverage tooling",
    license="Apache 2.0 Software License",
    include_package_data=True,
    long_description=_read("README.md"),
    install_requires=_INSTALL_REQUIRES,
    dependency_links=_DEPENDENCY_LINKS,
    test_suite="tests",
    package_dir={
        "mod1": "scripts/mod1",
        "mod2": "scripts/mod2",
        # Make pip -e happy
        "": "scripts",
    },
    tests_require=_read_reqs("tests-requirements.txt"),
    packages=[
        "mod1",
        "mod2",
        "mod2.core",
    ],
)
