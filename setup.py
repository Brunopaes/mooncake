from distutils.core import setup

setup(
    name='TreeShrews',
    version='0.1.0',
    author=['Bruno Paes'],
    author_email=['brunopaes05@gmail.com'],
    packages=[''],
    scripts=['src/propagation.py'],
    url=None,
    license=None,
    description='ANN Module',
    long_description=open('../README.md').read(),
    install_requires=[
        "Pandas >= 0.24.2",
    ])
