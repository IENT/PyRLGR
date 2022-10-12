set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(source_files
        catch_main.cpp
        test_math.cpp
)

add_executable(tests ${source_files})

target_link_libraries(tests PRIVATE)
target_link_libraries(tests PRIVATE pybind11_example_internal)
