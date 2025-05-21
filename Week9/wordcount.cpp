#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

struct FileStats {
    std::size_t lines = 0;
    std::size_t words = 0;
    std::size_t bytes = 0;
    std::size_t chars = 0;
    std::string filename;
};

void PrintUsage() {
    std::cout << "Usage: WordCount.exe [OPTION] filename [filename,.....]\n"
              << "Options:\n"
              << "  -l, --lines    print the line counts\n"
              << "  -c, --bytes    print the byte counts\n"
              << "  -w, --words    print the word counts\n"
              << "  -m, --chars    print the character counts\n"
              << "If no options are specified, -l, -w, -c are assumed\n";
}

FileStats CountFileStats(const std::string& filename) {
    FileStats stats;
    stats.filename = filename;
    
    std::ifstream file(filename, std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filename << "\n";
        return stats;
    }
    
    stats.bytes = file.tellg();
    file.seekg(0, std::ios::beg);
    
    bool inWord = false;
    char ch;
    
    while (file.get(ch)) {
        stats.chars++;
        
        if (ch == '\n') {
            stats.lines++;
        }
        
        if (std::isspace(static_cast<unsigned char>(ch))) {
            if (inWord) {
                stats.words++;
                inWord = false;
            }
        } else {
            inWord = true;
        }
    }
    
    // Count last word if file doesn't end with whitespace
    if (inWord) {
        stats.words++;
    }
    
    return stats;
}

void PrintStats(const FileStats& stats, bool showLines, bool showWords, 
               bool showBytes, bool showChars) {
    if (showLines) {
        std::cout << stats.lines << " ";
    }
    if (showWords) {
        std::cout << stats.words << " ";
    }
    if (showBytes) {
        std::cout << stats.bytes << " ";
    }
    if (showChars) {
        std::cout << stats.chars << " ";
    }
    std::cout << stats.filename << "\n";
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        PrintUsage();
        return 1;
    }
    
    bool showLines = false;
    bool showWords = false;
    bool showBytes = false;
    bool showChars = false;
    bool defaultMode = true;
    
    std::vector<std::string> filenames;
    
    // Parse command line arguments
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        
        if (arg[0] == '-') {
            defaultMode = false;
            
            if (arg == "-l" || arg == "--lines") {
                showLines = true;
            } else if (arg == "-w" || arg == "--words") {
                showWords = true;
            } else if (arg == "-c" || arg == "--bytes") {
                showBytes = true;
            } else if (arg == "-m" || arg == "--chars") {
                showChars = true;
            } else if (arg.size() > 1 && arg[0] == '-' && arg[1] != '-') {
                // Handle combined options like -lwc
                for (size_t j = 1; j < arg.size(); ++j) {
                    switch (arg[j]) {
                        case 'l': showLines = true; break;
                        case 'w': showWords = true; break;
                        case 'c': showBytes = true; break;
                        case 'm': showChars = true; break;
                        default:
                            std::cerr << "Error: Unknown option -" << arg[j] << "\n";
                            PrintUsage();
                            return 1;
                    }
                }
            } else {
                std::cerr << "Error: Unknown option " << arg << "\n";
                PrintUsage();
                return 1;
            }
        } else {
            filenames.push_back(arg);
        }
    }
    
    if (defaultMode) {
        showLines = true;
        showWords = true;
        showBytes = true;
    }
    
    if (filenames.empty()) {
        std::cerr << "Error: No input files specified\n";
        PrintUsage();
        return 1;
    }
    
    // Process each file
    for (const auto& filename : filenames) {
        FileStats stats = CountFileStats(filename);
        PrintStats(stats, showLines, showWords, showBytes, showChars);
    }
    
    return 0;
}
