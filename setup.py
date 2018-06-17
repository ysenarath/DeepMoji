from setuptools import setup

setup(
    name='deepmoji',
    version='1.0',
    packages=['deepmoji'],
    description='deepmoji library',
    include_package_data=True,
    install_requires=[
        'emoji',
        'h5py',
        'Keras',
        'numpy',
        'scikit-learn',
        'text-unidecode',
    ],
)
