cmake_minimum_required(VERSION 3.14)
project(RangeAdapters)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(lib)
add_subdirectory(bin)

enable_testing()
add_subdirectory(tests)