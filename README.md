# PyRLGR

Run Length Golomb Rice

A Python port of the Adaptive Run Length Golomb Rice encoding algorithm.

---

## Prerequisites

### Linux, macOS

* Compiler with C++11 support
* CMake >= 2.8.12

### Windows

* Visual Studio 2015
* CMake >= 3.1

## Installation

Just clone this repository and install via pip. Note the `--recursive` option which is
needed for the pybind11 submodule:

```bash
git clone --recursive <git clone URL>
pip install .
```

With the `setup.py` file included in this example, the `pip install .` command will
invoke CMake and build the pybind11 module as specified in `CMakeLists.txt`.

Note: We recommend the usage of a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Note: Uninstall via:

```bash
pip uninstall pyrlgr
```

## Pybind11 Example

```python
import pybind11_example
pybind11_example.add(1, 2)
```

## Python Unit Tests

Python unit tests are done using Python's built-in ``unittest`` module. Python unit tests live in the ``tests`` folder. As long as all of your files match ``'test*.py'``, ``unittest`` will automatically discover them. Run ``python3 -m unittest discover [--verbose]`` to run all unit tests.

## C++ Unit Tests

C++ unit tests are done using Catch2 (https://github.com/catchorg/Catch2). C++ unit tests live in the ``tests`` folder. The tests executable can be built with CMake. On Linux/macOS use the following commands to build the tests executable:

```bash
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make --jobs
```

This will leave the tests executable under ``build/tests/tests``.

## Credits

### RLGR Algorithm
For a more technical/scientific description of RLGR, you may want to have a look at:
```
H. S. Malvar, "Adaptive run-length/Golomb-Rice encoding of quantized generalized Gaussian sources with unknown statistics," Data Compression Conference (DCC'06), 2006, pp. 23-32, doi: 10.1109/DCC.2006.5. 
```

### Original C++ implementation
Taken from the RATH implementation of the [Digital Image and Video Processing Group](https://github.com/digitalivp) in Brasil:
`https://github.com/digitalivp/RAHT`

## Who do I talk to?

Christian Rohlfing <[rohlfing@ient.rwth-aachen.de](mailto:rohlfing@ient.rwth-aachen.de)>

Thibaut Meyer <[thibaut.meyer@ient.rwth-aachen.de](mailto:thibaut.meyer@ient.rwth-aachen.de)>
