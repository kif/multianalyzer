# coding: utf-8
# /*##########################################################################
# Copyright (C) 2016-2018 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/

__authors__ = ["V. Valls"]
__license__ = "MIT"
__date__ = "07/12/2021"

from numpy.distutils.misc_util import Configuration
import platform
import os
import numpy


def create_extension_config(name, extra_sources=None, can_use_openmp=False):
    """
    Util function to create numpy extension from the current pyFAI project.
    Prefer using numpy add_extension without it.
    """
    include_dirs = [numpy.get_include()]

    if can_use_openmp:
        extra_link_args = ['-fopenmp']
        extra_compile_args = ['-fopenmp']
    else:
        extra_link_args = []
        extra_compile_args = ["-ftree-vectorize"]

    sources = ["%s.pyx" % name]
    if extra_sources is not None:
        sources.extend(extra_sources)

    config = dict(
        name=name,
        sources=sources,
        include_dirs=include_dirs,
        language='c',
        extra_link_args=extra_link_args,
        extra_compile_args=extra_compile_args
    )

    return config


def configuration(parent_package='', top_path=None):
    config = Configuration('multianalyzer', parent_package, top_path)

    ext_modules = [
        create_extension_config("_multianalyzer", can_use_openmp=True),
        # create_extension_config("_cormap", can_use_openmp=False),
        # create_extension_config("_autorg", can_use_openmp=False),
        # create_extension_config("_bift", can_use_openmp=False),
    ]

    for ext_config in ext_modules:
        config.add_extension(**ext_config)

    config.add_subpackage('test')
    config.add_subpackage('app')

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
