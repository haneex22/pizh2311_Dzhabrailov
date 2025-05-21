#include "number.h"
#include <algorithm>
#include <stdexcept>
#include <cstring>

uint2022_t from_uint(uint32_t i) {
    uint2022_t result;
    result.chunks[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result;
    std::string str(buff);
    
    if (str.empty()) {
        return result;
    }

    for (char c : str) {
        if (!isdigit(c)) {
            throw std::invalid_argument("Invalid character in input string");
        }
    }

    for (size_t i = 0; i < str.size(); ++i) {
        uint32_t carry = 0;
        for (size_t j = 0; j < result.chunks.size(); ++j) {
            uint64_t product = static_cast<uint64_t>(result.chunks[j]) * 10 + carry;
            result.chunks[j] = static_cast<uint32_t>(product & 0xFFFFFFFF);
            carry = static_cast<uint32_t>(product >> 32);
        }
        if (carry != 0) {
            throw std::overflow_error("Number is too large for uint2022_t");
        }

        uint32_t digit = str[i] - '0';
        carry = digit;
        for (size_t j = 0; j < result.chunks.size() && carry != 0; ++j) {
            uint64_t sum = static_cast<uint64_t>(result.chunks[j]) + carry;
            result.chunks[j] = static_cast<uint32_t>(sum & 0xFFFFFFFF);
            carry = static_cast<uint32_t>(sum >> 32);
        }
        if (carry != 0) {
            throw std::overflow_error("Number is too large for uint2022_t");
        }
    }

    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint32_t carry = 0;

    for (size_t i = 0; i < lhs.chunks.size(); ++i) {
        uint64_t sum = static_cast<uint64_t>(lhs.chunks[i]) + rhs.chunks[i] + carry;
        result.chunks[i] = static_cast<uint32_t>(sum & 0xFFFFFFFF);
        carry = static_cast<uint32_t>(sum >> 32);
    }

    if (carry != 0 || (lhs.chunks.back() > 0 && rhs.chunks.back() > 0 && result.chunks.back() < std::min(lhs.chunks.back(), rhs.chunks.back()))) {
        throw std::overflow_error("Addition overflow in uint2022_t");
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint32_t borrow = 0;

    for (size_t i = 0; i < lhs.chunks.size(); ++i) {
        uint64_t diff = static_cast<uint64_t>(lhs.chunks[i]) - rhs.chunks[i] - borrow;
        result.chunks[i] = static_cast<uint32_t>(diff & 0xFFFFFFFF);
        borrow = (diff >> 32) ? 1 : 0;
    }

    if (borrow != 0) {
        throw std::underflow_error("Subtraction underflow in uint2022_t");
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    std::array<uint64_t, uint2022_t::kChunks * 2> temp = {0};

    for (size_t i = 0; i < lhs.chunks.size(); ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < rhs.chunks.size(); ++j) {
            uint64_t product = static_cast<uint64_t>(lhs.chunks[i]) * rhs.chunks[j] + temp[i + j] + carry;
            temp[i + j] = product & 0xFFFFFFFF;
            carry = product >> 32;
        }
        if (carry != 0) {
            throw std::overflow_error("Multiplication overflow in uint2022_t");
        }
    }

    for (size_t i = lhs.chunks.size(); i < temp.size(); ++i) {
        if (temp[i] != 0) {
            throw std::overflow_error("Multiplication overflow in uint2022_t");
        }
    }

    for (size_t i = 0; i < result.chunks.size(); ++i) {
        result.chunks[i] = static_cast<uint32_t>(temp[i]);
    }

    return result;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    return lhs.chunks == rhs.chunks;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    if (value == uint2022_t()) {
        stream << "0";
        return stream;
    }

    uint2022_t tmp = value;
    std::string result;
    
    while (tmp != uint2022_t()) {
        uint32_t remainder = 0;
        for (int i = tmp.chunks.size() - 1; i >= 0; --i) {
            uint64_t dividend = (static_cast<uint64_t>(remainder) << 32) + tmp.chunks[i];
            tmp.chunks[i] = static_cast<uint32_t>(dividend / 10);
            remainder = static_cast<uint32_t>(dividend % 10);
        }
        result.push_back('0' + remainder);
    }

    std::reverse(result.begin(), result.end());
    stream << result;
    return stream;
}

bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = lhs.chunks.size() - 1; i >= 0; --i) {
        if (lhs.chunks[i] > rhs.chunks[i]) {
            return true;
        } else if (lhs.chunks[i] < rhs.chunks[i]) {
            return false;
        }
    }
    return true;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == uint2022_t()) {
        throw std::invalid_argument("Division by zero");
    }

    if (lhs == uint2022_t()) {
        return uint2022_t();
    }

    if (rhs == from_uint(1)) {
        return lhs;
    }

    uint2022_t quotient;
    uint2022_t remainder;
    uint2022_t divisor = rhs;

    for (int i = lhs.chunks.size() * 32 - 1; i >= 0; --i) {
        remainder = remainder + remainder;
        if ((lhs.chunks[i / 32] >> (i % 32)) & 1) {
            remainder.chunks[0] |= 1;
        }

        if (remainder >= divisor) { 
            remainder = remainder - divisor;
            quotient.chunks[i / 32] |= (1 << (i % 32));
        }
    }

    return quotient;
}
