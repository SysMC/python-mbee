from distutils.core import setup

setup(
    name='python-mbee',
    version="1.0",
    author='von Boduen',
    author_email='mbee@sysmc.ru',
    packages=['mbee'],
    package_data = {'mbee': ['doc/*/*.*']},
    url='https://github.com/SysMC/python-mbee',
    license='MIT',
    description='Python tools for working with MBee radios.',
    long_description=open('README.txt').read(),
    requires=['pySerial']
)
