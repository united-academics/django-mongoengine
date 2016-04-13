"""
Django-MongoEngine
------------------

Django support for MongoDB using MongoEngine.

Links
`````

* `development version
  <https://github.com/MongoEngine/django-mongoengine/raw/master#egg=Django-MongoEngine-dev>`_

"""
from setuptools import setup, find_packages
import sys, os


__version__ = '0.2.1.ua.2'
__description__ = 'Django support for MongoDB via MongoEngine',
__license__ = 'BSD'
__author__ = 'Ross Lawley',
__email__ = 'ross.lawley@gmail.com',
__maintainer__ = 'Sergiu Zaharie',
__maintainer_email__ = 'zahariesergiu@gmail.com'

sys.path.insert(0, os.path.dirname(__file__))


REQUIRES = [i.strip() for i in open("requirements.txt").readlines()]


setup(
    name='django-mongoengine',
    version=__version__,
    url='https://github.com/united-academics/django-mongoengine',
    download_url='https://github.com/united-academics/django-mongoengine/tarball/master',
    license=__license__,
    author=__author__,
    author_email=__email__,
    maintainer = __maintainer__,
    maintainer_email = __maintainer_email__,
    description=__description__,
    long_description=__doc__,
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRES,
    packages=find_packages(exclude=('doc', 'docs',)),
    include_package_data=True,
    # use python setup.py nosetests to test
    setup_requires=['nose', 'coverage'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django'
    ]
)
