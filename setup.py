from setuptools import setup, find_packages

description = 'A Django Field for creating templated sequence strings.'

try:
    with open('README.md') as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name='django-sequence-field',
    version='0.2.4',
    description=description,
    packages=find_packages(),
    include_package_data=True,
    author='Antonio Ognio',
    author_email='antonio@ognio.com',
    url='https://github.com/gnrfan/django-sequence-field',
    long_description=long_description,
    install_requires=['django >= 1.11'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Database",
    ],
)
