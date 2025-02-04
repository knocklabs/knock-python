import setuptools
import os

base_dir = os.path.dirname(__file__)

with open("README.md", "r") as f:
    long_description = f.read()

about = {}
with open(os.path.join(base_dir, "knockapi", "__about__.py")) as f:
    exec(f.read(), about)


def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setuptools.setup(
    name='knockapi',
    version=about['__version__'],
    python_requires='>=2.7.16, <4',
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
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
