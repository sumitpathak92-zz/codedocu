#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup


VERSION = '0.0.1'

ld = """
codedocu is an experimental code documentation system which currently supports python 2.7.1
Documenting your code is very necessary as far as understanding of the module in a webapp
is concerned. codedocu helps you by extracting the comments from within your code base, smartly 
mapping those to the respective modules and generating a meaningful documentation out of it.
"""

setup(name='codedocu',
      version='0.0.4',
      description='Documenting python code made easy!',
      url='http://github.com/sumitpathak92/codedocu',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          ],
      author='Sumit Pathak',
      author_email='pathaksumit92@gmail.com',
      license='MIT',
      package=['codedocu'],
      entry_points={
          'console_scripts': ['codedoc = codedocu.__init__:first',
                              'codedoc generate = codedocu.html_report1:main'
                              ],
          },
      include_package_data=True,
      zip_safe=False)
