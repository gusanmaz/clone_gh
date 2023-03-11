from setuptools import setup, find_packages

setup(
    name='clone_gh',
    version='0.1',
    packages=find_packages(),
    package_data={
        'clone_gh': ['languages.json'],
    },
    install_requires=[
        'gitpython',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'clone_gh=clone_gh:main'
        ]
    },
    author='Güvenç Usanmaz',
    author_email='gusanmaz@gmail.com',
    description='Clone all starred Github repositories for a given username and programming language',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gusanmaz/clone_gh',
    license='MIT',
    keywords=['github', 'clone', 'starred', 'repositories'],
    python_requires='>=3.6',
    platforms=['any'],
    project_urls={
        'Bug Reports': 'https://github.com/gusanmaz/clone_gh/issues',
        'Source': 'https://github.com/gusanmaz/clone_gh',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
