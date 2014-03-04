from setuptools import setup, find_packages
from th_irc import __version__ as version
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

setup(
    name='django_th_evernote',
    version=version,
    description='This service provides a way to publish data on the IRC server and channel of your choice from and to the service of your choice',
    author='Olivier Demah',
    author_email='olivier@foxmask.info',
    url='https://github.com/foxmask/django-th-irc',
    download_url="https://github.com/foxmask/django-th-irc/archive/trigger-happy-irc-"
    + version + ".zip",
    packages=find_packages(exclude=['th_irc/local_settings']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
