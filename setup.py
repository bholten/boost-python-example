from distutils.core import setup, Extension

hello_module = Extension(
    'boost_example.hello',
    sources=['boost_example/ext/hello.cpp'],
    include_dirs=['/usr/include/python2.7'],
    library_dirs=['/usr/include/boost'],
    runtime_library_dirs=['/usr/include/boost'],
    libraries=['boost_python']
)

setup(
    name='boost_example',
    version='1',
    packages=['boost_example'],
    url='https://github.com/bholten/boost-python-example',
    license='wtfpl',
    author='Brennan Holten',
    author_email='brennan.holten@objectpartners.com',
    description='Example showing a trivial C++ extension with Boost',
    ext_modules=[hello_module]
)
