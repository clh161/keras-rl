from setuptools import setup
from setuptools import find_packages


setup(name='keras-rl',
      version='0.3.1',
      description='Deep Reinforcement Learning for Keras',
      author='Matthias Plappert',
      author_email='matthiasplappert@me.com',
      url='https://github.com/matthiasplappert/keras-rl',
      download_url='https://github.com/matthiasplappert/keras-rl/archive/v0.3.1.tar.gz',
      license='MIT',
      install_requires=['keras>=1.0.7,<2.4.4'],
      extras_require={
          'gym': ['gym'],
      },
      packages=find_packages())
