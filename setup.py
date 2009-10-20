from setuptools import setup, find_packages

install_requires = ['BeautifulSoup']

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License (GPL)
Programming Language :: Python
Development Status :: 3 - Alpha
"""

setup(
    name = 'pybhl',
    version = '0.1',  # remember to update pybhl/__init__.py on release!
    url = 'http://github.com/anarchivist/pybhl',
    author = 'Mark A. Matienzo',
    author_email = 'mark@matienzo.org',
    license = 'GPL',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'Interact with the Biodiversity Heritage Library API',
    classifiers = filter(None, classifiers.split('\n')),
)
