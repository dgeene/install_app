from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

METADATA = dict(
    name='install_app',
    version='1.0.0',
    author='David Geene',
    url='https://github.com/dgeene/install_app',
    description='Utility for installing .apk and .ipa files to phones.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['install_app'],
    install_requires=[],
    entry_points = {
        'console_scripts': ['install-app=install_app.command_line:main'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ])

if __name__ == "__main__":
    setup(**METADATA)