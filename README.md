histogram
==================================================
[![Build Status](https://travis-ci.org/nul-one/histogram.png)](https://travis-ci.org/nul-one/histogram)
[![PyPI version](https://badge.fury.io/py/histogram.svg)](https://badge.fury.io/py/histogram)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Requirements Status](https://requires.io/github/nul-one/histogram/requirements.svg?branch=master)](https://requires.io/github/nul-one/histogram/requirements/?branch=master)

Draw histogram based on a set of integers from STDIN.

Installation
-------------------------

### install from pypi (recommend)
`pip3 install histogram`

### install from github (latest master)
`pip3 install -U git+https://github.com/nul-one/histogram.git`

Usage
-------------------------

```
Description:
    histogram - draw histogram based on a set of integers from STDIN. Input
    is a string of integers, one per line. Lines with bad values will simply
    be skipped. Note that graph is rotated by -90 degrees.

Usage: histogram [OPTIONS]

Options:
    -h      - display this help and exit
    -c      - graph will display cumulative values
    -r      - reverse order of values
    -p      - show percentage on the right side instead of counts
    -t S    - for long inputs: show results periodically every S seconds
    -s S    - for short inputs: sleep S seconds after every entry
    -l N    - show results for last N values only
    -W      - graph width in number of lines (defaults to available lines)
    -H      - graph height in number of chars (defaults to available chars)

Example:
    for x in $(seq 1000); do echo $RANDOM; done | histogram -p
```

