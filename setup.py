#!/usr/bin/env python
"""Distribution Utilities setup program for Online CA Client Package

Contrail Project
"""
__author__ = "P J Kershaw"
__date__ = "21/05/10"
__copyright__ = "(C) 2010 Science and Technology Facilities Council"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id: $'

# Bootstrap setuptools if necessary.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name =            	'ContrailOnlineCAClient',
    version =         	'0.1.0',
    description =     	'Certificate Authority Web Service',
    long_description = 	'''\
Provides the client interface for an online Certificate Authority web-service.
This package works with the ``ContrailOnlineCAService`` the server-side 
implementation also available from PyPI.

The interface is implemented as a WSGI application which fronts a Certificate
Authority.  Web service call can be made to request a certificate.  The web 
service interface is RESTful using GET and POST operations.  The service 
should be hosted over HTTPS.  On the server-side, client authentication is 
configurable to the required means.  This client uses  HTTP Basic Auth to pass 
username and pass-phrase credentials

Client scripts are available which need no specialised installation or 
applications, only openssl and wget or curl which are typically available on 
Linux/UNIX based systems.

The code has been developed for the Contrail Project, http://contrail-project.eu/

Prerequisites
=============
This has been developed and tested for Python 2.6 and 2.7.

Installation
============
Installation can be performed using easy_install or pip.

Configuration
=============
Examples are contained in ``onlineca.client.test``.
''',
    author =          	'Philip Kershaw',
    author_email =    	'Philip.Kershaw@stfc.ac.uk',
    maintainer =        'Philip Kershaw',
    maintainer_email =  'Philip.Kershaw@stfc.ac.uk',
#    url =             	'',
    platforms =         ['POSIX', 'Linux', 'Windows'],
    install_requires =  ['ndg_httpsclient'],
    license =           __license__,
    test_suite =        'contrail.security.onlineca.client.test',
    packages =          find_packages(),
    package_data =      {
        'contrail.security.onlineca.client.test': [
            '*.cfg', '*.crt', '*.key', '*.pem', 'ca/*.0'
        ],
        'contrail.security.onlineca.client.sh': [
            '*.sh'
        ],
        'contrail.security.onlineca.client': [
            'README'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe = False
)
