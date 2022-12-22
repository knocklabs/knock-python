import setuptools

version = '0.5.1'

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='knockapi',
    version=version,
    python_requires='>=2.7.16, <4',
    install_requires=[
        'requests'
    ],
    extras_require={
        'dev': [
            'bump2version',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='Client library for the Knock API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/knocklabs/knock-python',
    packages=setuptools.find_packages(),
    author='Knock Labs, Inc.',
    author_email='support@knock.app',
    license='MIT'
)
