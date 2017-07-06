from setuptools import setup

setup(name='testyair',
      version='0.1.0',
      packages=['testyair'],
      entry_points={
          'console_scripts': [
              'testyair = testyair.qqq:main'
          ]
      },
      )