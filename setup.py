from setuptools import setup

setup(name='saphires',
      version='0.1.9',
      description='Stellar Analysis in Python for HIgh-REsolution Spectroscopy',
      author='Ben Tofflemire',
      author_email='tofflemire@utexas.edu',
      url='https://github.com/tofflemire/saphires',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Astronomy',
          ],
      packages=['saphires','saphires.extras'],
      requires=['numpy',
                'astropy',
                'scipy',
                'matplotlib',
                'pickle',
                'PyQt5',
                'pdyl'])
