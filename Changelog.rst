ChangeLog of MultiAnalyzer
==========================

Version 0.7 (12/2024)
---------------------
Take the output grid position from the scan command.
Better reproducibility.

Version 0.6 (05/2023)
---------------------
Migration to meson-python as build system. Numpy-distutils is now dead

Version 0.5 (10/2022)
---------------------
Allow each pixel to be treated independently. Can also work with ROI-collection.
New `--order` option
Intrgration to Ewoks 

Version 0.4 (04/2022)
---------------------
Process several entries from a BLISS-file

Version 0.3 (04/2022)
---------------------
Implmentation based on OpenCL. Requires GPU with good double precision performances.
Cython+OpenMP code works and provides equivalent results.


Version 0.2 (12/2021)
---------------------
Application for rebinning a ROI-collection onto a regular grid.

Version 0.1 (10/2021)
---------------------
Calculate the 2theta position for every pixel and perform the rebinning of diffraction data on a regular grid in Cython.
Library version

