from setuptools import setup, Extension
import sys

compile_args = []
link_args = []

if sys.platform == 'win32':
    compile_args = ['-openmp']
    
elif sys.platform == 'darwin':
    compile_args = ['-fopenmp']
    link_args = ['-fopenmp']
    
else:
    compile_args = ['-fopenmp']
    link_args = ['-fopenmp']
    
setup(
    name = 'anycrc',
    version = '0.4.0',
    package_dir = {"": "src"},
    
    ext_modules = [
        Extension(
            name='anycrc.anycrc',
            extra_compile_args=compile_args,
            extra_link_args = link_args,
            sources=['src/anycrc/anycrc.pyx', 'lib/crcany/model.c', 'lib/crcany/crc.c']
        )
    ]
)