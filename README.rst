===============
pyephem_sunpath
===============


.. image:: https://img.shields.io/pypi/v/pyephem_sunpath.svg
        :target: https://pypi.python.org/pypi/pyephem_sunpath

.. image:: https://img.shields.io/travis/santoshphilip/pyephem_sunpath.svg
        :target: https://travis-ci.org/santoshphilip/pyephem_sunpath

.. image:: https://readthedocs.org/projects/pyephem-sunpath/badge/?version=latest
        :target: https://pyephem-sunpath.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/santoshphilip/pyephem_sunpath/shield.svg
     :target: https://pyup.io/repos/github/santoshphilip/pyephem_sunpath/
     :alt: Updates



Calculate sunpath using pyephem


* Free software: GNU General Public License v3
* Documentation: https://pyephem-sunpath.readthedocs.io.

Introduction
------------

**Pyephem_sunpath** is built upon pyephem_ an astronomical computation package. From the pyephem_ website we have:

    "**PyEphem** provides basic astronomical computations for the Python programming language. Given a date and location on the Earth’s surface, it can compute the positions of the Sun and Moon, of the planets and their moons, and of any asteroids, comets, or earth satellites whose orbital elements the user can provide. Additional functions are provided to compute the angular separation between two objects in the sky, to determine the constellation in which an object lies, and to find the times at which an object rises, transits, and sets on a particular day."

Pyephem_sunpath uses the a small part of pyephem to calculate the sun position and sun path for any location on earth. The big advantage of using pyephem, is that we will get a high degree of accuracy in the calculations.

Features
--------

- The function **sunposUTC()** calculates the sun position (in altitude and azimuth) using the UTC time.
- TODO: decimal2degreeminute(), degreeminute2decimal()

Credits
-------

Pyephem_sunpath is built upon pyephem_ an awesome astronomical package

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _pyephem: http://rhodesmill.org/pyephem/index.html
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
