set(source_files
        file.cpp
)

add_library(rlgr_internal ${source_files})
add_library(rlgr_pybind11_internal ${source_files})
pybind11_add_module(rlgr ${source_files} bindings.cpp)
