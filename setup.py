from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='scrapy_utils',
    version='0.1.0',
    description='A collection of utility functions for use with the Scrapy web crawling framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dionysio/scrapy_utils',
    author='dio',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
    ],
    keywords='scrapy web scraping utilities',
    packages=find_packages(),
    install_requires=[
        'scrapy>=2.5.0',
        # Add any additional dependencies here
    ],
    python_requires='>=3.7',
    project_urls={
        'Bug Reports': 'https://github.com/your_username/scrapy_utils/issues',
        'Source': 'https://github.com/your_username/scrapy_utils',
    },
)