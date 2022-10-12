#include <stdio.h>
#include <stdint.h>
#include <cstdint>
#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>
#include <pybind11/stl.h>
#include <vector>
#include "file.h"

namespace py = pybind11;

PYBIND11_MODULE(rlgr, m) {
  m.doc() = "pybind11 rlgr";

    py::class_<file>(m, "file")
      .def(py::init<char*, uint_least8_t>())
      .def("rlgrRead", [](file &m, size_t N, uint_least8_t flagSigned) {
        std::vector<int64_t> seq(N, 0);
        m.rlgrRead(seq.data(), N, flagSigned);
        return seq;
      })
      .def("rlgrWrite", [](file &m, std::vector<int64_t> seq, uint_least8_t flagSigned) {
        m.rlgrWrite(seq.data(), seq.size(), flagSigned);
      })
      .def("grRead", &file::grRead)
      .def("grWrite", &file::grWrite)
      .def("openError", &file::openError)
      .def("close", &file::close);
}
