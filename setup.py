from setuptools import setup, find_packages

setup(
    name='jippity',
    version='0.1',    
    description='a simple cli wrapper around chat gpt',
    url='https://github.com/cookbenjamin/jippity',
    author='Benjamin Cook',
    author_email='cookbenjamin@gmail.com',
    license='MIT Licence',
    package_dir={'': 'src'},  # Define the directory where your packages are
    packages=find_packages(where='src'),
    install_requires=['openai==1.30.1',
                      'pygments==2.18.0',],
    entry_points={
        'console_scripts': [
            'jip = jippity.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3',
      ],
)

