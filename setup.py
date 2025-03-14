from setuptools import setup, find_packages

setup(
    name="kivy_desktop",
    version="0.0.1",
    author="Beltrán Offerrall",
    packages=find_packages(),
    package_data={
        'kivy_desktop': ['*.kv', 'resources/images/*.png'],
    },
    install_requires=[
        'kivy',
    ],
)
