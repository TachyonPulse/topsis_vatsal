# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:44:47 2020

@author: Vikram
"""

from distutils.core import setup
setup(
  name = 'topsis_101703618',         # How you named your package folder (MyLib)
  packages = ['topsis_101703618'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package allows you to run topsis on your dataset for Multiple Attribute Decision Making(MADM)',   # Give a short description about your library
  author = 'Vikram',                   # Type in your name
  author_email = 'vsingh1_be17@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/vikramu9td/topsis',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vikramu9td/topsis/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'DATA ANALYSTICS', 'PS RANA'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
