from setuptools import setup, find_packages

setup(
    name='django-googlesearch',
    version='0.0.5',
    description='Django Google custom search engine app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-googlesearch',
    packages = find_packages(),
    include_package_data=True,
    test_suite="setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.0.6',
    ],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
