#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>
#include <cstdint>

namespace fs = std::filesystem;

// Константы для цветов BMP
constexpr uint8_t kWhite[3] = {255, 255, 255};
constexpr uint8_t kGreen[3] = {0, 255, 0};
constexpr uint8_t kPurple[3] = {128, 0, 128};
constexpr uint8_t kYellow[3] = {255, 255, 0};
constexpr uint8_t kBlack[3] = {0, 0, 0};

// Структура для BMP заголовка
#pragma pack(push, 1)
struct BmpHeader {
    uint16_t signature = 0x4D42;
    uint32_t file_size;
    uint32_t reserved = 0;
    uint32_t data_offset = 54;
    uint32_t header_size = 40;
    int32_t width;
    int32_t height;
    uint16_t planes = 1;
    uint16_t bits_per_pixel = 24;
    uint32_t compression = 0;
    uint32_t image_size;
    int32_t x_pixels_per_m = 0;
    int32_t y_pixels_per_m = 0;
    uint32_t colors_used = 0;
    uint32_t important_colors = 0;
};
#pragma pack(pop)

void WriteBmp(const std::vector<std::vector<uint64_t>>& grid, 
              const fs::path& output_path, uint16_t width, uint16_t height) {
    std::ofstream bmp_file(output_path, std::ios::binary);
    if (!bmp_file) {
        std::cerr << "Failed to create BMP file: " << output_path << std::endl;
        return;
    }

    const uint32_t row_size = ((width * 3 + 3) / 4) * 4;
    const uint32_t image_size = row_size * height;

    BmpHeader header;
    header.file_size = sizeof(BmpHeader) + image_size;
    header.width = width;
    header.height = height;
    header.image_size = image_size;

    bmp_file.write(reinterpret_cast<const char*>(&header), sizeof(header));

    std::vector<uint8_t> row(row_size, 0);
    for (int y = height - 1; y >= 0; --y) {
        for (uint16_t x = 0; x < width; ++x) {
            const uint64_t grains = grid[y][x];
            const uint8_t* color = kBlack;
            
            if (grains == 0) color = kWhite;
            else if (grains == 1) color = kGreen;
            else if (grains == 2) color = kPurple;
            else if (grains == 3) color = kYellow;

            const size_t offset = x * 3;
            row[offset] = color[2];     // B
            row[offset + 1] = color[1]; // G
            row[offset + 2] = color[0]; // R
        }
        bmp_file.write(reinterpret_cast<const char*>(row.data()), row_size);
    }
}

class Sandpile {
public:
    Sandpile(uint16_t width, uint16_t height) : width_(width), height_(height) {
        grid_.resize(height, std::vector<uint64_t>(width, 0));
    }

    void LoadFromFile(const fs::path& input_path) {
        std::ifstream file(input_path);
        if (!file) {
            throw std::runtime_error("Cannot open input file");
        }

        uint16_t x, y;
        uint64_t grains;
        while (file >> x >> y >> grains) {
            if (x >= width_ || y >= height_) {
                throw std::out_of_range("Coordinates out of grid bounds");
            }
            grid_[y][x] = grains;
        }
    }

    void Simulate(uint32_t max_iter, uint32_t freq, const fs::path& output_dir) {
        if (!fs::exists(output_dir)) {
            fs::create_directory(output_dir);
        }

        for (uint32_t iter = 0; iter < max_iter; ++iter) {
            if (IsStable()) break;

            Topple();

            if (freq > 0 && iter % freq == 0) {
                const std::string filename = "iter_" + std::to_string(iter) + ".bmp";
                WriteBmp(grid_, output_dir / filename, width_, height_);
            }
        }
        WriteBmp(grid_, output_dir / "final.bmp", width_, height_);
    }

private:
    bool IsStable() const {
        for (const auto& row : grid_) {
            for (uint64_t grains : row) {
                if (grains > 3) return false;
            }
        }
        return true;
    }

    void Topple() {
        for (uint16_t y = 0; y < height_; ++y) {
            for (uint16_t x = 0; x < width_; ++x) {
                if (grid_[y][x] > 3) {
                    const uint64_t grains = grid_[y][x] / 4;
                    grid_[y][x] %= 4;

                    if (x > 0) grid_[y][x-1] += grains;
                    if (x < width_-1) grid_[y][x+1] += grains;
                    if (y > 0) grid_[y-1][x] += grains;
                    if (y < height_-1) grid_[y+1][x] += grains;
                }
            }
        }
    }

    std::vector<std::vector<uint64_t>> grid_;
    uint16_t width_;
    uint16_t height_;
};

int main(int argc, char* argv[]) {
    if (argc < 5) {
        std::cout << "Usage: " << argv[0] << " -l LENGTH -w WIDTH [-i INPUT] [-o OUTPUT] [-m MAX_ITER] [-f FREQ]\n";
        return 1;
    }

    try {
        uint16_t length = 10, width = 10;
        fs::path input = "input.tsv";
        fs::path output = "output";
        uint32_t max_iter = 100, freq = 0;

        for (int i = 1; i < argc; ++i) {
            std::string arg = argv[i];
            if ((arg == "-l" || arg == "--length") && i+1 < argc) {
                length = static_cast<uint16_t>(std::stoi(argv[++i]));
            } else if ((arg == "-w" || arg == "--width") && i+1 < argc) {
                width = static_cast<uint16_t>(std::stoi(argv[++i]));
            } else if ((arg == "-i" || arg == "--input") && i+1 < argc) {
                input = argv[++i];
            } else if ((arg == "-o" || arg == "--output") && i+1 < argc) {
                output = argv[++i];
            } else if ((arg == "-m" || arg == "--max-iter") && i+1 < argc) {
                max_iter = static_cast<uint32_t>(std::stoi(argv[++i]));
            } else if ((arg == "-f" || arg == "--freq") && i+1 < argc) {
                freq = static_cast<uint32_t>(std::stoi(argv[++i]));
            }
        }

        Sandpile sandpile(length, width);
        sandpile.LoadFromFile(input);
        sandpile.Simulate(max_iter, freq, output);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}