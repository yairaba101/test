from setuptools import setup
from testyair import __VERSION__

setup(name='testyair',
      version=__VERSION__,
      packages=['testyair'],
      entry_points={
          'console_scripts': [
              'testyair = testyair.qqq:main'
          ]
      },
      )