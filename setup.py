#!/usr/bin/python

from distutils.core import setup

name = 'keycloak-httpd-client-install'

setup(name=name,
      version='0.8',
      description='Tools to configure Apache HTTPD as Keycloak client',
      author='John Dennis',
      author_email='jdennis@redhat.com',
      url='https://github.com/jdennis/keycloak-httpd-client-install',
      license='GPLv3',
      packages = ['keycloak_httpd_client'],
      scripts = ['bin/keycloak-httpd-client-install'],
      data_files = [('/usr/share/{name}/templates'.format(name=name),
                     ['templates/mellon_httpd.conf',
                      'templates/sp_metadata.tpl'])],
      requires = ['requests', 'requests_oauthlib', 'jinja2'],
      classifiers = [           # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: POSIX",
      ],
     )
