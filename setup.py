
import platform
from setuptools import setup, find_packages
import versioneer

scripts = ["bin/soapy"]

if (platform.system() == "Windows"):
    scripts.append("bin/soapy.bat")

  
setup(
    name='soapy',
    author='Andrew P. Reeves',
    author_email='andrewpaulreeves@gmail.com',
    packages=find_packages(),
    scripts=scripts,
    description='A tomographic astronomical adaptive optics simulation with realistic laser guide star propagation.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.7.0, < 1.26",
        "scipy >= 0.15.0",
        "astropy >= 1.0",
        "aotools >= 1.0",
        "pyfftw >= 0.12.0",
        "pyyaml >= 5.1.1",
        "numba >= 0.40",
        "ipython >= 8.0",
        "pyqt5 >= 5.0",
        "qtconsole >= 5.0",
        "pyqtgraph >= 0.13"
      ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
