cmake_minimum_required(VERSION 3.10)
project(Id3v2Parser)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(id3v2_parser main.cpp id3v2_parser.cpp)