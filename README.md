# Neuro Digital Signal Processing Toolbox

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Latest Version](https://img.shields.io/pypi/v/neurodsp.svg)](https://pypi.python.org/pypi/neurodsp/)
[![Build Status](https://travis-ci.org/neurodsp-tools/neurodsp.svg)](https://travis-ci.org/neurodsp-tools/neurodsp)
[![codecov](https://codecov.io/gh/neurodsp-tools/neurodsp/branch/master/graph/badge.svg)](https://codecov.io/gh/neurodsp-tools/neurodsp)
[![License](https://img.shields.io/pypi/l/neurodsp.svg)](https://opensource.org/licenses/Apache-2.0)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/neurodsp.svg)](https://pypi.python.org/pypi/neurodsp/)
[![DOI](http://joss.theoj.org/papers/10.21105/joss.01272/status.svg)](https://doi.org/10.21105/joss.01272)

Tools to analyze and simulate neural time series, using digital signal processing.

## Documentation

Documentation for the NeuroDSP module is available [here](https://neurodsp-tools.github.io/neurodsp/).

The documentation includes:
- [Tutorials](https://neurodsp-tools.github.io/neurodsp/auto_tutorials/index.html):
which describe and work through each module in NeuroDSP
- [Examples](https://neurodsp-tools.github.io/neurodsp/auto_examples/index.html):
demonstrating example applications and workflows
- [API List](https://neurodsp-tools.github.io/neurodsp/api.html):
which lists and describes all the code and functionality available in the module
- [Glossary](https://neurodsp-tools.github.io/neurodsp/glossary.html):
which defines all the key terms used in the module

If you have a question about using NeuroDSP that doesn't seem to be covered by the documentation, feel free to
open an [issue](https://github.com/neurodsp-tools/neurodsp/issues) and ask!

## Dependencies

NeuroDSP is written in Python, and requires Python >= 3.5 to run.

It has the following dependencies:
- [numpy](https://github.com/numpy/numpy)
- [scipy](https://github.com/scipy/scipy)
- [matplotlib](https://github.com/matplotlib/matplotlib)

Optional dependencies:
- [pytest](https://github.com/pytest-dev/pytest) is needed if you want to run the test suite locally

We recommend using the [Anaconda](https://www.continuum.io/downloads) distribution to manage these requirements.

## Install

**Stable Release Version**

To install the latest stable release, use pip:

`$ pip install neurodsp`

**Development Version**

To get the current development version, first clone this repository:

`$ git clone https://github.com/neurodsp-tools/neurodsp`

To install this cloned copy, move into the directory you just cloned, and run:

`$ pip install .`

**Editable Version**

To install an editable version, download the development version as above, and run:

`$ pip install -e .`

## Bug Reports

Please use the
[Github issue tracker](https://github.com/neurodsp-tools/neurodsp/issues)
to file bug reports and/or ask questions about this project.

## Modules

Available modules in NeuroDSP include:

- ```filt``` : Filter data with bandpass, highpass, lowpass, or notch filters
- ```burst``` : Detect bursting oscillations in neural signals
- ```rhythm``` : Find and analyze rhythmic and recurrent patterns in time series
- ```spectral``` : Compute spectral domain features such as power spectra
- ```timefrequency``` : Estimate instantaneous measures of oscillatory activity
- ```sim``` : Simulate time series, including periodic and aperiodic signal components
- ```plts``` : Plotting functions

## Contribute

`NeuroDSP` welcomes and encourages contributions from the community!

If you have an idea of something to add to NeuroDSP, please start by opening an
[issue](https://github.com/neurodsp-tools/neurodsp/issues).

When writing code to add to NeuroDSP, please follow the
[Contribution Guidelines](https://github.com/neurodsp-tools/neurodsp/blob/master/CONTRIBUTING.md).

We also require that all contributors follow our
[Code of Conduct](https://github.com/neurodsp-tools/neurodsp/blob/master/CODE_OF_CONDUCT.md).

## Reference

If you use this code in your project, please cite:

```
Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019). NeuroDSP: A package for
neural digital signal processing. Journal of Open Source Software, 4(36), 1272.
DOI: 10.21105/joss.01272
```

Direct Link: https://doi.org/10.21105/joss.01272

Bibtex:
```
@article{cole_neurodsp:_2019,
    title = {NeuroDSP: A package for neural digital signal processing},
    author = {Cole, Scott and Donoghue, Thomas and Gao, Richard and Voytek, Bradley},
    journal = {Journal of Open Source Software},
    year = {2019},
    volume = {4},
    number = {36},
    issn = {2475-9066},
    url = {http://joss.theoj.org/papers/10.21105/joss.01272},
    doi = {10.21105/joss.01272},
}
```
