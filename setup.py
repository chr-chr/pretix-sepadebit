import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-sepadebit',
    version='2.0.1',
    description='This plugin adds SEPA direct debit support to pretix',
    long_description=long_description,
    url='https://github.com/pretix/pretix-sepadebit',
    author='Raphael Michel',
    author_email='mail@raphaelmichel.de',
    license='Apache Software License',

    install_requires=['django-localflavor', 'sepaxml>=2.4.1'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_sepadebit=pretix_sepadebit:PretixPluginMeta
""",
)
