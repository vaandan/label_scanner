from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='label_scanner',
    version='0.0.1',
    description='OCR Label Scanner for ERPNext',
    author='LMCP',
    author_email='vandan@logic-motive.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
