#!/usr/bin/env python

import distutils.core
import sys

# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

version = "0.1"

distutils.core.setup(
    name="splunktornado",
    version=version,
    packages = ["splunktornado"],
    author="Carl S. Yestrau Jr.",
    author_email="spam@featureblend.com",
    url="http://github.com/docyes/splunk_tornado",
    download_url="http://github.com/downloads/docyes/splunktornado/splunktornado-%s.tar.gz" % version,
    description="Implementation of Splunk authentication scheme for Tornado"
)
