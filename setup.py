from setuptools import setup

setup(
    name='Flask-DigestAuth',
    version='0.1.0',
    url='https://github.com/locojay/flask-digestauth',
    license='BSD',
    author='',
    author_email='',
    description='HTTP digest access authentication for Flask.',
    long_description=open('README.md').read(),
    packages=['flask_digestauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    # test_suite='test_basicauth.suite',
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
