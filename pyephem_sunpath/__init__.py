# -*- coding: utf-8 -*-

"""Top-level package for pyephem_sunpath."""

from importlib.metadata import version, PackageNotFoundError

__author__ = """Santosh Philip"""
__email__ = 'santosh_philip@notemail.com'

try:
    __version__ = version("pyephem_sunpath")   # must match [project] name =
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"                   # fallback for editable installs / dev

