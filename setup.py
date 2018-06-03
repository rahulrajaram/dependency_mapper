import setuptools


setuptools.setup(
    author='Rahul Rajaram',
    author_email='rahulrajaram2005@gmail.com',
    description='Draw the header-file dependency map of your C/C++ project',
    entry_points={
        'console_scripts': ['dependency_mapper=dependency_mapper.dependency_mapper:describe_headers'],
    },
    install_requires=[
        'six',
        'tabulate'
    ],
    license='MIT',
    name='dependency_mapper',
    packages=['dependency_mapper'],
    url='http://github.com/rahulrajaram/dependency_mapper',
    version='0.0.1',
    zip_safe=True
)
