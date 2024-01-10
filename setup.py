from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    packages=find_packages(),
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your_package_name',
    license='LICENSE',
    install_requires=[
        # List your project dependencies here
    ],
)
