subdir('app')
subdir('test')

py.install_sources([
	'__init__.py',
	'file_io.py',
	'multianalyzer.cl',
	'opencl.py',
	'timer.py',
	'utils.py',
],
  pure: false,    # Will be installed next to binaries
  subdir: 'multianalyzer'  # Folder relative to site-packages to install to
)

# OpenMP can be used
omp = dependency('openmp', required : false)

py.extension_module('_multianalyzer', '_multianalyzer.pyx',
        dependencies : [py_dep, omp], install: true, subdir: 'multianalyzer')
