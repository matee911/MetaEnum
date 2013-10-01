#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='MetaEnum',
      description='',
      keywords='',
      version='1.1',
      license='MIT',
      url='http://github.com/matee911/MetaEnum', # home page for the package
      download_url='http://github.com/matee911/MetaEnum/downloads',
      maintainer='Mateusz `matee` Pawlik',
      maintainer_email='matee@matee.net',
      long_description='''
      example of use:
      
      >>> from metaenum import MetaEnum
      >>> class FOO(MetaEnum):
      ...     BAZ = (0, 'bazik')
      ...     BAR = 1
      >>> FOO.BAZ
      0
      >>> FOO.BAR
      1
      >>> FOO.BAZ_name
      'BAZ'
      >>> FOO.BAZ_verbose
      'bazik'
      >>> FOO.get_verbose(FOO.BAZ)
      'bazik'
      >>> FOO.get_verbose(FOO.BAR)
      None
      >>> FOO.as_choices()
      [(0, 'bazik'), (1, None)]
      >>> FOO.by_name('BAZ')
      0
      >>> FOO.by_verbose('bazik')
      1
      ''',
      requires=[],
      #package_dir={'':'src'},
      py_modules=['metaenum'],
      platforms=['Any'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
      ],)
