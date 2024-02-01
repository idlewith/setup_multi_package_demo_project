from setuptools import setup, find_packages


setup(
    name="multi_package_demo",
    version="0.0.1",
    description="multiple packages demo description",
    packages=find_packages(),
    setup_requires=["wheel"],
)
