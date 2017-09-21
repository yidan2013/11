
# coding: utf-8


#!/usr/bin/env python
from setuptools import setup

#import sys
import versioneer



DISTNAME = 'FWmarket'
DESCRIPTION = "Market Analysis Package"
LONG_DESCRIPTION = """NA"""
MAINTAINER = 'Finweavers Inc'
AUTHOR = 'Finweavers Inc'
AUTHOR_EMAIL = 'NA'
URL = "https://github.com/FinWeavers/FWmarket"
LICENSE = "NA"

#VERSION = "0.0.10"


packages = ['FWmarket']
package_data={'FWmarket': ['*']}

classifiers = ['Development Status :: 4 - Beta',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Intended Audience :: Science/Research',
               'Topic :: Scientific/Engineering :: Mathematics',
               'Operating System :: OS Independent']

install_reqs = [
    'ipython>=3.2.3',
    'numpy>=1.8.0',
    'pandas>=0.18.0, <0.20.0',
    'scipy>=0.17.0',
    'configparser>=3.0.0',
    'python-dateutil>=2.6.0',
    'pydatastream>=0.4.6',
    'pymssql>=2.1.3',
    'sqlalchemy>=1.0.17'
#    'versioneer>=0.18'
]



if __name__ == "__main__":
    
    setup(
        name=DISTNAME,
#        version=VERSION,
#       Versioneer
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
#    
        maintainer=MAINTAINER,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        long_description=LONG_DESCRIPTION,
        packages=packages,
        package_data=package_data,
        classifiers=classifiers,
        install_requires=install_reqs
    )

