import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Flask-Foundation',
    version='1.4',
    url='http://github.com/brainfire/flask-foundation',
    license='BSD',
    author='Zakaria Zajac',
    author_email='zak@brainfi.re',
    description='An extension that includes the Foundation css framework in your '
                'project, without any boilerplate code.',
    long_description=read('README.md'),
    packages=['flask_foundation'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
