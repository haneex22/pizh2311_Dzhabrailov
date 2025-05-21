#include <lib/number.h>
#include <iostream>
#include <limits>

int main() {
    // Basic operations testing
    std::cout << "=== Basic tests ===" << std::endl;
    uint2022_t a = from_uint(123456789);
    uint2022_t b = from_string("987654321");
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    std::cout << "a + b = " << (a + b) << std::endl;
    std::cout << "b - a = " << (b - a) << std::endl;
    std::cout << "a * b = " << (a * b) << std::endl;
    std::cout << "b / a = " << (b / a) << std::endl;

    // Addition overflow test
    std::cout << "\n=== Addition overflow test ===" << std::endl;
    try {
        uint2022_t max_val;
        for (auto& chunk : max_val.chunks) {
            chunk = std::numeric_limits<uint32_t>::max(); // Все биты установлены в 1
        }
        
        uint2022_t one = from_uint(1);
        uint2022_t overflow = max_val + one;
        
        std::cout << "ERROR: Overflow not detected!" << std::endl;
    } catch (const std::overflow_error& e) {
        std::cout << "Overflow caught: " << e.what() << std::endl;
    }

    // Multiplication overflow test
    std::cout << "\n=== Multiplication overflow test ===" << std::endl;
    try {
        uint2022_t half_max;
        half_max.chunks.back() = 0x80000000; // 2^2019 (для 64 chunks)
        
        uint2022_t overflow = half_max * half_max;
        
        std::cout << "ERROR: Multiplication overflow not detected!" << std::endl;
    } catch (const std::overflow_error& e) {
        std::cout << "Multiplication overflow caught: " << e.what() << std::endl;
    }

    // Subtraction underflow test
    std::cout << "\n=== Subtraction underflow test ===" << std::endl;
    try {
        uint2022_t small = from_uint(5);
        uint2022_t big = from_uint(10);
        uint2022_t result = small - big;
        
        std::cout << "ERROR: Underflow not detected!" << std::endl;
    } catch (const std::underflow_error& e) {
        std::cout << "Underflow caught: " << e.what() << std::endl;
    }

    // Construction from string overflow test
    std::cout << "\n=== String construction overflow test ===" << std::endl;
    try {
        std::string too_large_num = "1";
        too_large_num.append(2022, '0');  // "1" + 2022 zeros = 2^2022
        
        uint2022_t overflow = from_string(too_large_num.c_str());
        
        std::cout << "ERROR: Construction overflow not detected!" << std::endl;
    } catch (const std::overflow_error& e) {
        std::cout << "Construction overflow caught: " << e.what() << std::endl;
    }

    // Division by zero test
    std::cout << "\n=== Division by zero test ===" << std::endl;
    try {
        uint2022_t zero = from_uint(0);
        uint2022_t some_num = from_uint(10);
        uint2022_t result = some_num / zero;
        
        std::cout << "ERROR: Division by zero not detected!" << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cout << "Division by zero caught: " << e.what() << std::endl;
    }

    return 0;
}