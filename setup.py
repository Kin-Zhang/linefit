from setuptools import setup, find_packages

setup(
    name='linefit',
    version='1.1.0',
    description='linefit ground segmentation algorithm Python bindings',
    author='Qingwen Zhang',
    author_email='qingwen@kth.se',
    url='https://github.com/Kin-Zhang/linefit',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',        
        'Programming Language :: Python :: 3.13',        
    ],
    install_requires=[
        "numpy",
    ],
    python_requires='>=3.8',
)
