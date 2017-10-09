from setuptools import setup, find_packages

packages=[find_packages()]

reqs = [
    "psycopg2"
]

setup(
    name="color-db",
    version="1.0.0",
    url="",
    install_requires=reqs
)