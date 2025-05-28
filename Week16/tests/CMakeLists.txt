include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(test_adapters test_adapters.cpp)
target_link_libraries(test_adapters PRIVATE GTest::gtest_main range_adapters)

include(GoogleTest)
gtest_discover_tests(test_adapters)