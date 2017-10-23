from setuptools import setup

setup(
    name='pretty-json',
    packages=[
        'pretty_json'
    ],
    version='1.1.0',
    include_package_data=True,
    description='make pretty json',
    long_description=open('README.rst').read(),
    url='https://github.com/devstuff-io/pretty-json',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=[
        'Pygments',
        'pygments-json'
    ],
    keywords=[
        'pretty',
        'json'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
