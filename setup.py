from setuptools import setup

setup(
    name='learnad',

    packages=['learnad'],

    include_package_data=True,

    version='0.1',

    description='News API',

    author='Ryan Hallisey',

    author_email='rthallisey@gmail.com',

    install_requires=['requests>=2.0.0,<3.0.0'],

    test_suite='nose.collector',

    tests_require=['nose', 'requests_mock'],

    url='https://github.com/rthallisey/learnad',

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
