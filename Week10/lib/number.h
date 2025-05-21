#pragma once
#include <cinttypes>
#include <iostream>
#include <array>
#include <string>

struct uint2022_t {
    static const size_t kBits = 2022;                        // Количество бит в числе
    static const size_t kBytes = (kBits + 7) / 8;            // Байт (253)
    static const size_t kChunks = (kBits + 31) / 32;         // 32-битных слов (64)
    std::array<uint32_t, kChunks> chunks;                    // Хранилище данных
 
    uint2022_t() {                                           // Конструктор (инициализация нулями)
        chunks.fill(0);
    }
};

static_assert(sizeof(uint2022_t) <= 300, "Size of uint2022_t must be no higher than 300 bytes");

uint2022_t from_uint(uint32_t i);

uint2022_t from_string(const char* buff);

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs);

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs);

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs);

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs);

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value);
