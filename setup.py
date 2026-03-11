from setuptools import setup, find_packages

setup(
    name='deep-jscc-starter',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A starter package for deep-jscc projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Symbol-WANG/deep-jscc-starter',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # Example: 'numpy', 'pandas', etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)