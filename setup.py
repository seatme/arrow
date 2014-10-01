try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='arrow',
    version='0.4.4sm0',
    description='Better dates and times for Python',
    url='http://crsmithdev.com/arrow',
    author='Chris Smith',
    author_email="crsmithdev@gmail.com",
    license='Apache 2.0',
    packages=['arrow'],
    zip_safe=False,
    install_requires=[
        'python-dateutil'
    ],
    test_suite="tests",
)

